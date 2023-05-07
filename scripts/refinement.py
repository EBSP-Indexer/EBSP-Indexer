import json
import warnings
from os import path
from typing import Optional, Sequence

import kikuchipy as kp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from kikuchipy.indexing._merge_crystal_maps import merge_crystal_maps
from kikuchipy.signals.ebsd import EBSD, LazyEBSD
from kikuchipy.signals.ebsd_master_pattern import LazyEBSDMasterPattern
from kikuchipy.signals.util._crystal_map import _equal_phase
from orix import io, plot
from orix.crystal_map import CrystalMap, PhaseList
from orix.vector import Vector3d
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from scripts.pc_from_wd import pc_from_wd
from ui.ui_refine_setup import Ui_RefineSetupDialog
from utils import (
    FileBrowser,
    SettingFile,
    get_setting_file_bottom_top,
    sendToJobManager,
)

# Ignore warnings to avoid crash with integrated console
warnings.filterwarnings("ignore")


class RefineSetupDialog(QDialog):
    def __init__(self, parent: QMainWindow, file_path: Optional[str] = ""):
        super().__init__(parent)

        parameter_file, self.xmap_dir = get_setting_file_bottom_top(
            file_path, "indexing_parameters.txt", return_dir_path=True
        )
        self.setting_file, self.working_dir = get_setting_file_bottom_top(
            file_path, "project_settings.txt", return_dir_path=True
        )
        self.program_settings = SettingFile("advanced_settings.txt")
        self.pattern_path = ""
        self.xmap_path = ""
        self.s_energy = 20  # kV
        self.data_path = ""
        self.xmaps: dict[str, CrystalMap] = {}
        self.master_patterns: dict[str, LazyEBSDMasterPattern] = {}
        self.ui = Ui_RefineSetupDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{self.windowTitle()} - {file_path}")
        self.fileBrowserOF = FileBrowser(
            mode=FileBrowser.OpenFile,
            dirpath=path.dirname(file_path),
            filter_name="Hierarchical Data Format (*.h5);",
        )
        # Try loading file as EBSD or LazyEBSD
        try:
            try:
                s_preview = kp.load(file_path, lazy=True)
                if isinstance(s_preview, (EBSD, LazyEBSD)):
                    self.pattern_path = file_path
                    self.s_energy = (
                        s_preview.metadata.Acquisition_instrument.SEM.beam_energy
                    )
                else:
                    raise ValueError("File selected does not contain a siganl")
            except Exception as e:
                raise e
        # Try loading file as CrystalMap
        except:
            try:
                xmap_prew = io.load(file_path)
                if isinstance(xmap_prew, (CrystalMap)):
                    self.load_crystal_maps(file_path)
                    if parameter_file is None:
                        raise Exception(
                            "No indexing parameters associated with selected crystal map"
                        )
                    if self.setting_file is None:
                        raise Exception(
                            "Could not determine project settings associated with selected crystal map"
                        )
                    self.pattern_path = path.join(
                        self.working_dir, parameter_file.read("Pattern name")
                    )
                    # Try loading signal from path found in parameter file
                    try:
                        s_preview = kp.load(self.pattern_path)
                        self.s_energy = (
                            s_preview.metadata.Acquisition_instrument.SEM.beam_energy
                        )
                    except Exception as e:
                        print("Could not load patterns associated with crystal map")
                        raise e
                else:
                    raise ValueError("File does not contain a Crystal Map")
            except Exception as e:
                raise e
        self.ui.labelNavigationShape.setText(
            f"Navigation shape: {str(s_preview.axes_manager.navigation_shape[::-1])}"
        )
        self.binnings = self.getBinningShapes(s_preview)
        self.colors = [
            "blue",
            "orange",
            "lime",
            "yellow",
        ]

        self.setupConnections()
        self.load_parameters(s_preview)

        # Matplotlib configuration
        mpl.use("agg")
        plt.rcParams.update({"font.size": 20})
        self.savefig_kwds = dict(pad_inches=0, bbox_inches="tight", dpi=150)

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.run_refinement())
        self.ui.pushButtonLoadMP.clicked.connect(lambda: self.load_master_pattern())
        self.ui.pushButtonRemoveMP.clicked.connect(lambda: self.remove_master_pattern())
        self.ui.pushButtonLoadXmap.clicked.connect(
            lambda: self.load_crystal_maps(force_clear=True)
        )
        self.ui.pushButtonAddXmap.clicked.connect(lambda: self.load_crystal_maps())
        self.ui.pushButtonRemoveXmap.clicked.connect(lambda: self.remove_crystal_maps())
        self.ui.comboBoxBinning.currentTextChanged.connect(
            lambda: self.ui.labelNewSignalShape.setText(
                f"{self.binnings[self.ui.comboBoxBinning.currentText()]} px"
            )
        )
        self.ui.comboBoxBinning.addItems(self.binnings.keys())
        self.ui.labelSignalPath.setText(self.pattern_path)
        self.ui.radioButtonMultipleXmap.toggled.connect(
            lambda: self.setAvailableButtons()
        )
        self.ui.radioButtonMultipleXmap.toggled.connect(
            lambda: self.clear_crystal_maps()
        )
        self.ui.radioButtonMultipleXmap.toggled.connect(
            lambda: self.updateCrystalMapTable()
        )

    def getOptions(self) -> dict:
        return {
            "mask": self.ui.checkBoxMask.isChecked(),
            "binning": self.ui.comboBoxBinning.currentText(),
            "lazy": self.ui.checkBoxLazy.isChecked(),
            "ncc": [
                self.ui.checkBoxNCC.isChecked(),
                self.save_ncc_map,
            ],
            "phase": [self.ui.checkBoxPhase.isChecked(), self.save_phase_map],
            "orientation": [
                self.ui.checkBoxOrientation.isChecked(),
                self.save_ipf_map,
            ],
            "ckey_direction": self.ui.lineEditColorKey.text(),
            "data": self.ui.checkBoxData.isChecked(),
            "multiple": self.ui.radioButtonMultipleXmap.isChecked(),
            "single": self.ui.radioButtonSingleXmap.isChecked(),
            "convention": self.ui.comboBoxConvention.currentText().lower(),
            "pc": (
                self.ui.patternCenterX.value(),
                self.ui.patternCenterY.value(),
                self.ui.patternCenterZ.value(),
            ),
            "method": self.ui.comboBoxMethod.currentText(),
            "ref_kwargs": self.ui.lineEditRefKwargs.text(),
        }

    def load_parameters(self, signal: LazyEBSD):
        """
        Read current settings from project_settings.txt, advanced_settings.txt
        """
        try:
            convention = self.setting_file.read("Convention")
        except:
            convention = self.program_settings.read("Convention")
        self.ui.comboBoxConvention.setCurrentText(convention)
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
            try:
                microscope = signal.metadata.Acquisition_instrument.SEM.microscope
                working_distance = (
                    signal.metadata.Acquisition_instrument.SEM.working_distance
                )
                pc: list[float] = pc_from_wd(microscope, working_distance, convention)
                for i, param in enumerate(pc_params):
                    param.setValue(pc[i])
            except:
                for value, param in zip((0.5, 0.8, 0.5), pc_params):
                    param.setValue(value)
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
                self.load_master_pattern(mp_path)
                i += 1
            except:
                break

    # TODO Save parameters to project_settings

    def available_index_data(path: str) -> str:
        """
        Returns the path of the available index data.
        If no path is found, retuns an empty string.
        """
        parameter_file: SettingFile = get_setting_file_bottom_top(
            path, "indexing_parameters.txt"
        )
        if parameter_file is not None:
            try:
                return parameter_file.read("data_path")
            except:
                pass
        return ""

    def clear_crystal_maps(self, force_clear: Optional[bool] = False):
        if force_clear or (
            len(self.xmaps) > 1 and self.ui.radioButtonSingleXmap.isChecked()
        ):
            self.xmaps: dict[str, CrystalMap] = {}
            self.xmap_path = "No crystal map loaded"
            self.data_path = ""
            self.updateCrystalMapTable()

    def load_crystal_maps(self, xmap_path: Optional[str] = None, force_clear=False):
        if xmap_path is not None:
            try:
                xmap_name = path.basename(xmap_path)
                self.xmaps[f"{xmap_name}"] = io.load(xmap_path)
                self.xmap_path = xmap_path
                self.xmap_dir = path.dirname(self.xmap_path)
                self.data_path = RefineSetupDialog.available_index_data(xmap_path)
            except Exception as e:
                raise e
            self.updateCrystalMapTable()
            return
        if self.ui.radioButtonMultipleXmap.isChecked():
            self.fileBrowserOF.setMode(FileBrowser.OpenFiles)
        else:
            self.fileBrowserOF.setMode(FileBrowser.OpenFile)
        if self.fileBrowserOF.getFile():
            self.clear_crystal_maps(force_clear)
            for temp_path in self.fileBrowserOF.getPaths():
                try:
                    xmap_name = path.basename(temp_path)
                    self.xmaps[f"{xmap_name}"] = io.load(temp_path)
                    self.xmap_path = temp_path
                    self.xmap_dir = path.dirname(self.xmap_path)
                    self.data_path = RefineSetupDialog.available_index_data(
                        self.xmap_path
                    )
                except Exception as e:
                    raise e
            self.updateCrystalMapTable()
            return

    def remove_crystal_maps(self):
        """
        Removes selected rows from tableWidgetXmap
        """
        xmapTable = self.ui.tableWidgetXmap
        indexes = xmapTable.selectionModel().selectedRows()
        indexes.sort(key=lambda qIndex: qIndex.row(), reverse=True)
        for modelIndex in indexes:
            xmap_name = xmapTable.item(modelIndex.row(), 0).text()
            xmapTable.removeRow(modelIndex.row())
            self.xmaps.pop(xmap_name)
            for row in range(xmapTable.rowCount()):
                if xmapTable.itemAt(row, 0).text() == xmap_name:
                    xmapTable.removeRow(row)
        self.updateCrystalMapTable()

    def load_master_pattern(self, mp_path: Optional[str] = None):
        if mp_path is not None:
            try:
                mp_preview: LazyEBSDMasterPattern = kp.load(
                    mp_path,
                    energy=self.s_energy,
                    projection="lambert",
                    hemisphere="upper",
                    lazy=True,
                )
                load_kwargs = {"hemisphere": "both"}
                if mp_preview.phase.point_group.contains_inversion:
                    load_kwargs["hemisphere"] = "upper"
                mp: LazyEBSDMasterPattern = kp.load(
                    mp_path,
                    energy=self.s_energy,
                    projection="lambert",
                    lazy=True,
                    **load_kwargs,
                )
                if mp.phase.name == "":
                    mp.phase.name = path.dirname(mp_path).split("/").pop()
                mp.phase.color = self.colors[len(self.master_patterns.keys())]
                self.master_patterns[mp.phase.name] = mp
            except Exception as e:
                raise e
            self.updateMasterPatternTable()
            return
        self.fileBrowserOF.setMode(FileBrowser.OpenFiles)
        if self.fileBrowserOF.getFile():
            mp_paths = self.fileBrowserOF.getPaths()
            for mp_path in mp_paths:
                try:
                    mp_preview: LazyEBSDMasterPattern = kp.load(
                        mp_path,
                        energy=self.s_energy,
                        projection="lambert",
                        hemisphere="upper",
                        lazy=True,
                    )
                    load_kwargs = {"hemisphere": "both"}
                    if mp_preview.phase.point_group.contains_inversion:
                        load_kwargs["hemisphere"] = "upper"
                    mp: LazyEBSDMasterPattern = kp.load(
                        mp_path,
                        energy=self.s_energy,
                        projection="lambert",
                        lazy=True,
                        **load_kwargs,
                    )
                    if mp.phase.name == "":
                        mp.phase.name = path.dirname(mp_path).split("/").pop()
                    mp.phase.color = self.colors[len(self.master_patterns.keys())]
                    self.master_patterns[mp.phase.name] = mp
                except Exception as e:
                    raise e
            self.updateMasterPatternTable()
            return

    def updateMasterPatternTable(self):
        """
        NAME_COL = 0
        NUMBER_COL = 1
        ISS_COL = 2
        CRYSTAL_COL = 3
        COLOR_COL = 4
        """
        tableMP = self.ui.tableWidgetMP
        tableMP.setRowCount(len(self.master_patterns.keys()))
        row = 0
        for mp in self.master_patterns.values():
            sg = mp.phase.space_group
            entries = [
                mp.phase.name,
                sg.number,
                sg.short_name,
                sg.crystal_system,
                mp.phase.color_rgb,
            ]
            for col, entry in enumerate(entries):
                item = QTableWidgetItem(str(entry))
                if entry == mp.phase.color_rgb:
                    color = QColor.fromRgbF(*entry)
                    item = QTableWidgetItem(mp.phase.color)
                    item.setBackground(color)
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                tableMP.setItem(row, col, item)
            row += 1
        self.setAvailableButtons()

    def updateCrystalMapTable(self):
        if self.ui.radioButtonMultipleXmap.isChecked():
            self.ui.labelXmapPath.setText("Multiple crystal maps")
        else:
            self.ui.labelXmapPath.setText(
                self.xmap_path if len(self.xmap_path) else "No crystal map loaded"
            )
        xmapTable = self.ui.tableWidgetXmap
        row_count = 0
        for xmap in self.xmaps.values():
            row_count += len(xmap.phases.ids)
        xmapTable.setRowCount(row_count)
        row = 0
        for xmap_name, xmap in self.xmaps.items():
            for _, phase in xmap.phases:
                phase_amount = xmap[f"{phase.name}"].size / xmap.size
                entries = [
                    xmap_name,
                    phase.name,
                    f"{xmap[f'{phase.name}'].size} ({phase_amount:.1%})",
                ]
                for col, entry in enumerate(entries):
                    item = QTableWidgetItem(str(entry))
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                    xmapTable.setItem(row, col, item)
                row += 1
        if len(self.data_path) and self.ui.radioButtonSingleXmap.isChecked():
            self.ui.labelIndexDataStatus.setStyleSheet("QLabel { color : green; }")
            self.ui.labelIndexDataStatus.setText("Index data available")
        else:
            self.ui.labelIndexDataStatus.setStyleSheet("QLabel { color : red; }")
            self.ui.labelIndexDataStatus.setText("No available index data")
        self.setAvailableButtons()

    def remove_master_pattern(self):
        """
        Removes selected rows of master patterns from tableWidgetMP
        """
        tableMP = self.ui.tableWidgetMP
        indexes = tableMP.selectionModel().selectedRows()
        indexes.sort(key=lambda qIndex: qIndex.row(), reverse=True)
        for model_index in indexes:
            mp_phase_name = tableMP.item(model_index.row(), 0).text()
            tableMP.removeRow(model_index.row())
            if mp_phase_name in self.master_patterns.keys():
                self.master_patterns.pop(mp_phase_name)
        self.setAvailableButtons()

    def setAvailableButtons(self):
        ok_flag = False
        phase_map_flag = False
        add_phase_flag = True
        index_data = False
        count_mp = self.ui.tableWidgetMP.rowCount()
        count_phase = 0
        for xmap in self.xmaps.values():
            for ph_id, _ in xmap.phases_in_data:
                if ph_id != -1:
                    count_phase += 1
        if count_mp and count_mp <= count_phase:
            ok_flag = True
            if count_mp > 1:
                phase_map_flag = True
        if self.ui.radioButtonSingleXmap.isChecked() and len(self.data_path):
            index_data = True
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(ok_flag)
        self.ui.checkBoxPhase.setEnabled(phase_map_flag)
        self.ui.checkBoxPhase.setChecked(phase_map_flag)
        self.ui.pushButtonLoadMP.setEnabled(add_phase_flag)
        self.ui.checkBoxData.setEnabled(index_data)
        self.ui.checkBoxData.setChecked(index_data)

    def getBinningShapes(self, signal: LazyEBSD) -> dict:
        sig_shape = signal.axes_manager.signal_shape[::-1]
        self.ui.labelOriginalSignalShape.setText(f"{sig_shape} px")
        binnings: dict = {"None": sig_shape}
        for num in range(2, 17):
            if sig_shape[0] % num == 0 and sig_shape[1] % num == 0:
                binnings[f"{num}"] = (int(sig_shape[0] / num), int(sig_shape[1] / num))
        return binnings

    def refine_orientations(
        self,
        s: EBSD,
        xmaps: dict[str, CrystalMap],
        master_patterns: dict[str, LazyEBSDMasterPattern],
        options: dict,
    ):
        binning = eval(options["binning"])
        pc = options["pc"]
        convention = options["convention"]
        mask = options["mask"]
        method = options["method"]
        if len(options["ref_kwargs"]):
            ref_kwargs = eval(options["ref_kwargs"])
        else:
            ref_kwargs = {}
        energy: int = s.metadata.Acquisition_instrument.SEM.beam_energy
        nav_shape = s.axes_manager.navigation_shape[::-1]
        step_sizes = (s.axes_manager["x"].scale, s.axes_manager["y"].scale)
        scan_unit = s.axes_manager["x"].units  # Assumes same for y and x
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
        if mask:
            signal_mask = ~kp.filters.Window("circular", det.shape).astype(bool)
        else:
            signal_mask = None
        print("------- Detector stats -------")
        print(f"Navigation shape: {nav_shape}")
        print(f"Steps: {step_sizes} {scan_unit}")
        print(f"Signal shape: {sig_shape}")
        print(f"Circular mask: {mask}")

        ref_xmaps: list[CrystalMap] = []
        ref_xmaps_navs: list[np.ndarray] = []
        for mp_phase_name, mp in master_patterns.items():
            print(f"\nRefining with Master Pattern: {mp.phase.name}")
            for xmap in xmaps.values():
                for phase_id, phase in xmap.phases_in_data:
                    if phase.name == mp_phase_name:
                        # TODO Switch from -2 to -1 when kikuchipy supports merging not_indexed (0.8.5)
                        nav_mask_phase = ~np.logical_or(
                            xmap.phase_id == phase_id,
                            xmap.phase_id == -2,
                        )
                        nav_mask_phase = nav_mask_phase.reshape(xmap.shape)
                        refined_xmap = s.refine_orientation(
                            xmap=xmap,
                            detector=det,
                            master_pattern=mp,
                            energy=energy,
                            navigation_mask=nav_mask_phase,
                            signal_mask=signal_mask,
                            trust_region=[1, 1, 1],
                            method=method,
                            method_kwargs=ref_kwargs,
                            compute=True,
                        )
                        ref_xmaps.append(refined_xmap)
                        ref_xmaps_navs.append(nav_mask_phase)
        if ref_xmaps[0].rotations_per_point > 1:
            merge_kwargs = dict(simulation_indices_prop="simulation_indices")
        else:
            merge_kwargs = dict()
        if len(ref_xmaps) == 1:
            refined_xmap = ref_xmaps[0]
        else:
            refined_xmap = merge_crystal_maps(
                ref_xmaps,
                scores_prop="scores",
                navigation_masks=ref_xmaps_navs,
                **merge_kwargs,
            )
        name = ""
        for phase_id, phase in refined_xmap.phases_in_data:
            if phase_id != -1:
                name += f"{phase.name}_"
        name = f"{name}refined_xmap"
        io.save(path.join(self.output_dir, f"{name}.h5"), refined_xmap, overwrite=True)
        io.save(path.join(self.output_dir, f"{name}.ang"), refined_xmap, overwrite=True)
        print(f"Result was saved as {name}.ang and {name}.h5")

        for key in ["phase", "orientation", "ncc"]:
            optionEnabled, optionExecute = options.get(key)
            if optionEnabled:
                try:
                    if key == "orientation":
                        optionExecute(
                            refined_xmap, eval(f"[{options['ckey_direction']}]")
                        )
                    else:
                        optionExecute(refined_xmap)
                except Exception as e:
                    print(f"Could not save {key}_map:\n{e}")
        print(f"Finished refining orientations")

    def run_refinement(self):
        fileBrowserOF = FileBrowser(
            mode=FileBrowser.OpenDirectory,
            dirpath=path.dirname(self.xmap_dir),
            filter_name="Hierarchical Data Format (*.h5);",
            caption="Choose Output Directory for Refined Results"
        )
        options = self.getOptions()
        try:
            s: EBSD = kp.load(self.pattern_path, lazy=options["lazy"])
            nav_shape = s.axes_manager.navigation_shape[::-1]
            step_sizes = (s.axes_manager["x"].scale, s.axes_manager["y"].scale)
            scan_unit = s.axes_manager["x"].units  # Assumes y and x are same
        except Exception as e:
            raise e
        if options["data"] and path.exists(self.data_path):
            phases = PhaseList()
            for phase_id, phase in list(self.xmaps.values())[0].phases_in_data:
                if phase_id != -1:
                    phases.add(phase)
            phases.add_not_indexed()
            data = np.load(self.data_path)
            try:
                self.xmaps: dict[str, CrystalMap] = {}
                for phase_id, phase in phases:
                    if phase_id != -1:
                        xmap: CrystalMap = kp.indexing.xmap_from_hough_indexing_data(
                            data=data,
                            phase_list=phases,
                            data_index=phase_id,
                            navigation_shape=nav_shape,
                            step_sizes=step_sizes,
                            scan_unit=scan_unit,
                        )
                        self.xmaps[f"data_{phase.name}"] = xmap
            except Exception as e:
                raise e
        for mp_phase_name, mp in self.master_patterns.items():
            for xmap in self.xmaps.values():
                if mp_phase_name in xmap.phases_in_data.names:
                    xmap_phase = xmap.phases_in_data[mp_phase_name]
                    equal_phases, are_different = _equal_phase(mp.phase, xmap_phase)
                    if not equal_phases:
                        if self.promptOverridePhase(
                            f"Master pattern phase '{mp.phase.name}' and phase of points to refine "
                            f"in crystal map '{xmap_phase.name}' must be the same, but have "
                            f"different {are_different}."
                        ):
                            xmap_phase.name = mp.phase.name
                            xmap_phase.space_group = mp.phase.space_group
                            xmap_phase.color = mp.phase.color
                            xmap_phase.structure = mp.phase.structure
                            continue
                        else:
                            return
        job_title = "Refine orientations of "
        for xmap in self.xmaps.values():
            for ph_id, ph in xmap.phases_in_data:
                if ph_id != -1:
                    job_title += f"{ph.name}, "
        if not fileBrowserOF.getFile():
            return
        self.output_dir = fileBrowserOF.getPaths()[0]
        sendToJobManager(
            job_title=job_title[0:-2],
            output_path=self.output_dir,
            listview=self.parentWidget().ui.jobList,
            func=self.refine_orientations,
            allow_cleanup=False,
            allow_logging=False,
            s=s,
            xmaps=self.xmaps,
            master_patterns=self.master_patterns,
            options=options,
        )

    def promptOverridePhase(self, message) -> bool:
        reply = QMessageBox(self).information(
            self,
            "Warning Phase conflict",
            f"{message}\nOverride phase from crystal map with phase from master pattern'?",
            QMessageBox.Yes | QMessageBox.Abort,
            QMessageBox.Yes,
        )
        if reply == QMessageBox.Yes:
            return True
        else:
            return False

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
                path.join(self.output_dir, f"quality_metrics_{to_plot}.png"),
                arr,
            )
        fig.subplots_adjust(wspace=0, hspace=0.05)
        fig.savefig(
            path.join(self.output_dir, "quality_metrics_all.png"), **self.savefig_kwds
        )

    def save_phase_map(self, xmap):
        """
        Plot phase map
        """
        print("Saving phase map ...")
        fig = xmap.plot(return_figure=True, remove_padding=True)
        fig.savefig(
            path.join(self.output_dir, "phase_map_refined.png"), **self.savefig_kwds
        )

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
        sym = xmap.phases_in_data[0].point_group
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
                path.join(self.output_dir, "orientation_color_key.png"),
                **self.savefig_kwds,
            )
        fig.savefig(path.join(self.output_dir, "IPF_refined.png"), **self.savefig_kwds)

    def save_ncc_map(self, xmap: CrystalMap):
        if len(xmap.phases.ids) == 1:
            fig = xmap.plot(
                "scores",
                return_figure=True,
                colorbar=True,
                colorbar_label="NCC",
                cmap="gray",
                remove_padding=True,
            )
        else:
            fig = xmap.plot(
                value=xmap.merged_scores[:, 0],
                colorbar=True,
                colorbar_label="NCC",
                return_figure=True,
                cmap="gray",
                remove_padding=True,
            )
        fig.savefig(
            path.join(self.output_dir, "NCC_refined.png"),
            **self.savefig_kwds,
        )


# TODO Log method
