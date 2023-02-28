import warnings
import json
from datetime import date
from os import mkdir, path

import kikuchipy as kp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np
from orix import io, plot, sampling, crystal_map
from orix.quaternion import Rotation
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import QThreadPool

from ui.ui_di_setup import Ui_DiSetupDialog
from utils import SettingFile, FileBrowser, sendToJobManager

import gc

# TODO: from time import time


class DiSetupDialog(QDialog):
    """
    Setup dialog box for Dictionary indexing
    """

    def __init__(self, parent=None, pattern_path=None):
        super().__init__(parent)
        # pattern path
        self.pattern_path = pattern_path

        # pattern name
        self.pattern_name = path.basename(pattern_path)

        # working directory
        self.working_dir = path.dirname(self.pattern_path)

        # Dialog box ui setup
        self.ui = Ui_DiSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(
            mode=FileBrowser.OpenFile,
            filter_name="(*.h5)",
        )

        self.load_pattern()
        self.ui.sliderBinning.setInvertedAppearance(True)
        self.setupInitialSettings()
        self.checkConfirmState()
        self.setupBinningShapes()
        self.generate_rotation_lookup_dict()
        self.estimateSimulationSize()

        # temporary
        self.keep_unrefined_xmaps = False

        # Setup button connections
        self.setupConnections()

    # Initial settup functions

    def setupInitialSettings(self):

        # Matplotlib settings
        mpl.use("agg")
        self.savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)

        # standard dictionary indexing kwargs
        self.di_kwargs = dict(metric="ncc", keep_n=20)

        # read current setting from project_settings.txt, advanced_settings.txt
        self.setting_file = SettingFile(
            path.join(self.working_dir, "project_settings.txt")
        )
        self.program_settings = SettingFile("advanced_settings.txt")

        # PC convention, default is TSL
        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convention")

        self.ui.comboBoxConvention.setCurrentText(self.convention)

        if self.program_settings.read("Lazy Loading") == "False":
            self.ui.checkBoxLazy.setChecked(False)

        # Update pattern center to be displayed in UI
        try:
            self.pc = np.array(
                [
                    float(self.setting_file.read("X star")),
                    float(self.setting_file.read("Y star")),
                    float(self.setting_file.read("Z star")),
                ]
            )
            if self.convention == "TSL":
                # Ensure that PC is stored in BRUKER convention
                self.pc[1] = 1 - self.pc[1]
        except:
            self.pc = np.array([0.500, 0.200, 0.500])

        self.update_pc_spinbox()

        # Setup colors from program settings
        try:
            self.colors = json.loads(self.program_settings.read("Colors"))
        except:
            self.colors = [
                "lime",
                "r",
                "b",
                "yellow",
            ]

        # Paths for master patterns
        self.mpPaths = {}

        i = 1
        while True:
            try:
                mpPath = self.setting_file.read(f"Master pattern {i}")
                phase = path.dirname(mpPath).split("/").pop()
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)
                i += 1
            except:
                break

        self.getPhases()
        self.load_master_pattern()

        # Set max for N-iter
        x_len, y_len = self.s.axes_manager.navigation_shape
        self.ui.spinBoxNumIter.setMaximum(x_len * y_len)

    # Lookup table for sample rotations
    def generate_rotation_lookup_dict(self):
        self.sample_rotations = {}
        with open("sample_rotations.txt", "r") as f:
            for line in f:
                (key, value) = line.strip().split("\t")
                self.sample_rotations[f"{float(key):.2}"] = eval(value)

    def estimateSimulationSize(self):
        angle = float(self.ui.doubleSpinBoxStepSize.value())
        total_sim = 0
        if len(self.phases) > 0:
            for ph in self.phases:
                file_mp = path.join(self.mpPaths[ph])  # , f"{ph}_mc_mp_20kv.h5")
                mp = kp.load(
                    file_mp,
                    energy=20,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                    projection="lambert",  # stereographic, lambert
                    hemisphere="upper",  # upper, lower
                )

                total_sim += self.sample_rotations[f"{round(angle, 1)}"][
                    mp.phase.point_group.name
                ]

            self.ui.numSimPatterns.setText(f"{total_sim:,}")
        else:
            self.ui.numSimPatterns.setText("N/A")

    def load_pattern(self, lazy_load=True):
        try:
            self.s = kp.load(self.pattern_path, lazy=lazy_load)
            # Read metadata from pattern file
            self.energy = self.s.metadata.Acquisition_instrument.SEM.beam_energy
            self.sample_tilt = self.s.detector.sample_tilt
        except Exception as e:
            raise e

    def setupBinningShapes(self):
        self.ui.comboBoxBinning.clear()
        try:
            sig_shape = self.s.axes_manager.signal_shape[::-1]
            bin_shapes = np.array([])
            for num in range(10, sig_shape[0] + 1):
                if self.ui.checkBoxLazy.isChecked():
                    if sig_shape[0] % num == 0:
                        bin_shapes = np.append(bin_shapes, f"({num}, {num})")
                else:
                    bin_shapes = np.append(bin_shapes, f"({num}, {num})")

            self.ui.comboBoxBinning.addItems(bin_shapes[::-1])
            self.ui.sliderBinning.setMaximum(len(bin_shapes) - 1)

            # Define pixel-scale globally
            self.scale = self.s.axes_manager["x"].scale
        except Exception as e:
            raise e

    def updateBinningShape(self):
        self.ui.comboBoxBinning.setCurrentIndex(self.ui.sliderBinning.value())

    def set_save_fileformat(self):
        self.di_result_filetypes = [
            el.strip(".") for el in self.ui.comboBoxFiletype.currentText().split(", ")
        ]

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_dictionary_indexing())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

        self.ui.comboBoxConvention.currentTextChanged.connect(
            lambda: self.update_pc_convention()
        )
        self.ui.checkBoxLazy.stateChanged.connect(lambda: self.setNiterState())
        self.ui.checkBoxLazy.stateChanged.connect(lambda: self.setupBinningShapes())
        self.ui.doubleSpinBoxStepSize.valueChanged.connect(
            lambda: self.estimateSimulationSize()
        )

        self.ui.sliderBinning.valueChanged.connect(
            lambda: self.ui.comboBoxBinning.setCurrentIndex(
                self.ui.sliderBinning.value()
            )
        )
        self.ui.comboBoxBinning.currentIndexChanged.connect(
            lambda: self.ui.sliderBinning.setValue(
                self.ui.comboBoxBinning.currentIndex()
            )
        )

    def setNiterState(self):
        if self.ui.checkBoxLazy.isChecked():
            self.ui.spinBoxNumIter.setEnabled(False)
            self.ui.nIterLabel.setEnabled(False)
        else:
            self.ui.spinBoxNumIter.setEnabled(True)
            self.ui.nIterLabel.setEnabled(True)

    def checkConfirmState(self):
        if len(self.phases) == 0:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            self.ui.pushButtonRemovePhase.setEnabled(False)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.ui.pushButtonRemovePhase.setEnabled(True)

        if len(self.phases) == 1:
            self.ui.checkBoxPM.setEnabled(False)
        else:
            self.ui.checkBoxPM.setEnabled(True)

    ### Pattern center functions

    def update_pc_convention(self):
        self.convention = self.ui.comboBoxConvention.currentText()
        self.update_pc_spinbox()

    def update_pc_spinbox(self):
        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterZ.setValue(self.pc[2])
        if self.convention == "BRUKER":
            self.ui.patternCenterY.setValue(self.pc[1])
        elif self.convention == "TSL":
            self.ui.patternCenterY.setValue(1 - self.pc[1])

    def update_pc_array_from_spinbox(self):
        self.pc[0] = self.ui.patternCenterX.value()
        self.pc[2] = self.ui.patternCenterZ.value()
        if self.convention == "BRUKER":
            self.pc[1] = self.ui.patternCenterY.value()
        elif self.convention == "TSL":
            self.pc[1] = 1 - self.ui.patternCenterY.value()

    ### Phases
    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mpPath = self.fileBrowserOD.getPaths()[0]
            phase = path.dirname(mpPath).split("/").pop()
            self.fileBrowserOD.setDefaultDir(mpPath[0 : -len(phase) - 1])

            if phase not in self.mpPaths.keys():
                self.mpPaths[phase] = mpPath
                self.ui.listWidgetPhase.addItem(phase)

        self.getPhases()
        self.load_master_pattern()
        self.estimateSimulationSize()
        self.checkConfirmState()

    def removePhase(self):
        self.mpPaths.pop(str(self.ui.listWidgetPhase.currentItem().text()))
        self.ui.listWidgetPhase.takeItem(self.ui.listWidgetPhase.currentRow())

        self.getPhases()
        self.load_master_pattern()
        self.estimateSimulationSize()
        self.checkConfirmState()

    def getPhases(self):
        lw = self.ui.listWidgetPhase
        self.phases = [lw.item(x).text() for x in range(lw.count())]

    # Read options from interactive elements in dialog box
    def getOptions(self) -> dict:
        return {
            "refine": self.ui.checkBoxRefine.isChecked(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "n_iter": int(self.ui.spinBoxNumIter.value()),
            "angular_step_size": float(self.ui.doubleSpinBoxStepSize.value()),
            "binning": eval(self.ui.comboBoxBinning.currentText()),
            "mask": self.ui.checkBoxMask.isChecked(),
            "ncc": self.ui.checkBoxNCC.isChecked(),
            "osm": self.ui.checkBoxOSM.isChecked(),
            "ipf": self.ui.checkBoxIPF.isChecked(),
            "pm": self.ui.checkBoxPM.isChecked(),
        }

    # Call worker to start DI in separate thread
    def run_dictionary_indexing(self):
        # Create folder for storing DI results in working directory
        i = 1
        while True:
            try:
                self.results_dir = path.join(self.working_dir, f"di_results_{i}")
                mkdir(self.results_dir)
                break
            except FileExistsError:
                pass
            i += 1
        # Pass the function to execute
        sendToJobManager(
            job_title=f"DI {self.pattern_name}",
            output_path=self.results_dir,
            listview=self.parentWidget().ui.jobList,
            func=self.dictionary_indexing,
            allow_cleanup=True
        )

    # Master pattern dictionary
    def load_master_pattern(self):
        self.mp = {}
        for ph in self.phases:
            file_mp = path.join(self.mpPaths[ph])  # , f"{ph}_mc_mp_20kv.h5")

            self.mp[f"{ph}"] = kp.load(
                file_mp,
                energy=self.energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                projection="lambert",  # stereographic, lambert
                hemisphere="upper",  # upper, lower
            )

    # Signal mask
    def signal_mask(self, sig_shape):  # Add signal mask
        if self.options["mask"]:
            print("Applying signal mask")
            signal_mask = ~kp.filters.Window("circular", sig_shape).astype(bool)

            # Set signal mask for dictionary indexing
            self.di_kwargs["signal_mask"] = signal_mask

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

    # Normal cross correlation
    def save_ncc_figure(self, xmap_dict, xmap_type):
        for ph in self.phases:
            if xmap_type == "refined":
                ncc_map = xmap_dict[f"{ph}"].get_map_data("scores")
            if xmap_type == "unrefined":
                ncc_map = (
                    xmap_dict[f"{ph}"].scores[:, 0].reshape(*xmap_dict[f"{ph}"].shape)
                )

            ### Inspect dictionary indexing results for phase
            fig, ax = plt.subplots()
            ax.axis("off")
            ncc = ax.imshow(ncc_map, cmap="gray")
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(ncc, cax=cax, label="NCC")
            scalebar = ScaleBar(
                self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4
            )
            ax.add_artist(scalebar)
            fig.savefig(
                path.join(self.results_dir, f"ncc_{ph}_{xmap_type}.png"),
                **self.savefig_kwargs,
            )

            plt.close(fig)

    def save_orientation_similairty_map(self, xmap_dict):

        for ph in self.phases:

            ### Calculate and save orientation similairty map

            osm = kp.indexing.orientation_similarity_map(xmap_dict[f"{ph}"])
            ### Inspect dictionary indexing results for phase

            fig, ax = plt.subplots()
            ax.axis("off")
            osm_map = ax.imshow(osm, cmap="gray")
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(osm_map, cax=cax, label="Orientation similarity")
            scalebar = ScaleBar(
                self.scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4
            )
            ax.add_artist(scalebar)
            fig.savefig(
                path.join(self.results_dir, f"osm_{ph}.png"), **self.savefig_kwargs
            )

            plt.close(fig)

    def save_inverse_pole_figure(self, xmap_dict, xmap_type):

        for ph in self.phases:

            ckey = plot.IPFColorKeyTSL(self.mp[f"{ph}"].phase.point_group)

            fig = ckey.plot(return_figure=True)
            fig.savefig(
                path.join(self.results_dir, "orientation_color_key.png"),
                **self.savefig_kwargs,
            )

            fig = xmap_dict[f"{ph}"].plot(
                ckey.orientation2color(xmap_dict[f"{ph}"].orientations),
                remove_padding=True,
                return_figure=True,
            )

            fig.savefig(
                path.join(self.results_dir, f"ipf_{ph}_{xmap_type}.png"),
                **self.savefig_kwargs,
            )

            plt.close(fig)

    def refine_orientations(self, xmaps, detector, pattern):
        xmaps_ref = {}
        ref_kw = dict(detector=detector, energy=self.energy, compute=True)

        if self.options["mask"]:
            ref_kw["signal_mask"] = self.di_kwargs["signal_mask"]

        for ph in self.phases:
            ### Refine xmaps
            xmaps_ref[f"{ph}"] = pattern.refine_orientation(
                xmap=xmaps[f"{ph}"],
                master_pattern=self.mp[f"{ph}"],
                trust_region=[1, 1, 1],
                **ref_kw,
            )
            if self.keep_unrefined_xmaps:
                for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                    io.save(
                        path.join(self.results_dir, f"di_results_{ph}.{filetype}"),
                        xmaps[f"{ph}"],
                    )
            for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                io.save(
                    path.join(self.results_dir, f"di_ref_results_{ph}.{filetype}"),
                    xmaps_ref[f"{ph}"],
                )

        return xmaps_ref

    def merge_crystal_maps(self, xmap_dict, xmap_type):

        cm = [xmap_dict[f"{ph}"] for ph in self.phases]
        merge_kwargs = dict()

        if xmap_type == "unrefined":
            merge_kwargs = dict(
                mean_n_best=1, simulation_indices_prop="simulation_indices"
            )

        # Merge xmaps from indexed phases

        merged = kp.indexing.merge_crystal_maps(
            crystal_maps=cm, scores_prop="scores", **merge_kwargs
        )

        for i in range(len(self.phases)):
            merged.phases[i].color = self.colors[i]

        #        for i, ph in enumerate(self.phases):
        #            merged.phases[ph].color = self.colors[i]

        for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
            io.save(
                path.join(
                    self.results_dir,
                    f"di_results_merged_{xmap_type}.{filetype}",
                ),
                merged,
            )
        ncc_kwargs = dict(value=merged.scores)
        if xmap_type == "unrefined":
            ncc_kwargs = dict(value=merged.scores[:, 0])

        if self.options["ncc"]:
            ### Plot and save the normalized cross correlation score

            fig = merged.plot(
                colorbar=True,
                colorbar_label="NCC",
                return_figure=True,
                cmap="gray",
                remove_padding=True,
                **ncc_kwargs,
            )

            fig.savefig(
                path.join(self.results_dir, f"ncc_merged_{xmap_type}.png"),
                **self.savefig_kwargs,
            )

        return merged

    def save_project_settings(self):
        self.setting_file.delete_all_entries()  # clean up initial dictionary

        ### Sample parameters
        for i, mppath in enumerate(self.mpPaths.values(), 1):
            self.setting_file.write(f"Master pattern {i}", mppath)

        self.setting_file.write("Convention", self.convention)

        self.update_pc_array_from_spinbox()
        self.setting_file.write("X star", f"{self.pc[0]}")

        if self.convention == "BRUKER":
            self.setting_file.write("Y star", f"{self.pc[1]}")
        elif self.convention == "TSL":
            self.setting_file.write("Y star", f"{1-self.pc[1]}")

        self.setting_file.write("Z star", f"{self.pc[2]}")

        self.setting_file.write("Binning", f"({self.new_signal_shape})")
        self.setting_file.write(
            "Angular step size [\u00B0]", f"{round(self.angular_step_size, 2)}"
        )

        self.setting_file.save()

    def save_di_settings(self, xmap):
        self.di_setting_file = SettingFile(
            path.join(self.results_dir, "di_parameters.txt")
        )

        ### Time and date
        self.di_setting_file.write("Date", f"{date.today()}\n")

        ### Sample info

        for i, mp_path in enumerate(self.mpPaths, 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        ### SEM parameters
        self.di_setting_file.write(
            "Microscope", self.s.metadata.Acquisition_instrument.SEM.microscope
        )
        self.di_setting_file.write("Acceleration voltage [kV]", f"{self.energy}")
        self.di_setting_file.write("Sample tilt [degrees]", f"{self.sample_tilt}")
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

        pc_copy = self.pc.copy()
        if self.convention == "TSL":
            pc_copy[1] = 1 - pc_copy[1]

        self.di_setting_file.write("PC convention", f"{self.convention}")
        self.di_setting_file.write("Pattern center (x*, y*, z*)", f"{tuple(pc_copy)}")

        if len(self.phases) > 1:
            for i, ph in enumerate(self.phases, 1):
                phase_amount = xmap[f"{ph}"].size / xmap.size
                self.di_setting_file.write(
                    f"Phase {i}: {ph} [% ( # points)] ",
                    f"{phase_amount:.1%}, ({xmap[f'{ph}'].size})",
                )

            not_indexed_percent = xmap["not_indexed"].size / xmap.size

            self.di_setting_file.write(
                "Not indexed", f"{xmap['not_indexed'].size} ({not_indexed_percent:.1%})"
            )

        self.di_setting_file.write(
            "Pattern resolution DI (Binning)", self.new_signal_shape
        )
        self.di_setting_file.write(
            "Angular step size [\u00B0]", f"{self.angular_step_size:.2}"
        )
        self.di_setting_file.write("Circular mask", self.ui.checkBoxMask.isChecked())
        self.di_setting_file.write(
            "Number of experimental patterns matched per iteration [None - all]",
            self.n_per_iteration,
        )
        self.di_setting_file.write("Refinement of orientations", self.refine)
        for i, mp_path in enumerate(self.mpPaths.values(), 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        self.di_setting_file.write("Dataset path", self.pattern_path)
        
        self.di_setting_file.save()

    def dictionary_indexing(self):
        print("Initializing dictionary indexing")

        # get options from input
        self.options = self.getOptions()
        self.load_pattern(self.options["lazy"])
        self.update_pc_array_from_spinbox()
        self.set_save_fileformat()
        self.refine = self.options["refine"]
        self.new_signal_shape = self.options["binning"]
        self.angular_step_size = self.options["angular_step_size"]

        self.n_per_iteration = None
        if self.options["n_iter"] != 0:
            self.n_per_iteration = self.options["n_iter"]
        self.di_kwargs["n_per_iteration"] = self.n_per_iteration

        # Rebinning of signal
        print("Rebinning EBSD signals")
        nav_shape = self.s.axes_manager.navigation_shape
        s_binned = self.s.deepcopy().rebin(new_shape=nav_shape + self.new_signal_shape)
        #self.s_binned = self.s.rebin(new_shape=self.nav_shape + self.new_signal_shape)
        s_binned.rescale_intensity(dtype_out=np.uint8)

        # Define detector-sample geometry
        print("Defining detector")
        sig_shape = s_binned.axes_manager.signal_shape[::-1]
        detector = kp.detectors.EBSDDetector(
            shape=sig_shape,
            sample_tilt=self.sample_tilt,  # Degrees
            pc=self.pc,
            convention="BRUKER",  # Default is Bruker
        )
        detector.save(path.join(self.results_dir, "detector.txt"))

        # Apply signal mask
        self.signal_mask(sig_shape)

        # Define dictionaries for storing crystal maps
        xmaps = {}
        #xmaps["type"] = "unrefined"
        #self.xmaps_ref = {}
        #self.xmaps_ref["type"] = "refined"

        # Save current project settings to project_settings.txt
        self.save_project_settings()

        ### Dictionary indexing

        for ph in self.phases:
            self.mp[
                f"{ph}"
            ].phase.name = ph  # TO ensure that the master pattern is named correctly
            ### Sample orientations
            rot = sampling.get_sample_fundamental(
                method="cubochoric",
                resolution=self.angular_step_size,
                point_group=self.mp[f"{ph}"].phase.point_group,
            )
            print(f"Generating simulation dictionary from {ph} master pattern")
            ### Generate dictionary
            sim_dict = self.mp[f"{ph}"].get_patterns(
                rotations=rot,
                detector=detector,
                energy=self.energy,
                compute=False,
            )

            xmaps[f"{ph}"] = s_binned.dictionary_indexing(
                dictionary=sim_dict, **self.di_kwargs
            )
            xmaps[f"{ph}"].scan_unit = "um"
            print(ph)
            xmaps[f"{ph}"].phases[0].name = ph

            del sim_dict

            if not self.refine:
                for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                    io.save(
                        path.join(self.results_dir, f"di_results_{ph}.{filetype}"),
                        xmaps[f"{ph}"],
                    )

        if self.options["osm"]:
            print("Creating orientation similarity map")
            self.save_orientation_similairty_map(xmaps)

        if self.refine:
            xmaps_ref = self.refine_orientations(xmaps, detector, s_binned)

        if len(self.phases) == 1:
            print("Saving figures")
            if self.refine:
                # Save IPF of refined xmap
                if self.options["ipf"]:
                    self.save_inverse_pole_figure(xmaps_ref, "refined")
                    print("Saving inverse pole figure")

                if self.options["ncc"]:
                    print("Saving normalized cross-correlation map")
                    self.save_ncc_figure(xmaps_ref, "refined")

                self.save_di_settings(xmaps_ref)

            else:
                # If xmaps are not refined, an unrefined IPF is saved
                if self.options["ipf"]:
                    print("Saving inverse pole figure")
                    self.save_inverse_pole_figure(xmaps, "unrefined")

                # NCC map
                if self.options["ncc"]:
                    print("Saving normalized cross-correlation map")
                    self.save_ncc_figure(xmaps, "unrefined")

                # save DI settings to file
                self.save_di_settings(xmaps)

        ## Multiple phase

        if len(self.phases) > 1:
            print("Merging crystal maps")
            if self.refine:
                type = "refined"
                merged = self.merge_crystal_maps(xmaps_ref, type)
            else:
                type = "unrefined"
                merged = self.merge_crystal_maps(xmaps, type)

            if self.options["ipf"]:
                ckey = plot.IPFColorKeyTSL(
                    self.mp[f"{self.phases[0]}"].phase.point_group
                )

                fig = ckey.plot(return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, "orientation_color_key.png"),
                    **self.savefig_kwargs,
                )

                rgb_all = np.zeros((merged.size, 3))
                for i, phase in merged.phases:
                    if i != -1:
                        rgb_i = ckey.orientation2color(merged[phase.name].orientations)
                        rgb_all[merged.phase_id == i] = rgb_i

                fig = merged.plot(rgb_all, remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, f"ipf_z_{type}.png"),
                    **self.savefig_kwargs,
                )

                plt.close(fig)

            ### Phase map
            if self.options["pm"]:
                fig = merged.plot(remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, f"phase_map_{type}.png"),
                    **self.savefig_kwargs,
                )

            self.save_di_settings(merged)
        print(
            f"Dictionary indexing complete, results are stored in {path.basename(self.results_dir)}"
        )
