import json
import warnings
from datetime import date
from os import mkdir, path
from typing import Optional, Sequence

import kikuchipy as kp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from diffpy.structure.structure import Structure
from kikuchipy.signals.ebsd import EBSD, LazyEBSD
from orix import io, plot
from orix.crystal_map import CrystalMap, Phase, PhaseList
from orix.vector import Vector3d
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMainWindow, QTableWidgetItem

from scripts.create_phase import NewPhaseDialog
from ui.ui_hi_setup import Ui_HISetupDialog
from utils import FileBrowser, SettingFile, sendToJobManager

# Ignore warnings to avoid crash with integrated console
warnings.filterwarnings("ignore")


class HiSetupDialog(QDialog):
    def __init__(self, parent: QMainWindow, pattern_path: str):
        super().__init__(parent)
        self.pattern_path = pattern_path
        self.pattern_name = path.basename(pattern_path)
        self.working_dir = path.dirname(pattern_path)

        self.ui = Ui_HISetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {self.pattern_path}")
        self.fileBrowserOF = FileBrowser(mode=FileBrowser.OpenFile, filter_name="*.h5")

        # Load pattern-file to get acquisition resolution
        try:
            s_prew: LazyEBSD = kp.load(self.pattern_path, lazy=True)
        except Exception as e:
            raise e
        self.binnings = self.getBinningShapes(s_prew)
        self.colors = [
            "blue",
            "orange",
            "lime",
            "yellow",
        ]
        self.mp_paths = {}
        self.phases = PhaseList()

        self.setupConnections()
        self.load_parameters()
        self.setAvailableButtons()

        # Matplotlib configuration
        mpl.use("agg")
        plt.rcParams.update({"font.size": 20})
        self.savefig_kwds = dict(pad_inches=0, bbox_inches="tight", dpi=150)

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_hough_indexing())
        self.ui.buttonBox.rejected.connect(lambda: self.reject())
        self.ui.pushButtonCreatePhase.clicked.connect(lambda: self.create_phase())
        self.ui.pushButtonLoadPhase.clicked.connect(
            lambda: self.load_master_pattern_phase()
        )
        self.ui.pushButtonRemovePhase.clicked.connect(lambda: self.remove_phase())
        self.ui.horizontalSliderRho.valueChanged.connect(
            lambda: self.ui.labelRho.setText(f"{self.ui.horizontalSliderRho.value()}%")
        )
        self.ui.comboBoxBinning.currentTextChanged.connect(
            lambda: self.ui.labelNewSignalShape.setText(
                f"{self.binnings[self.ui.comboBoxBinning.currentText()]} px"
            )
        )
        self.ui.comboBoxBinning.addItems(self.binnings.keys())

    def getOptions(self) -> dict:
        return {
            "binning": self.ui.comboBoxBinning.currentText(),
            "bands": self.ui.spinBoxBands.value(),
            "rho": self.ui.horizontalSliderRho.value(),
            "data": self.ui.checkBoxIndexData.isChecked(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "quality": [
                self.ui.checkBoxQuality.isChecked(),
                self.save_quality_metrics,
            ],
            "phase": [self.ui.checkBoxPhase.isChecked(), self.save_phase_map],
            "orientation": [
                self.ui.checkBoxOrientation.isChecked(),
                self.save_ipf_map,
            ],
            "ckey_direction": self.ui.lineEditColorKey.text(),
            "convention": self.ui.comboBoxConvention.currentText().lower(),
            "pc": (
                self.ui.patternCenterX.value(),
                self.ui.patternCenterY.value(),
                self.ui.patternCenterZ.value(),
            ),
        }

    def load_parameters(self):
        # Read current setting from project_settings.txt, advanced_settings.txt
        self.setting_file = SettingFile(
            path.join(self.working_dir, "project_settings.txt")
        )
        self.program_settings = SettingFile("advanced_settings.txt")
        try:
            lazy = eval(self.program_settings.read("Lazy Loading"))
        except:
            lazy = False
        self.ui.checkBoxLazy.setChecked(lazy)

        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = self.program_settings.read("Convention")
        pc_params = (
            self.ui.patternCenterX,
            self.ui.patternCenterY,
            self.ui.patternCenterZ,
        )
        try:
            pc = eval(self.setting_file.read("PC"))
            for i, param in enumerate(pc_params):
                param.setValue(float(pc[i]))
        except:
            for param in pc_params:
                param.setValue(0.5)
            # if self.s_cal.metadata.Acquisition_instrument.SEM.microscope == "ZEISS SUPRA55 VP":
            #     self.pc = [
            #         0.5605-0.0017*float(self.working_distance),
            #         1.2056-0.0225*float(self.working_distance),
            #         0.483,
            #     ]
            # else:
            #     self.pc = np.array([0.5000, 0.5000, 0.5000])

        self.ui.comboBoxConvention.setCurrentText(self.convention)
        try:
            self.colors = json.loads(self.program_settings.read("Colors"))
        except:
            pass
        try:
            if self.program_settings.read("Lazy Loading") == "False":
                self.ui.checkBoxLazy.setChecked(False)
        except:
            pass

        binningBox = self.ui.comboBoxBinning
        try:
            binning = json.loads(self.setting_file.read("Binning"))
            binningBox.setCurrentIndex(binningBox.findText(str(binning)))
        except:
            binningBox.setCurrentIndex(binningBox.findText("None"))

        i = 1
        while True:
            try:
                mp_path = self.setting_file.read(f"Master pattern {i}")
                self.load_master_pattern_phase(mp_path)
                i += 1
            except:
                break
        i = 1
        while True:
            try:
                params = eval(self.setting_file.read(f"Phase {i}"))
                structure = Structure()
                if params["structure"]:
                    structure.readStr(s=params["structure"], format="cif")
                self.add_phase(
                    name=params["name"],
                    space_group=params["space_group"],
                    structure=structure,
                    color=params["color"],
                )
                i += 1
            except Exception as e:
                break

    def save_parameters(self):
        self.setting_file.delete_all_entries()  # Clean up initial dictionary
        options = self.getOptions()
        master_idx = 1
        phase_idx = 1
        for _, phase in self.phases:
            if phase.name in self.mp_paths.keys():
                self.setting_file.write(
                    f"Master pattern {master_idx}", self.mp_paths[phase.name]
                )
                master_idx += 1
            else:
                sg = phase.space_group
                phase_settings = {
                    "name": phase.name,
                    "space_group": sg.number,
                    "color": phase.color,
                    "structure": phase.structure.writeStr(format="cif")
                    if phase.structure
                    else None,
                }
                self.setting_file.write(f"Phase {phase_idx}", phase_settings)
                phase_idx += 1
        self.setting_file.write("Convention", options["convention"].upper())
        self.setting_file.write("PC", options["pc"])
        # self.setting_file.write("X star", pc[0])
        # self.setting_file.write("Y star", pc[1])
        # self.setting_file.write("Z star", pc[2])
        self.setting_file.write("Binning", options["binning"])
        self.setting_file.save()

    def load_master_pattern_phase(self, mp_path: Optional[str] = None):
        if mp_path is not None:
            try:
                mp = kp.load(mp_path, lazy=True)
                if mp.phase.name == "":
                    mp.phase.name = path.dirname(mp_path).split("/").pop()
                self.phases.add(mp.phase)
                mp.phase.color = self.colors[len(self.phases.ids) - 1]
                self.mp_paths[mp.phase.name] = mp_path
            except Exception as e:
                print("Phase could not be loaded from master pattern", e)
            self.updatePhaseTable()
        elif self.fileBrowserOF.getFile():
            mp_paths = self.fileBrowserOF.getPaths()
            for mp_path in mp_paths:
                try:
                    mp = kp.load(mp_path, lazy=True)
                    if mp.phase.name == "":
                        mp.phase.name = path.dirname(mp_path).split("/").pop()
                    self.phases.add(mp.phase)
                    mp.phase.color = self.colors[len(self.phases.ids) - 1]
                    self.mp_paths[mp.phase.name] = mp_path
                except Exception as e:
                    print("Phase could not be loaded from master pattern", e)
            self.updatePhaseTable()

    def add_phase(
        self,
        name: str = "",
        space_group: int = None,
        structure: Structure = None,
        color: str = "",
    ):
        if not len(color):
            color = self.colors[len(self.phases.ids) - 1]
        try:
            if structure:
                self.phases.add(
                    Phase(
                        name,
                        space_group,
                        structure=structure,
                        color=color,
                    )
                )
            else:
                self.phases.add(Phase(name, space_group, color=color))
        except Exception as e:
            raise e
        self.updatePhaseTable()

    def create_phase(self):
        newPhaseDialog = NewPhaseDialog(self, self.colors[len(self.phases.ids)])
        if newPhaseDialog.exec() == QDialog.Accepted:
            self.phases.add(newPhaseDialog.get_phase(**newPhaseDialog.kwargs))
            self.updatePhaseTable()

    def updatePhaseTable(self):
        """
        NAME_COL = 0
        NUMBER_COL = 1
        ISS_COL = 2
        CRYSTAL_COL = 3
        COLOR_COL = 4
        """
        phasesTable = self.ui.tableWidgetPhase
        phasesTable.setRowCount(len(self.phases.ids))
        row = 0
        for _, phase in self.phases:
            sg = phase.space_group
            entries = [
                phase.name,
                sg.number,
                sg.short_name,
                sg.crystal_system,
                phase.color_rgb,
            ]
            for col, entry in enumerate(entries):
                item = QTableWidgetItem(str(entry))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                if entry == phase.color_rgb:
                    color = QColor.fromRgbF(*entry)
                    item = QTableWidgetItem(phase.color)
                    item.setBackground(color)
                phasesTable.setItem(row, col, item)
            row += 1
        self.setAvailableButtons()

    def remove_phase(self):
        """
        Removes selected rows of phases from tableWidgetPhase
        """
        phaseTable = self.ui.tableWidgetPhase
        indexes = phaseTable.selectionModel().selectedRows()
        indexes.sort(key=lambda qIndex: qIndex.row(), reverse=True)
        for modelIndex in indexes:
            phase_key = phaseTable.item(modelIndex.row(), 0).text()
            phaseTable.removeRow(modelIndex.row())
            self.phases.__delitem__(phase_key)
            if phase_key in self.mp_paths.keys():
                self.mp_paths.pop(phase_key)
        self.updatePhaseTable()

    def setAvailableButtons(self):
        display_message = False
        message = ""
        ok_flag = False
        phase_map_flag = False
        add_phase_flag = True
        n_phases = self.ui.tableWidgetPhase.rowCount()
        if n_phases != 0:
            ok_flag = True
            if n_phases == 2:
                phase_map_flag = True
                add_phase_flag = False
            if n_phases > 2:
                ok_flag = False
                add_phase_flag = False
                display_message = True
                message = "Current version of PyEBSDIndex supports maximum two phases (FCC, BCC)"
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(ok_flag)
        self.ui.checkBoxPhase.setEnabled(phase_map_flag)
        self.ui.checkBoxPhase.setChecked(phase_map_flag)
        self.ui.pushButtonCreatePhase.setEnabled(add_phase_flag)
        self.ui.pushButtonLoadPhase.setEnabled(add_phase_flag)
        self.ui.labelMessage.setVisible(display_message)
        self.ui.labelMessage.setText(message)

    def getBinningShapes(self, signal: LazyEBSD) -> dict:
        sig_shape = signal.axes_manager.signal_shape[::-1]
        self.ui.labelOriginalSignalShape.setText(f"{sig_shape} px")
        binnings: dict = {"None": sig_shape}
        for num in range(2, 17):
            if sig_shape[0] % num == 0 and sig_shape[1] % num == 0:
                binnings[f"{num}"] = (int(sig_shape[0] / num), int(sig_shape[1] / num))
        return binnings

    def hough_indexing(self, s):
        options = self.getOptions()
        self.rho_mask = (100.0 - options["rho"]) / 100.0
        self.number_bands = options["bands"]
        binning = eval(options["binning"])
        pc = options["pc"]
        convention = options["convention"]
        self.save_parameters()
        print(f"Loading {self.pattern_name} | lazy = {options['lazy']}")
        nav_shape = s.axes_manager.navigation_shape[::-1]
        step_sizes = (s.axes_manager["x"].scale, s.axes_manager["y"].scale)
        scan_unit = s.axes_manager[
            "x"
        ].units  # Assumes scan unit is the same for y and x
        if binning is None:
            binning = 1
        else:
            s = s.rebin(
                new_shape=s.axes_manager.navigation_shape + self.binnings[str(binning)]
            )
        sig_shape = s.axes_manager.signal_shape[::-1]  # (Rows, columns)
        det = kp.detectors.EBSDDetector(
            shape=sig_shape,
            binning=binning,
            sample_tilt=s.detector.sample_tilt,
            tilt=s.detector.tilt,
            pc=pc,
            convention=convention,
        )
        det.save(path.join(self.dir_out, "detector.txt"), convention)
        indexer = det.get_indexer(
            phase_list=self.phases, rhoMaskFrac=self.rho_mask, nBands=self.number_bands
        )
        print("------- Detector stats -------")
        print(f"Indexer Vendor: {indexer.vendor}")
        print(f"Sample tilt: {indexer.sampleTilt}")
        print(f"Camera elevation: {indexer.camElev}")
        print(f"Atomic arrangements: {indexer.phaselist}")
        print(f"Navigation shape: {nav_shape}")
        print(f"Signal shape: {sig_shape}")
        print(f"Steps: {step_sizes} {scan_unit}")
        xmap, data = s.hough_indexing(
            phase_list=self.phases, indexer=indexer, verbose=0, return_index_data=True
        )
        if options["data"]:
            index_data_path = path.join(self.dir_out, "index_data.npy")
            np.save(index_data_path, data)
            print(
                f"Saved index data array to {index_data_path}"
            )
        else:
            index_data_path = None
        name = ""
        for phase_id, phase in xmap.phases_in_data:
            if phase_id != -1:
                name += f"{phase.name}_"
        name = f"{name}xmap"
        io.save(path.join(self.dir_out, f"{name}.h5"), xmap)
        io.save(path.join(self.dir_out, f"{name}.ang"), xmap)
        print(f"Result was saved as {name}.ang and {name}.h5")
        for key in ["quality", "phase", "orientation"]:
            optionEnabled, optionExecute = options.get(key)
            if optionEnabled:
                try:
                    if key == "orientation":
                        optionExecute(xmap, eval(f"[{options['ckey_direction']}]"))
                    else:
                        optionExecute(xmap)
                except Exception as e:
                    print(f"Could not save {key}_map:\n{e}")
        print("Logging parameters used ...")
        log_hi_parameters(
            self.pattern_path,
            self.dir_out,
            s,
            xmap,
            self.mp_paths,
            convention=options["convention"],
            binning=binning,
            pattern_center=pc,
            index_data_path=index_data_path
        )
        print(f"Finished indexing {self.pattern_name}")

    def run_hough_indexing(self):
        for i in range(1, 100):
            try:
                self.dir_out = path.join(self.working_dir, "hi_results_" + str(i))
                mkdir(self.dir_out)
                break
            except FileExistsError:
                pass
        # Load s outside of thread to avoid leaked sesmaphores
        options = self.getOptions()
        try:
            signal = kp.load(self.pattern_path, lazy=options["lazy"])
        except Exception as e:
            raise e
        sendToJobManager(
            job_title=f"HI {self.pattern_name}",
            output_path=self.dir_out,
            listview=self.parentWidget().ui.jobList,
            func=self.hough_indexing,
            allow_cleanup=True,
            allow_logging=True,
            s=signal,
        )

    def save_quality_metrics(self, xmap):
        """
        Save plots of quality metrics
        """
        print("Saving quality metric for combined map ...")
        aspect_ratio = xmap.shape[1] / xmap.shape[0]
        figsize = (8 * aspect_ratio, 4.5 * aspect_ratio)
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=figsize)
        for a, to_plot in zip(ax.ravel(), ["pq", "cm", "fit", "nmatch"]):
            arr = xmap.get_map_data(to_plot)
            im = a.imshow(arr)
            fig.colorbar(im, ax=a, label=to_plot)
            a.axis("off")
            plt.imsave(
                path.join(self.dir_out, f"quality_metrics_{to_plot}.png"),
                arr,
            )
        fig.subplots_adjust(wspace=0, hspace=0.05)
        fig.savefig(
            path.join(self.dir_out, "quality_metrics_all.png"), **self.savefig_kwds
        )

    def save_phase_map(self, xmap):
        """
        Plot phase map
        """
        print("Saving phase map ...")
        # for i, ph in enumerate(self.phases):
        #     xmap.phases[ph].color = self.colors[i]
        fig = xmap.plot(return_figure=True, remove_padding=True)
        fig.savefig(path.join(self.dir_out, "phase_map.png"), **self.savefig_kwds)

    def save_ipf_map(
        self,
        xmap: CrystalMap,
        ckey_direction: Optional[Sequence] = [0, 0, 1],
        ckey_overlay: Optional[bool] = False,
    ):
        """
        Plot inverse pole figure map with orientation colour key

        Parameters
        ----------
        xmap : CrystalMap
            The crystal map which the orientations originates from
        ckey_direction: sequence
            3D vector used to determine the orientation color key
        ckey_overlay : bool
            Whether the colour orientation key is shown on top of the map or saved to seperate png, default is seperate
        """
        print("Saving inverse pole figure map ...")
        v_ipf = Vector3d(ckey_direction)
        sym = xmap.phases[0].point_group
        ckey = plot.IPFColorKeyTSL(sym, v_ipf)
        print(ckey)
        fig_ckey = ckey.plot(return_figure=True)
        rgb_direction = ckey.orientation2color(xmap.rotations)
        fig = xmap.plot(rgb_direction, remove_padding=True, return_figure=True)
        if ckey_overlay:
            ax_ckey = fig.add_axes(
                [0.77, 0.07, 0.2, 0.2], projection="ipf", symmetry=sym
            )
            ax_ckey.plot_ipf_color_key(show_title=False)
            ax_ckey.patch.set_facecolor("None")
        else:
            fig_ckey.savefig(
                path.join(self.dir_out, "orientation_colour_key.png"),
                **self.savefig_kwds,
            )
        fig.savefig(path.join(self.dir_out, "IPF.png"), **self.savefig_kwds)


# TODO Add more Hough related properties, better way to sort?
def log_hi_parameters(
    pattern_path: str,
    dir_out: str,
    signal: EBSD | LazyEBSD = None,
    xmap: CrystalMap = None,
    mp_paths: dict = None,
    pattern_center: np.ndarray = None,
    convention: str = "BRUKER",
    binning: int = 1,
    index_data_path = None
):
    """
    Assumes convention is BRUKER for pattern center if none is given
    """

    log = SettingFile(path.join(dir_out, "indexing_parameters.txt"))
    K = ["strs"]
    ### Time and date
    log.write("Date", f"{date.today()}\n")

    ### SEM parameters
    log.write("Microscope", signal.metadata.Acquisition_instrument.SEM.microscope)
    log.write(
        "Acceleration voltage",
        f"{signal.metadata.Acquisition_instrument.SEM.beam_energy} kV",
    )
    log.write("Pattern name", path.basename(pattern_path))
    log.write("Sample tilt", f"{signal.detector.sample_tilt} degrees")
    log.write("Camera tilt", f"{signal.detector.tilt} degrees")
    log.write(
        "Working distance",
        signal.metadata.Acquisition_instrument.SEM.working_distance,
    )
    log.write("Magnification", signal.metadata.Acquisition_instrument.SEM.magnification)
    log.write(
        "Navigation shape (rows, columns)",
        signal.axes_manager.navigation_shape[::-1],
    )
    binning = None if binning == 1 else binning
    log.write("Binning", binning)
    log.write("Signal shape (rows, columns)", signal.axes_manager.signal_shape[::-1])
    log.write("Step size", f"{signal.axes_manager[0].scale} um\n")

    ### HI parameteres

    log.write("kikuchipy version", kp.__version__)
    if index_data_path is not None:
        log.write("data_path", index_data_path)
    if mp_paths is not None:
        for i, mp_path in enumerate(mp_paths.values(), 1):
            log.write(f"Master pattern path {i}", mp_path)
    log.write("PC convention", f"{convention.upper()}")
    log.write("Pattern center (x*, y*, z*)", f"{pattern_center}")

    if len(xmap.phases.names) > 1:
        for i, ph in enumerate(xmap.phases.names, 1):
            phase_amount = xmap[f"{ph}"].size / xmap.size
            log.write(
                f"Phase {i}: {ph} [% ( # points)] ",
                f"{phase_amount:.1%}, ({xmap[f'{ph}'].size})",
            )

        # not_indexed_percent = xmap["not_indexed"].size / xmap.size
        # log.write(
        #     "Not indexed", f"{xmap['not_indexed'].size} ({not_indexed_percent:.1%})"
        # )

    log.save()
