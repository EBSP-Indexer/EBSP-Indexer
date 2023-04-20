import warnings
import json
from datetime import date
from os import mkdir, path, getcwd

import kikuchipy as kp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np
from orix import io, plot, sampling, crystal_map
from orix.quaternion import Rotation
from orix.crystal_map import PhaseList
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem
from PySide6.QtCore import QThreadPool

from ui.ui_di_setup import Ui_DiSetupDialog
from utils import SettingFile, FileBrowser, sendToJobManager

import gc

SAMPLE_ROTATIONS = {
    "3.0": {"4/mmm": 90979, "m-3m": 30443},
    "2.9": {"4/mmm": 97627, "m-3m": 32363},
    "2.8": {"4/mmm": 110709, "m-3m": 36829},
    "2.7": {"4/mmm": 124885, "m-3m": 41625},
    "2.6": {"4/mmm": 132893, "m-3m": 44073},
    "2.5": {"4/mmm": 157151, "m-3m": 52607},
    "2.4": {"4/mmm": 175689, "m-3m": 58453},
    "2.2": {"4/mmm": 226787, "m-3m": 75539},
    "2.3": {"4/mmm": 195441, "m-3m": 65097},
    "2.1": {"4/mmm": 262101, "m-3m": 87529},
    "2.0": {"4/mmm": 301055, "m-3m": 100347},
    "1.9": {"4/mmm": 357801, "m-3m": 119077},
    "1.8": {"4/mmm": 421899, "m-3m": 141267},
    "1.7": {"4/mmm": 492855, "m-3m": 164179},
    "1.6": {"4/mmm": 592249, "m-3m": 197225},
    "1.5": {"4/mmm": 729573, "m-3m": 243129},
    "1.4": {"4/mmm": 913161, "m-3m": 304053},
    "1.3": {"4/mmm": 1157317, "m-3m": 385545},
    "1.2": {"4/mmm": 1481139, "m-3m": 494039},
    "1.1": {"4/mmm": 1906537, "m-3m": 635777},
    "1.0": {"4/mmm": 2571073, "m-3m": 857973},
}

mpl.use("agg")
savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)
di_kwargs = dict(metric="ncc", keep_n=20)


class DiSetupDialog(QDialog):
    """
    Setup dialog box for Dictionary indexing
    """

    def __init__(self, parent=None, pattern_path=None):
        super().__init__(parent)
        # pattern path
        self.pattern_path = pattern_path

        # pattern name
        self.pattern_name = path.basename(self.pattern_path)

        # working directory
        self.working_dir = path.dirname(self.pattern_path)

        # Dialog box ui setup
        self.ui = Ui_DiSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOD = FileBrowser(
            mode=FileBrowser.OpenFile,
            filter_name="*.h5",
        )

        self.setupInitialSettings()
        self.checkConfirmState()

        # Setup button connections
        self.setupConnections()

        # temporary
        self.keep_unrefined_xmaps = True

    # Initial setup functions

    def setupInitialSettings(self):
        try:
            ebsd_signal = kp.load(self.pattern_path, lazy=True)
            self.energy = ebsd_signal.metadata.Acquisition_instrument.SEM.beam_energy
            self.sample_tilt = ebsd_signal.detector.sample_tilt
            self.scale = ebsd_signal.axes_manager["x"].scale

        except Exception as e:
            raise e

        self.setupBinningShapes(ebsd_signal)

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
            self.pc = np.array(eval(self.setting_file.read("PC")))
        except:
            # try:
            #     self.pc = np.array(
            #         [
            #             float(self.setting_file.read("X star")),
            #             float(self.setting_file.read("Y star")),
            #             float(self.setting_file.read("Z star")),
            #         ]
            #     )
            # except:
            self.pc = np.array((0.500, 0.800, 0.500))

        self.ui.patternCenterX.setValue(self.pc[0])
        self.ui.patternCenterY.setValue(self.pc[1])
        self.ui.patternCenterZ.setValue(self.pc[2])

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

        # Paths for master patterns and pha
        self.mpPaths = {}
        self.phaseList = PhaseList()
        i = 1
        while True:
            try:
                mp_path = self.setting_file.read(f"Master pattern {i}")
                mp = kp.load(mp_path, lazy=True)
                if mp.phase.name == "":
                    mp.phase.name = path.dirname(mp_path).split("/").pop()
                phase = mp.phase.name
                self.mpPaths[phase] = mp_path
                self.phaseList.add(mp.phase)
                i += 1
            except:
                break

        self.updatePhaseTable()
        self.estimateSimulationSize()

        # TODO: Add N-iter for non-lazy indexing
        x_len, y_len = ebsd_signal.axes_manager.navigation_shape
        self.ui.spinBoxNumIter.setMaximum(x_len * y_len)
        self.ui.spinBoxNumIter.setMinimum(1)

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_dictionary_indexing())

        self.ui.pushButtonAddPhase.clicked.connect(lambda: self.addPhase())
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.removePhase())

        self.ui.checkBoxLazy.stateChanged.connect(lambda: self.setNiterState())

        self.ui.doubleSpinBoxStepSize.valueChanged.connect(
            lambda: self.estimateSimulationSize()
        )

        self.ui.comboBoxBinning.currentTextChanged.connect(
            lambda: self.ui.labelNewSignalShape.setText(
                f"{self.binnings[self.ui.comboBoxBinning.currentText()]}"
            )
        )

    def estimateSimulationSize(self):
        angle = float(self.ui.doubleSpinBoxStepSize.value())
        total_sim = 0
        if len(self.phaseList.ids) > 0:
            try:
                for i, ph in self.phaseList:
                    total_sim += SAMPLE_ROTATIONS[f"{round(angle, 1)}"][
                        ph.point_group.name
                    ]
                self.ui.numSimPatterns.setText(f"{total_sim:,}")
            except:
                self.ui.numSimPatterns.setText("N/A")
        else:
            self.ui.numSimPatterns.setText("N/A")

    def setupBinningShapes(self, ebsd_signal):
        self.ui.comboBoxBinning.clear()
        try:
            sig_shape = ebsd_signal.axes_manager.signal_shape[::-1]
            self.ui.comboBoxBinning.addItem("None")
            self.binnings = {"None": sig_shape}
            for i in range(2, 17):
                if sig_shape[0] % i == 0 and sig_shape[1] % i == 0:
                    self.binnings[f"{i}"] = (sig_shape[0] // i, sig_shape[1] // i)
                    self.ui.comboBoxBinning.addItem(str(i))
                    self.ui.labelOriginalSigShape.setText(f"{sig_shape}")
                    self.ui.labelNewSignalShape.setText(f"{sig_shape}")
        except Exception as e:
            raise e

    def setNiterState(self):
        if self.ui.checkBoxLazy.isChecked():
            self.ui.spinBoxNumIter.setEnabled(False)
            self.ui.nIterLabel.setEnabled(False)
        else:
            self.ui.spinBoxNumIter.setEnabled(True)
            self.ui.nIterLabel.setEnabled(True)

    def checkConfirmState(self):
        if len(self.phaseList.ids) == 0:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            self.ui.pushButtonRemovePhase.setEnabled(False)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.ui.pushButtonRemovePhase.setEnabled(True)

        if len(self.phaseList.ids) == 1:
            self.ui.checkBoxPM.setEnabled(False)
        else:
            self.ui.checkBoxPM.setEnabled(True)

    ### Phases
    def addPhase(self):
        if self.fileBrowserOD.getFile():
            mpPath = self.fileBrowserOD.getPaths()[0]

            self.fileBrowserOD.setDefaultDir(path.dirname(path.dirname(mpPath)))
            mp = kp.load(mpPath, lazy=True)
            if mp.phase.name == "":
                mp.phase.name = path.dirname(mpPath).split("/").pop()

            phase = mp.phase.name

            if phase not in self.mpPaths.keys():
                self.mpPaths[phase] = mpPath
                self.phaseList.add(mp.phase)

        self.updatePhaseTable()

        self.estimateSimulationSize()
        self.checkConfirmState()

    def removePhase(self):
        phaseTable = self.ui.tableWidgetPhase
        indexes = phaseTable.selectionModel().selectedRows()

        for index in indexes:
            phase_key = phaseTable.item(index.row(), 0).text()
            self.phaseList.__delitem__(phase_key)
            self.mpPaths.pop(f"{phase_key}")
            phaseTable.removeRow(index.row())

        self.updatePhaseTable()
        self.checkConfirmState()

    def updatePhaseTable(self):
        """
        NAME_COL = 0
        NUMBER_COL = 1
        ISS_COL = 2
        CRYSTAL_COL = 3
        COLOR_COL = 4
        """
        phaseTable = self.ui.tableWidgetPhase
        phaseTable.setRowCount(len(self.phaseList.ids))
        row = 0
        for i, ph in self.phaseList:
            try:
                ph.color = self.colors[row]
            except:
                pass
            sg = ph.space_group
            entries = [
                ph.name,
                sg.number,
                sg.short_name,
                sg.crystal_system,
                ph.color,
            ]
            for col, entry in enumerate(entries):
                item = QTableWidgetItem(str(entry))
                phaseTable.setItem(row, col, item)
            row += 1

    # Read options from interactive elements in dialog box
    def getOptions(self) -> dict:
        pc = (
            self.ui.patternCenterX.value(),
            self.ui.patternCenterY.value(),
            self.ui.patternCenterZ.value(),
        )
        return {
            "refine": self.ui.checkBoxRefine.isChecked(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "n_iter": int(self.ui.spinBoxNumIter.value()),
            "angular_step_size": float(self.ui.doubleSpinBoxStepSize.value()),
            "binning": self.ui.comboBoxBinning.currentText(),
            "mask": self.ui.checkBoxMask.isChecked(),
            "ncc": self.ui.checkBoxNCC.isChecked(),
            "osm": self.ui.checkBoxOSM.isChecked(),
            "ipf": self.ui.checkBoxIPF.isChecked(),
            "pm": self.ui.checkBoxPM.isChecked(),
            "pc": pc,
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

        # load pattern

        ebsd_pattern = kp.load(self.pattern_path, lazy=self.ui.checkBoxLazy.isChecked())

        # Pass the function to execute
        sendToJobManager(
            job_title=f"DI {self.pattern_name}",
            output_path=self.results_dir,
            listview=self.parentWidget().ui.jobList,
            func=self.dictionary_indexing,
            allow_cleanup=True,
            allow_logging=True,
            ebsd=ebsd_pattern,
        )

    # Master pattern dictionary
    def load_master_pattern(self):
        mp_dict = {}
        for i, ph in self.phaseList:
            file_mp = path.join(self.mpPaths[ph.name])

            mp_dict[f"{ph.name}"] = kp.load(
                file_mp,
                energy=self.energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
                projection="lambert",  # stereographic, lambert
                hemisphere="upper",  # upper, lower
                lazy=True,
            )

        return mp_dict

    # Signal mask
    def signal_mask(self, sig_shape):  # Add signal mask
        if self.options["mask"]:
            print("Applying signal mask")
            signal_mask = ~kp.filters.Window("circular", sig_shape).astype(bool)

            # Set signal mask for dictionary indexing
            di_kwargs["signal_mask"] = signal_mask

    # Normal cross correlation
    def save_ncc_figure(self, xmap_dict, xmap_type):
        for i, ph in self.phaseList:
            if xmap_type == "refined":
                ncc_map = xmap_dict[f"{ph.name}"].get_map_data("scores")
            if xmap_type == "unrefined":
                ncc_map = (
                    xmap_dict[f"{ph.name}"]
                    .scores[:, 0]
                    .reshape(*xmap_dict[f"{ph.name}"].shape)
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
                path.join(self.results_dir, f"ncc_{ph.name}_{xmap_type}.png"),
                **savefig_kwargs,
            )

            plt.close(fig)

    def save_orientation_similairty_map(self, xmap_dict):
        for i, ph in self.phaseList:
            ### Calculate and save orientation similairty map

            osm = kp.indexing.orientation_similarity_map(xmap_dict[f"{ph.name}"])
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
                path.join(self.results_dir, f"osm_{ph.name}.png"), **savefig_kwargs
            )

            plt.close(fig)

    def save_inverse_pole_figure(self, xmap_dict, xmap_type):
        for i, ph in self.phaseList:
            ckey = plot.IPFColorKeyTSL(self.mp[f"{ph.name}"].phase.point_group)

            fig = ckey.plot(return_figure=True)
            fig.savefig(
                path.join(self.results_dir, "orientation_color_key.png"),
                **savefig_kwargs,
            )

            fig = xmap_dict[f"{ph.name}"].plot(
                ckey.orientation2color(xmap_dict[f"{ph.name}"].orientations),
                remove_padding=True,
                return_figure=True,
            )

            fig.savefig(
                path.join(self.results_dir, f"ipf_{ph.name}_{xmap_type}.png"),
                **savefig_kwargs,
            )

            plt.close(fig)

    def refine_orientations(self, xmaps, detector, pattern):
        xmaps_ref = {}
        ref_kw = dict(detector=detector, energy=self.energy, compute=True)

        if self.options["mask"]:
            ref_kw["signal_mask"] = di_kwargs["signal_mask"]

        refined_dir = path.join(self.results_dir, "refined_crystal_maps")
        mkdir(refined_dir)

        if self.keep_unrefined_xmaps:
            unrefined_dir = path.join(self.results_dir, "unrefined_crystal_maps")
            mkdir(unrefined_dir)

        for i, ph in self.phaseList:
            ### Refine xmaps
            xmaps_ref[f"{ph.name}"] = pattern.refine_orientation(
                xmap=xmaps[f"{ph.name}"],
                master_pattern=self.mp[f"{ph.name}"],
                method="ln_neldermead",
                trust_region=[1, 1, 1],
                **ref_kw,
            )
            if self.keep_unrefined_xmaps:
                try:
                    for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                        io.save(
                            path.join(unrefined_dir, f"{ph.name}.{filetype}"),
                            xmaps[f"{ph.name}"],
                        )
                except Exception as e:
                    raise e
            try:
                for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                    io.save(
                        path.join(refined_dir, f"{ph.name}_refined.{filetype}"),
                        xmaps_ref[f"{ph.name}"],
                    )
            except Exception as e:
                raise e

        return xmaps_ref

    def merge_crystal_maps(self, xmap_dict, xmap_type):
        cm = [xmap_dict[f"{ph.name}"] for i, ph in self.phaseList]
        merge_kwargs = dict()

        if xmap_type == "unrefined":
            merge_kwargs = dict(
                mean_n_best=1, simulation_indices_prop="simulation_indices"
            )

        # Merge xmaps from indexed phases

        merged = kp.indexing.merge_crystal_maps(
            crystal_maps=cm, scores_prop="scores", **merge_kwargs
        )

        for i, ph in merged.phases:
            ph.color = self.colors[i]

        for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
            io.save(
                path.join(
                    self.results_dir,
                    f"xmap_di_{xmap_type}.{filetype}",
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
                **savefig_kwargs,
            )

        return merged

    def dictionary_indexing(self, ebsd):
        print("Initializing dictionary indexing ..")
        # load phases
        self.mp = self.load_master_pattern()

        # get options from input
        self.options = self.getOptions()

        self.pc = self.options["pc"]

        self.di_result_filetypes = [
            el.strip(".") for el in self.ui.comboBoxFiletype.currentText().split(", ")
        ]
        self.refine = self.options["refine"]
        self.binning = self.options["binning"]
        self.angular_step_size = self.options["angular_step_size"]

        self.convention = self.ui.comboBoxConvention.currentText().upper()
        # Rebinning of signal
        original_nav_shape = ebsd.axes_manager.signal_shape[::-1]
        if self.binning != "None":
            print("Rebinning EBSD signal...")
            print(f"Binning: {self.binning}")
            ebsd.downsample(eval(self.binning), inplace=True, show_progressbar=False)

        # Define detector-sample geometry
        print("Defining detector...")
        sig_shape = ebsd.axes_manager.signal_shape[::-1]
        detector = kp.detectors.EBSDDetector(
            shape=sig_shape,
            sample_tilt=self.sample_tilt,  # Degrees
            pc=self.pc,
            convention=self.convention,  # Default is Bruker
        )
        detector.save(path.join(self.results_dir, "detector.txt"))

        # Apply signal mask
        self.signal_mask(sig_shape)

        # Define dictionaries for storing crystal maps
        xmaps = {}

        # Save current project settings to project_settings.txt
        self.save_project_settings()

        if not self.refine:
            try:
                unrefined_dir = path.join(self.results_dir, "unrefined_crystal_maps")
                mkdir(unrefined_dir)
            except Exception as e:
                raise e

        ### Dictionary indexing

        for i, ph in self.phaseList:
            ### Sample orientations
            rot = sampling.get_sample_fundamental(
                method="cubochoric",
                resolution=self.angular_step_size,
                point_group=ph.point_group,
            )
            print(f"Generating simulation dictionary from {ph.name} master pattern ...")
            ### Generate dictionary
            sim_dict = self.mp[f"{ph.name}"].get_patterns(
                rotations=rot,
                detector=detector,
                energy=self.energy,
                compute=False,
            )

            if self.ui.spinBoxNumIter.isEnabled():
                n_iteration = self.options["n_iter"]
                di_kwargs["n_per_iteration"] = (
                    sim_dict.axes_manager.navigation_size // n_iteration
                )

            xmaps[f"{ph.name}"] = ebsd.dictionary_indexing(
                dictionary=sim_dict, **di_kwargs
            )
            xmaps[f"{ph.name}"].scan_unit = "um"
            xmaps[f"{ph.name}"].phases[0].name = ph.name

            del sim_dict

            if not self.refine:
                try:
                    for filetype in self.di_result_filetypes:  # [".ang", ".h5"]
                        io.save(
                            path.join(unrefined_dir, f"{ph.name}.{filetype}"),
                            xmaps[f"{ph.name}"],
                        )
                except Exception as e:
                    raise e

        if self.options["osm"]:
            print("Creating orientation similarity map")
            self.save_orientation_similairty_map(xmaps)

        if self.refine:
            xmaps_ref = self.refine_orientations(xmaps, detector, ebsd)

        if len(self.phaseList.ids) == 1:
            print("Saving figures")
            if self.refine:
                # Save IPF of refined xmap
                if self.options["ipf"]:
                    self.save_inverse_pole_figure(xmaps_ref, "refined")
                    print("Saving inverse pole figure")

                if self.options["ncc"]:
                    print("Saving normalized cross-correlation map")
                    self.save_ncc_figure(xmaps_ref, "refined")

                self.save_di_settings(xmaps_ref, ebsd, original_nav_shape)

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
                self.save_di_settings(xmaps, ebsd, original_nav_shape)

        ## Multiple phase

        if len(self.phaseList.ids) > 1:
            print("Merging crystal maps")
            if self.refine:
                type = "refined"
                merged = self.merge_crystal_maps(xmaps_ref, type)
            else:
                type = "unrefined"
                merged = self.merge_crystal_maps(xmaps, type)

            if self.options["ipf"]:
                phase_id = merged.phases.ids[0]
                ckey = plot.IPFColorKeyTSL(merged.phases[phase_id].point_group)

                fig = ckey.plot(return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, "orientation_color_key.png"),
                    **savefig_kwargs,
                )

                rgb_all = np.zeros((merged.size, 3))
                for i, phase in merged.phases:
                    if i != -1:
                        rgb_i = ckey.orientation2color(merged[phase.name].orientations)
                        rgb_all[merged.phase_id == i] = rgb_i

                fig = merged.plot(rgb_all, remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, f"ipf_z_{type}.png"),
                    **savefig_kwargs,
                )

                plt.close(fig)

            ### Phase map
            if self.options["pm"]:
                fig = merged.plot(remove_padding=True, return_figure=True)
                fig.savefig(
                    path.join(self.results_dir, f"phase_map_{type}.png"),
                    **savefig_kwargs,
                )

            self.save_di_settings(merged, ebsd, original_nav_shape)
        print(
            f"Dictionary indexing complete, results stored in {path.basename(self.results_dir)}"
        )

    def save_project_settings(self):
        self.setting_file.delete_all_entries()  # clean up initial dictionary

        ### Sample parameters
        for i, mppath in enumerate(self.mpPaths.values(), 1):
            self.setting_file.write(f"Master pattern {i}", mppath)

        self.setting_file.write("Convention", self.convention)

        self.setting_file.write("PC", f"{self.pc}")
        # self.setting_file.write("X star", f"{self.pc[0]}")
        # self.setting_file.write("Y star", f"{self.pc[1]}")
        # self.setting_file.write("Z star", f"{self.pc[2]}")

        self.setting_file.write("Binning", f"({self.binning})")
        self.setting_file.write(
            "Angular step size [\u00B0]", f"{round(self.angular_step_size, 2)}"
        )

        self.setting_file.save()

    def save_di_settings(self, xmap, ebsd, original_nav_shape):
        self.di_setting_file = SettingFile(
            path.join(self.results_dir, "indexing_parameters.txt")
        )

        ### Time and date
        self.di_setting_file.write("Date", f"{date.today()}\n")

        ### Sample info

        for i, mp_path in enumerate(self.mpPaths, 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        ### SEM parameters
        self.di_setting_file.write(
            "Microscope", ebsd.metadata.Acquisition_instrument.SEM.microscope
        )
        self.di_setting_file.write("Acceleration voltage [kV]", f"{self.energy}")
        self.di_setting_file.write("Sample tilt [degrees]", f"{self.sample_tilt}")
        self.di_setting_file.write(
            "Working distance",
            ebsd.metadata.Acquisition_instrument.SEM.working_distance,
        )
        self.di_setting_file.write(
            "Magnification", ebsd.metadata.Acquisition_instrument.SEM.magnification
        )
        self.di_setting_file.write(
            "Navigation shape (rows, columns)",
            original_nav_shape,
        )
        self.di_setting_file.write(
            "Signal shape (rows, columns)", ebsd.axes_manager.signal_shape[::-1]
        )
        self.di_setting_file.write("Step size", f"{ebsd.axes_manager[0].scale} um\n")

        ### DI parameteres

        self.di_setting_file.write("kikuchipy version", kp.__version__)
        self.di_setting_file.write("PC convention", f"{self.convention}")
        self.di_setting_file.write("Pattern center (x*, y*, z*)", f"{tuple(self.pc)}")

        if len(self.phaseList.ids) > 1:
            for i, ph in xmap.phases:
                if i != -1:
                    phase_amount = xmap[ph.name].size / xmap.size
                    self.di_setting_file.write(
                        f"Phase {i}: {ph.name} [% ( # points)] ",
                        f"{phase_amount:.1%}, ({xmap[ph.name].size})",
                    )
                else:
                    not_indexed_percent = xmap[ph.name].size / xmap.size

                    self.di_setting_file.write(
                        "Not indexed", f"{xmap[-1].size} ({not_indexed_percent:.1%})"
                    )

        self.di_setting_file.write(
            "Pattern resolution DI (Binning)", self.binnings[f"{self.binning}"]
        )
        self.di_setting_file.write(
            "Angular step size [\u00B0]", f"{self.angular_step_size:.2}"
        )
        self.di_setting_file.write("Circular mask", self.ui.checkBoxMask.isChecked())
        n_iter = self.options["n_iter"]
        if self.options["n_iter"] == 1:
            n_iter = None
        self.di_setting_file.write(
            "Slicing of simulation dicitonary [None - all]",
            n_iter,
        )
        self.di_setting_file.write("Refinement of orientations", self.refine)
        for i, mp_path in enumerate(self.mpPaths.values(), 1):
            self.di_setting_file.write(f"Master pattern path {i}", mp_path)

        self.di_setting_file.write("Pattern name", path.basename(self.pattern_path))

        self.di_setting_file.save()