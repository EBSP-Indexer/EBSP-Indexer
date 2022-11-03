from os import path, mkdir

from PySide6.QtWidgets import QDialog
from scripts.setting_file import SettingFile

from utils.filebrowser import FileBrowser
from utils.worker import Worker
from ui.ui_di_setup import Ui_DiSetupDialog

import kikuchipy as kp
import matplotlib.pyplot as plt
import numpy as np
from orix.quaternion import Rotation
from orix import io, sampling, plot
import warnings

# TODO: from time import time
import gc

# Turn interactive plotting off
plt.ioff()

# Ignore warnings to avoid crash with integrated console
warnings.filterwarnings("ignore")

class DiSetupDialog(QDialog):
    """
    Setup dialog box for Dictionary indexing
    """

    def __init__(self, parent=None, pattern_path=None):
        super().__init__(parent)
        # initate threadpool
        self.threadPool = parent.threadPool

        # pattern path
        self.pattern_path = pattern_path

        # working directory
        self.working_dir = path.dirname(self.pattern_path)

        # Standard settings for dictionary indexing
        self.savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)

        # Dialog box ui setup
        self.ui = Ui_DiSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.setupConnections()

        self.setupBinningShapes()

        self.setupInitialSettings()

    def setupBinningShapes(self):
        # Load pattern-file to get acquisition resolution
        try:
            self.s = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

        self.sig_shape = self.s.axes_manager.signal_shape[::-1]
        bin_shapes_1D = np.array([10, 20, 30, 40, 50, 60, 12, 24, 32, 48])
        bin_shapes_2D = np.array(
            [
                "(10, 10)",
                "(20, 20)",
                "(30, 30)",
                "(40, 40)",
                "(50, 50)",
                "(60, 60)",
                "(12, 12)",
                "(24, 24)",
                "(32, 32)",
                "(48, 48)",
            ]
        )
        self.bin_shapes_to_comboBox = bin_shapes_2D[
            np.where(np.array(self.sig_shape[0] % bin_shapes_1D) == 0)[0]
        ]
        self.ui.comboBoxBinning.addItems(self.bin_shapes_to_comboBox)

    def setupInitialSettings(self):
        self.sf = SettingFile(path.join(self.working_dir, "project_settings.txt"))
        try:
            self.pc = np.array(
                [
                    float(self.sf.read("X star:")),
                    float(self.sf.read("Y star:")),
                    float(self.sf.read("Z star:")),
                ]
            )
        except:
            self.pc = np.array([0.000, 0.000, 0.000])

        self.updatePCpatternCenter()
        
        self.mpPaths = {}
        
        i = 1
        while True:
            try:
                mpPath = self.sf.read("Master pattern " + str(i) + ":")
                phase = mpPath.split("/").pop()
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
                i += 1
            except:
                break                

    def updatePCpatternCenter(self):
        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterY.setValue(self.pc[1])
        self.ui.patternCenterZ.setValue(self.pc[2])

    def updatePCArrayFrompatternCenter(self):
        self.pc[0] = self.ui.patternCenterX.value()
        self.pc[1] = self.ui.patternCenterY.value()
        self.pc[2] = self.ui.patternCenterZ.value()

    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mpPath = self.fileBrowserOD.getPaths()[0]
            phase = mpPath.split("/").pop()
            self.fileBrowserOD.setDefaultDir(mpPath[0 : -len(phase) - 1])

            if phase not in self.mpPaths.keys():
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)

    def removePhase(self):
        self.mpPaths.pop(str(self.ui.listWidgetPhase.currentItem().text()))
        self.ui.listWidgetPhase.takeItem(self.ui.listWidgetPhase.currentRow())

    def getPhases(self):
        lw = self.ui.listWidgetPhase
        self.phases = [lw.item(x).text() for x in range(lw.count())]

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_dictionary_indexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

    # read options from interactive elements in dialog box
    def getOptions(self) -> dict:
        return {
            "Phase": self.ui.listWidgetPhase.selectedItems(),
            "Refine": self.ui.checkBoxRefine.isChecked(),
            "Lazy": self.ui.checkBoxLazy.isChecked(),
            "N_iter": int(self.ui.spinBoxNumIter.value()),
            "Disori": float(self.ui.doubleSpinBoxStepSize.value()),
            "Binning": self.ui.comboBoxBinning.currentText(),
            "Mask": [self.ui.checkBoxMask.isChecked(), lambda: self.signal_mask()],
            "IQ": [self.ui.checkBoxIQ.isChecked(), lambda: self.image_quality_map()],
            "ADP": [self.ui.checkBoxADP.isChecked(), lambda: self.average_dot_product()],
            "MI": [self.ui.checkBoxMI.isChecked(), lambda: self.mean_intensity_map()],
            "VBSE": [self.ui.checkBoxVBSE.isChecked(), lambda: self.vbse_image()]
        }

    def run_dictionary_indexing(self):
        # Pass the function to execute
        di_worker = Worker(self.dictionary_indexing)
        # Execute
        self.threadPool.start(di_worker)
        self.accept()

    def signal_mask(self):
        self.signal_mask = ~kp.filters.Window("circular", self.sig_shape).astype(bool)

        # Save figure of signal mask for visualization
        try:
            p = self.s2.inav[0, 0].data
            fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
            ax[0].imshow(p * self.signal_mask, cmap="gray")
            ax[0].set_title("Not used in matching")
            ax[1].imshow(p * ~self.signal_mask, cmap="gray")
            ax[1].set_title("Used in matching")
            fig.savefig(
                path.join(self.results_dir, "circular_mask_for_di.png"),
                **self.savefig_kwargs,
            )

            plt.close(fig)

        except Exception as e:
            raise e

        # Set signal mask for dictionary indexing
        self.di_kwargs["signal_mask"] = self.signal_mask

    def mean_intensity_map(self):
        mean_intensity = self.s.mean(axis=(2, 3))
        plt.imsave(
            path.join(
                self.results_dir, "mean_intensity.png"), mean_intensity.data, cmap="gray"
            )

    def vbse_image(self):
        vbse_gen = kp.generators.VirtualBSEGenerator(self.s)
        red = (2, 1)
        green = (2, 2)
        blue = (2, 3)

        p = vbse_gen.plot_grid(rgb_channels=[red, green, blue])
        p._plot.signal_plot.figure.savefig(
            path.join(self.results_dir, "vbse_rgb_grid.png"), **self.savefig_kwargs
        )

        vbse_rgb_img = vbse_gen.get_rgb_image(r=red, g=green, b=blue)
        vbse_rgb_img.change_dtype("uint8")
        plt.imsave(path.join(self.results_dir, "vbse_rgb.png"), vbse_rgb_img.data)

        plt.close("all")

    def image_quality_map(self):
        # Image quality

        iq = self.s.get_image_quality()
        plt.imsave(path.join(self.results_dir, "iq.png"), iq, cmap="gray")

        plt.close("all")

    def average_dot_product(self):
        # Average dot product map

        adp = self.s.get_average_neighbour_dot_product_map()
        plt.imsave(path.join(self.results_dir, "adp.png"), adp, cmap="gray")

        plt.close("all")

    def dictionary_indexing(self):
        # Create folder for storing DI results in working directory
        i = 1
        while True:
            try:
                self.results_dir = path.join(self.working_dir, "di_results" + str(i))
                mkdir(self.results_dir)
                break
            except FileExistsError:
                print(
                    f"Directory '{self.results_dir}' exists, will try to create directory '{self.results_dir[:-1] + str(i + 1)}'"
                )
            i += 1

        # get options from input
        self.options = self.getOptions()

        # load selected EBSD pattern with current options
        try:
            self.s = kp.load(self.pattern_path, lazy=self.options["Lazy"])
        except Exception as e:
            raise e

        # set pattern center values
        self.updatePCArrayFrompatternCenter()

        # Get phases
        self.getPhases()

        # Refinement
        self.refine = self.options["Refine"]

        # Remaining user input values
        self.new_signal_shape = eval(self.options["Binning"])
        self.disori = self.options["Disori"]
        self.use_signal_mask = self.options["Mask"]

        # If n per iteration is 0
        self.n_per_iteration = None

        if self.options["N_iter"] != 0:
            self.n_per_iteration = self.options["N_iter"]

        # Read metadata from pattern file
        self.energy = self.s.metadata.Acquisition_instrument.SEM.beam_energy
        self.sample_tilt = self.s.detector.sample_tilt

        ### Dictionary indexing

        # Rebinning of signal
        self.nav_shape = self.s.axes_manager.navigation_shape
        self.s2 = self.s.rebin(new_shape=self.nav_shape + self.new_signal_shape)
        self.s2.rescale_intensity(dtype_out=np.uint8)

        # Define detector-sample geometry
        self.sig_shape = self.s2.axes_manager.signal_shape[::-1]

        self.detector = kp.detectors.EBSDDetector(
            shape=self.sig_shape,
            sample_tilt=self.sample_tilt,  # Degrees
            pc=self.pc,
            convention="tsl",  # Default is Bruker, TODO: let user choose convention
        )

        ### Set up dictionary indexing parameters

        self.di_kwargs = dict(
            metric="ncc", keep_n=20, n_per_iteration=self.n_per_iteration
        )
        
        ### additional functions to be performed
        keys = ["Mask", "IQ", "VBSE", "MI", "ADP"]

        for key in keys:
            optionEnabled, optionExecute = self.options[key]
            if optionEnabled:
                optionExecute()

        ### Dictionaries for use with several phases

        # Master pattern dictionary
        self.mp = {}
        for ph in self.phases:
            self.file_mp = path.join(self.mpPaths[ph], f"{ph}_mc_mp_20kv.h5")
            self.mp[f"mp_{ph}"] = kp.load(
                self.file_mp,
                energy=self.energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                projection="lambert",  # stereographic, lambert
                hemisphere="both",  # north, south, both
            )

        # Xmaps dictionary for storing crystalmaps
        self.xmaps = {}
        # Refined xmaps dictionary for storing refined crystalmaps
        self.xmaps_ref = {}

        for ph in self.phases:

            ### Sample orientations

            self.rot = sampling.get_sample_fundamental(
                method="cubochoric",
                resolution=self.disori,
                point_group=self.mp[f"mp_{ph}"].phase.point_group,
            )

            ### Simulate one pattern to check the parameters. The master pattern sampling was implemented by Lars Lervik.

            self.sim = self.mp[f"mp_{ph}"].get_patterns(
                rotations=Rotation.from_euler(np.deg2rad([0, 0, 0])),
                # rotations=rot[0],
                detector=self.detector,
                energy=self.energy,  # Defined above
                compute=True,  # if False, sim.compute() must be called at a later time
            )

            fig = self.detector.plot(
                pattern=self.sim.squeeze().data,
                draw_gnomonic_circles=True,
                coordinates="gnomonic",
                return_figure=True,
            )

            fig.savefig(
                path.join(self.results_dir, f"pc_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)

            ### Generate dictionary

            self.sim_dict = self.mp[f"mp_{ph}"].get_patterns(
                rotations=self.rot,
                detector=self.detector,
                energy=self.energy,
                compute=True,
            )

            self.xmaps[f"xmap_{ph}"] = self.s2.dictionary_indexing(
                dictionary=self.sim_dict, **self.di_kwargs
            )
            self.xmaps[f"xmap_{ph}"].scan_unit = "um"

            ### Save results from DI for phase

            io.save(
                path.join(self.results_dir, f"di_results_{ph}.h5"),
                self.xmaps[f"xmap_{ph}"],
            )  # orix' HDF5
            io.save(
                path.join(self.results_dir, f"di_results_{ph}.ang"),
                self.xmaps[f"xmap_{ph}"],
            )  # .ang

            ### Inspect dictionary indexing results for phase

            fig = self.xmaps[f"xmap_{ph}"].plot(
                value=self.xmaps[f"xmap_{ph}"].scores[:, 0],
                colorbar=True,
                colorbar_label="Normalized cross correlation score",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                path.join(self.results_dir, f"ncc_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)

            ### Calculate and save orientation similairty map

            osm = kp.indexing.orientation_similarity_map(self.xmaps[f"xmap_{ph}"])

            fig = self.xmaps[f"xmap_{ph}"].plot(
                value=osm.ravel(),
                colorbar=True,
                colorbar_label="Orientation similarity",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                path.join(self.results_dir, f"osm_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)

            self.ckey = plot.IPFColorKeyTSL(self.mp[f"mp_{ph}"].phase.point_group)

            # Refinemenet kwargs
            self.ref_kw = dict(detector=self.detector, energy=self.energy, compute=True)

            if self.refine:

                ### Refine xmaps
                self.xmap_ref = self.s2.refine_orientation(
                    xmap=self.xmaps[f"xmap_{ph}"],
                    master_pattern=self.mp[f"mp_{ph}"],
                    trust_region=[1, 1, 1],
                    **self.ref_kw,
                )
                self.xmaps_ref[f"xmap_ref_{ph}"] = self.xmap_ref

                io.save(
                    path.join(self.results_dir, f"di_ref_results_{ph}.ang"),
                    self.xmaps_ref[f"xmap_ref_{ph}"],
                )  # .ang

                fig = self.xmaps_ref[f"xmap_ref_{ph}"].plot(
                    self.ckey.orientation2color(
                        self.xmaps_ref[f"xmap_ref_{ph}"].orientations
                    ),
                    remove_padding=True,
                    return_figure=True,
                )

                fig.savefig(
                    path.join(self.results_dir, f"ipf_ref{ph}.png"),
                    **self.savefig_kwargs,
                )

                plt.close(fig)

            fig = self.xmaps[f"xmap_{ph}"].plot(
                self.ckey.orientation2color(self.xmaps[f"xmap_{ph}"].orientations),
                remove_padding=True,
                return_figure=True,
            )

            fig.savefig(
                path.join(self.results_dir, f"ipf_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)
            del self.sim_dict
            gc.collect()

        if len(self.phases) > 1:

            cm = [self.xmaps[f"xmap_{ph}"] for ph in self.phases]

            # Merge xmaps from indexed phases

            self.xmap_merged = kp.indexing.merge_crystal_maps(
                crystal_maps=cm,
                mean_n_best=1,
                scores_prop="scores",
                simulation_indices_prop="simulation_indices",
            )

            self.colors = ["lime", "r", "b", "yellow"]

            for i in range(len(self.phases)):
                self.xmap_merged.phases[i].color = self.colors[i]

            io.save(
                path.join(self.results_dir, "di_results_merged.h5"), self.xmap_merged
            )  # orix' HDF5
            io.save(
                path.join(self.results_dir, "di_results_merged.ang"), self.xmap_merged
            )  # .ang

            ### Plot and save the normalized cross correlation score

            fig = self.xmap_merged.plot(
                value=self.xmap_merged.scores[:, 0],
                colorbar=True,
                colorbar_label="Normalized cross correlation score",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                path.join(self.results_dir, "ncc_merged.png"), **self.savefig_kwargs
            )

            ### Phase map

            fig = self.xmap_merged.plot(remove_padding=True, return_figure=True)
            fig.savefig(
                path.join(self.results_dir, "phase_map.png"), **self.savefig_kwargs
            )

            # TODO: NCC histogram

            if self.refine:
                self.cm_ref = [self.xmaps_ref[f"xmap_ref_{ph}"] for ph in self.phases]

                ### Merge xmaps from indexed phases

                self.xmap_merged_ref = kp.indexing.merge_crystal_maps(
                    crystal_maps=self.cm_ref,
                )

                ### Set colors of phases and save merged xmaps to file

                for i in range(len(self.phases)):
                    self.xmap_merged_ref.phases[i].color = self.colors[i]

                io.save(
                    path.join(self.results_dir, "di_results_ref_merged.h5"),
                    self.xmap_merged_ref,
                )  # orix' HDF5
                io.save(
                    path.join(self.results_dir, "di_results_ref_merged.ang"),
                    self.xmap_merged_ref,
                )  # .ang

                ### Plot and save the normalized cross correlation score for merged map after refinement

                fig = self.xmap_merged_ref.plot(
                    value=self.xmap_merged_ref.scores,
                    colorbar=True,
                    colorbar_label="Normalized cross correlation score after refinement",
                    return_figure=True,
                    cmap="gray",
                )

                fig.savefig(
                    path.join(self.results_dir, "ncc_merged_ref.png"),
                    **self.savefig_kwargs,
                )

                ### Phase map

                fig = self.xmap_merged_ref.plot(remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, "phase_map_ref.png"),
                    **self.savefig_kwargs,
                )

        self.accept()
