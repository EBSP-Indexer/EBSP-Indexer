import warnings
from datetime import date
from os import mkdir, path

import kikuchipy as kp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from orix import io, plot, sampling
from orix.quaternion import Rotation
from PySide6.QtWidgets import QDialog

from ui.ui_di_setup import Ui_DiSetupDialog
from utils.filebrowser import FileBrowser
from utils.setting_file import SettingFile
from utils.worker import Worker

# TODO: from time import time


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

        # Dialog box ui setup
        self.ui = Ui_DiSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)

        self.load_pattern()
        self.setupInitialSettings()
        self.setupBinningShapes()

        self.setupConnections()

    # Initial settup functions

    def load_pattern(self):
        # Load pattern-file to get acquisition resolution
        try:
            self.s = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e

    def setupBinningShapes(self):
        self.sig_shape = self.s.axes_manager.signal_shape[::-1]
        self.bin_shapes = np.array([])
        for num in range(10, self.sig_shape[0]+1):
            if self.sig_shape[0] % num == 0:
                self.bin_shapes = np.append(self.bin_shapes, f"({num}, {num})")

        self.ui.comboBoxBinning.addItems(self.bin_shapes[::-1])

    def setupInitialSettings(self):

        # matplotlib settings
        mpl.use("agg")
        self.savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)

        # standard dictionary indexing kwargs
        self.di_kwargs = dict(metric="ncc", keep_n=20)

        # read current setting from project_settings.txt
        self.setting_file = SettingFile(
            path.join(self.working_dir, "project_settings.txt")
        )

        # PC convention, default is TSL

        try:
            self.convention = self.setting_file.read["Convention"]

        except:
            self.convention = "TSL"

        # TODO: add convention read from settings file
        self.ui.comboBoxConvention.setCurrentText(self.convention)

        # Update pattern center to be displayed in UI
        try:
            self.pc = np.array(
                [
                    float(self.setting_file.read("X star")),
                    float(self.setting_file.read("Y star")),
                    float(self.setting_file.read("Z star")),
                ]
            )
        except:
            self.pc = np.array([0.400, 0.400, 0.400])

        self.updatePCpatternCenter()

        # Paths for master patterns
        self.mpPaths = {}

        i = 1
        while True:
            try:
                mpPath = self.setting_file.read(f"Master pattern {i}")
                phase = mpPath.split("/").pop()
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
                i += 1
            except:
                break

    def update_pc_convention(self):

        self.convention = self.ui.comboBoxConvention.currentText()

        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterY.setValue(1 - self.pc[1])
        self.ui.patternCenterZ.setValue(self.pc[2])

        self.updatePCArrayFrompatternCenter()

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_dictionary_indexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

        self.ui.comboBoxConvention.currentTextChanged.connect(
            lambda: self.update_pc_convention()
        )

    # Pattern center

    def updatePCpatternCenter(self):
        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterY.setValue(self.pc[1])
        self.ui.patternCenterZ.setValue(self.pc[2])

    def updatePCArrayFrompatternCenter(self):
        self.pc[0] = self.ui.patternCenterX.value()
        self.pc[1] = self.ui.patternCenterY.value()
        self.pc[2] = self.ui.patternCenterZ.value()

    # Phases
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

    # Read options from interactive elements in dialog box
    def getOptions(self) -> dict:
        return {
            "Refine": self.ui.checkBoxRefine.isChecked(),
            "Lazy": self.ui.checkBoxLazy.isChecked(),
            "N_iter": int(self.ui.spinBoxNumIter.value()),
            "Disori": float(self.ui.doubleSpinBoxStepSize.value()),
            "Binning": self.ui.comboBoxBinning.currentText(),
            "Mask": [self.ui.checkBoxMask.isChecked(), lambda: self.signal_mask()],
            "IQ": [self.ui.checkBoxIQ.isChecked(), lambda: self.image_quality_map()],
            "ADP": [
                self.ui.checkBoxADP.isChecked(),
                lambda: self.average_dot_product(),
            ],
            "MI": [self.ui.checkBoxMI.isChecked(), lambda: self.mean_intensity_map()],
            "VBSE": [self.ui.checkBoxVBSE.isChecked(), lambda: self.vbse_image()],
        }

    # Call worker to start DI in separate thread
    def run_dictionary_indexing(self):
        # Pass the function to execute
        di_worker = Worker(self.dictionary_indexing)
        # Execute
        self.threadPool.start(di_worker)
        self.accept()

    def signal_mask(self):  # Add signal mask

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
        self.ref_kw["signal_mask"] = self.signal_mask

    # Pre-indexing operations

    def mean_intensity_map(self):
        mean_intensity = self.s.mean(axis=(2, 3))
        plt.imsave(
            path.join(self.results_dir, "mean_intensity.png"),
            mean_intensity.data,
            cmap="gray",
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

    def image_quality_map(self):
        # Image quality

        iq = self.s.get_image_quality()
        plt.imsave(path.join(self.results_dir, "iq.png"), iq, cmap="gray")

    def average_dot_product(self):
        # Average dot product map

        adp = self.s.get_average_neighbour_dot_product_map()
        plt.imsave(path.join(self.results_dir, "adp.png"), adp, cmap="gray")

    # Master pattern sample, TODO: add in dialog
    def master_pattern_sample(self, ph):
        ### Simulate one pattern to check the parameters. The master pattern sampling was implemented by Lars Lervik.

        self.sim = self.mp[f"{ph}"].get_patterns(
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

        fig.savefig(path.join(self.results_dir, f"pc_{ph}.png"), **self.savefig_kwargs)

        plt.close(fig)

    # Normal correlation
    def save_ncc_figure(self, ph):

        ### Inspect dictionary indexing results for phase
        for ph in self.phases:

            fig = self.xmaps[f"{ph}"].plot(
                value=self.xmaps[f"{ph}"].scores[:, 0],
                colorbar=True,
                colorbar_label="Normalized cross correlation score",
                return_figure=True,
                cmap="gray",
            )

            fig.savefig(
                path.join(self.results_dir, f"ncc_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)

    def save_orientation_similairty_map(self):

        for ph in self.phases:

            ### Calculate and save orientation similairty map

            osm = kp.indexing.orientation_similarity_map(self.xmaps[f"{ph}"])

            fig = self.xmaps[f"{ph}"].plot(
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

    def save_inverse_pole_figure(self, xmap_dict):

        for ph in self.phases:

            self.ckey = plot.IPFColorKeyTSL(self.mp[f"{ph}"].phase.point_group)

            fig = xmap_dict[f"{ph}"].plot(
                self.ckey.orientation2color(xmap_dict[f"{ph}"].orientations),
                remove_padding=True,
                return_figure=True,
            )

            fig.savefig(
                path.join(self.results_dir, f"ipf_{ph}_{xmap_dict['Type']}.png"),
                **self.savefig_kwargs,
            )

            plt.close(fig)

    def refine_orientations(self):
        self.ref_kw = dict(detector=self.detector, energy=self.energy, compute=True)

        for ph in self.phases:
            ### Refine xmaps
            self.xmaps_ref[f"{ph}"] = self.s2.refine_orientation(
                xmap=self.xmaps[f"{ph}"],
                master_pattern=self.mp[f"{ph}"],
                trust_region=[1, 1, 1],
                **self.ref_kw,
            )

            io.save(
                path.join(self.results_dir, f"di_ref_results_{ph}.ang"),
                self.xmaps_ref[f"{ph}"],
            )  # .ang

    def merge_refined_crystal_maps(self, xmap_dict):

        cm = [xmap_dict[f"{ph}"] for ph in self.phases]

        # Merge xmaps from indexed phases

        self.merged = kp.indexing.merge_crystal_maps(
            crystal_maps=cm,
        )

        self.colors = ["lime", "r", "b", "yellow"]

        for i, ph in enumerate(self.phases):
            self.merged.phases[ph].color = self.colors[i]

        io.save(
            path.join(self.results_dir, f"di_results_merged_{xmap_dict['Type']}.h5"),
            self.merged,
        )  # orix' HDF5
        io.save(
            path.join(self.results_dir, f"di_results_merged_{xmap_dict['Type']}.ang"),
            self.merged,
        )  # .ang

        ### Plot and save the normalized cross correlation score

        fig = self.merged.plot(
            value=self.merged.scores,
            colorbar=True,
            colorbar_label="Normalized cross correlation score",
            return_figure=True,
            cmap="gray",
        )

        fig.savefig(
            path.join(self.results_dir, f"ncc_merged_{xmap_dict['Type']}.png"),
            **self.savefig_kwargs,
        )

        ### Phase map

        fig = self.merged.plot(remove_padding=True, return_figure=True)
        fig.savefig(
            path.join(self.results_dir, f"phase_map_{xmap_dict['Type']}.png"),
            **self.savefig_kwargs,
        )

    def save_project_settings(self):
        self.setting_file.delete_all_entries()  # clean up initial dictionary

        ### Sample parameters
        for i, path in enumerate(self.mpPaths.values(), 1):
            self.setting_file.write(f"Master pattern {i}", path)

        self.setting_file.write("Convention", self.convention)

        self.updatePCArrayFrompatternCenter()
        self.setting_file.write("X star", f"{self.pc[0]}")
        self.setting_file.write("Y star", f"{self.pc[1]}")
        self.setting_file.write("Z star", f"{self.pc[2]}")

        self.setting_file.write("Binning", f"{self.new_signal_shape}")
        self.setting_file.write(
            "Angular step size [\u00B0]", f"{round(self.disori, 2)}"
        )

        self.setting_file.save()

    def save_di_settings(self):
        self.di_setting_file = SettingFile(path.join(self.results_dir, "di_parameters.txt"))

        ### Time and date
        self.di_setting_file.write("Date", f"{date.today()}\n")

        ### Sample info

        for i, mp_path in enumerate(self.mpPaths, 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        ### SEM parameters
        self.di_setting_file.write(
            "Microscope", self.s.metadata.Acquisition_instrument.SEM.microscope
        )
        self.di_setting_file.write("Acceleration voltage", f"{self.energy} kV")
        self.di_setting_file.write("Sample tilt", f"{self.sample_tilt} degrees")
        self.di_setting_file.write(
            "Working distance",
            self.s.metadata.Acquisition_instrument.SEM.working_distance,
        )
        self.di_setting_file.write(
            "Magnification", self.s.metadata.Acquisition_instrument.SEM.magnification
        )
        self.di_setting_file.write(
            "Navigation shape (rows, columns)",
            self.s.axes_manager.navigation_shape[::-1],
        )
        self.di_setting_file.write(
            "Signal shape (rows, columns)", self.s.axes_manager.signal_shape[::-1]
        )
        self.di_setting_file.write("Step size", f"{self.s.axes_manager[0].scale} um\n")

        ### DI parameteres

        self.di_setting_file.write("kikuchipy version", kp.__version__)
        self.di_setting_file.write("PC (x*, y*, z*)", f"{self.pc}")
        self.di_setting_file.write("PC convention", f"{self.convention}")
        for i, ph in enumerate(self.phases, 1):
            self.di_setting_file.write(f"Phase {i}", f"{ph}")
        self.di_setting_file.write(
            "Pattern resolution DI (Binning)", self.new_signal_shape
        )
        self.di_setting_file.write(
            "Angular step size [\u00B0]", f"{self.disori} degrees"
        )
        self.di_setting_file.write("Circular mask", self.ui.checkBoxMask.isChecked())
        self.di_setting_file.write(
            "Number of experimental patterns matched per iteration [None - all]",
            self.n_per_iteration,
        )
        self.di_setting_file.write("Refinement of orientations", self.refine)
        for i, mp_path in enumerate(self.mpPaths.values(), 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        self.di_setting_file.save()

    def dictionary_indexing(self):
        # Create folder for storing DI results in working directory
        i = 1
        while True:
            try:
                self.results_dir = path.join(self.working_dir, f"di_results_{i}")
                mkdir(self.results_dir)
                break
            except FileExistsError:
                print(
                    f"Directory {self.results_dir} exists, will try to create directory di_results_{i + 1}"
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

        # If n per iteration is 0
        self.n_per_iteration = None

        if self.options["N_iter"] != 0:
            self.n_per_iteration = self.options["N_iter"]

        self.di_kwargs["n_per_iteration"] = self.n_per_iteration

        # Read metadata from pattern file
        self.energy = self.s.metadata.Acquisition_instrument.SEM.beam_energy
        self.sample_tilt = self.s.detector.sample_tilt

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
            convention=self.convention,  # Default is Bruker, TODO: let user choose convention
        )

        # Define refinement kwargs

        self.ref_kw = dict(detector=self.detector, energy=self.energy, compute=True)

        ### Set up dictionary indexing parameters

        self.di_kwargs = dict(
            metric="ncc", keep_n=20, n_per_iteration=self.n_per_iteration
        )

        ### additional functions to be performed
        pre_processing_keys = ["Mask", "IQ", "VBSE", "MI", "ADP"]

        for key in pre_processing_keys:
            optionEnabled, optionExecute = self.options[key]
            if optionEnabled:
                optionExecute()

        # Master pattern dictionary
        self.mp = {}
        for ph in self.phases:
            self.file_mp = path.join(self.mpPaths[ph], f"{ph}_mc_mp_20kv.h5")
            self.mp[f"{ph}"] = kp.load(
                self.file_mp,
                energy=self.energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                projection="lambert",  # stereographic, lambert
                hemisphere="upper",  # upper, lower
            )

        # Xmaps dictionary for storing crystalmaps
        self.xmaps = {}
        self.xmaps["Type"] = "unrefined"
        # Refined xmaps dictionary for storing refined crystalmaps
        self.xmaps_ref = {}
        self.xmaps_ref["Type"] = "refined"

        self.save_project_settings()

        ### Dictionary indexing

        for ph in self.phases:

            ### Sample orientations

            self.rot = sampling.get_sample_fundamental(
                method="cubochoric",
                resolution=self.disori,
                point_group=self.mp[f"{ph}"].phase.point_group,
            )

            ### Generate dictionary

            self.sim_dict = self.mp[f"{ph}"].get_patterns(
                rotations=self.rot,
                detector=self.detector,
                energy=self.energy,
                compute=False,
            )

            self.xmaps[f"{ph}"] = self.s2.dictionary_indexing(
                dictionary=self.sim_dict, **self.di_kwargs
            )
            self.xmaps[f"{ph}"].scan_unit = "um"

            del self.sim_dict

        ## Single phase

        if len(self.phases) == 1:

            ### Save results from DI for phase, TODO: let user choose file type to be saved

            io.save(
                path.join(self.results_dir, f"di_results_{ph}.h5"),
                self.xmaps[f"{ph}"],
            )  # orix' HDF5
            io.save(
                path.join(self.results_dir, f"di_results_{ph}.ang"),
                self.xmaps[f"{ph}"],
            )  # .ang

            # Refine orientations
            if self.refine:

                self.refine_orientations()
                # Save IPF of refined xmaps
                self.save_inverse_pole_figure(self.xmaps_ref)

            else:
                # If xmaps are not refined, an unrefined IPF is saved
                self.save_inverse_pole_figure(self.xmaps)

                fig.savefig(
                    path.join(self.results_dir, f"ipf_ref_{ph}.png"),
                    **self.savefig_kwargs,
                )

            # NCC plot

            ncc_map = (
                self.xmaps[f"{ph}"].scores[:, 0].reshape(*self.xmaps[f"{ph}"].shape)
            )

            plt.imsave(
                path.join(self.results_dir, f"ncc_{ph}.png"), ncc_map, cmap="gray"
            )

        ## Multiple phase

        if len(self.phases) > 1:

            ### Save results from DI for phase, TODO: let user choose file type to be saved

            # io.save(
            #    path.join(self.results_dir, f"di_results_{ph}.h5"),
            #    self.xmaps[f"{ph}"],
            # )  # orix' HDF5
            # io.save(
            #    path.join(self.results_dir, f"di_results_{ph}.ang"),
            #    self.xmaps[f"{ph}"],
            # )  # .ang

            ## When dealing with multiple phases, the orientations are always refined
            self.refine_orientations()

            self.merge_refined_crystal_maps(self.xmaps_ref)

            self.ckey = plot.IPFColorKeyTSL(
                self.mp[f"{self.phases[0]}"].phase.point_group
            )

            fig = self.ckey.plot(return_figure=True)
            fig.savefig(
                path.join(self.results_dir, "orientation_color_key.png"),
                **self.savefig_kwargs,
            )

            rgb_all = np.zeros((self.merged.size, 3))
            for i, phase in self.merged.phases:
                if i != -1:
                    rgb_i = self.ckey.orientation2color(
                        self.merged[phase.name].orientations
                    )
                    rgb_all[self.merged.phase_id == i] = rgb_i

                fig = self.merged.plot(rgb_all, remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, "maps_ipfz.png"), **self.savefig_kwargs
                )

            plt.close(fig)
        self.save_di_settings()
