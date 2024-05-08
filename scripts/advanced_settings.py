import json
import platform
from os.path import exists

import matplotlib.colors as mplcolors
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QMessageBox
from tabulate import tabulate

from scripts.color_picker import ColorPicker
from scripts.pc_from_wd import wdCalibration
from ui.ui_advanced_settings import Ui_AdvancedSettings
from utils import FileBrowser, SettingFile, Setting


class AdvancedSettingsDialog(QDialog):
    settingsChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdvancedSettings()
        self.ui.setupUi(self)
        self.loadSettings()
        self.setupConnections()
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)

        self.ui.colorTreeWidget.setColumnWidth(0, 200)

    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.settingsChanged.emit())
        self.ui.buttonBox.accepted.connect(lambda: self.saveSettings())

        # File Explorer
        self.ui.addFileTypeButton.clicked.connect(lambda: self.addFileType())
        self.ui.removeFileTypeButton.clicked.connect(lambda: self.removeFileType())
        self.ui.resetFileTypeButton.clicked.connect(lambda: self.resetFileType())
        self.ui.directoryBox.clicked.connect(lambda: self.toggleDefaultDirectory())
        self.ui.browseDirectoryButton.clicked.connect(lambda: self.browseDirectory())

        # Pre-Processing
        self.ui.brukerButton.clicked.connect(lambda: self.setBruker())
        self.ui.tslButton.clicked.connect(lambda: self.setTSL())
        self.ui.savePcsBox.clicked.connect(lambda: self.setIndividualPCData())
        self.ui.pushButtonAddNewMicroscope.clicked.connect(lambda: self.addNewMicroscope())
        self.ui.pushButtonRemoveMicroscope.clicked.connect(lambda: self.removeMicroscope())
        self.ui.listWidgetMicroscopes.itemDoubleClicked.connect(lambda: self.display_calibration_params())

        # Indexing
        self.ui.lazyLoadingBox.clicked.connect(lambda: self.setLazy())
        self.ui.checkBoxSaveIPFMap.clicked.connect(lambda: self.setSaveIPF())
        self.ui.checkBoxSavePhaseMap.clicked.connect(lambda: self.setSavePhase())
        self.ui.checkBoxSaveNumpy.clicked.connect(lambda: self.setSaveNumpy())
        self.ui.checkBoxRefine.clicked.connect(lambda: self.setRefine())
        self.ui.colorTreeWidget.doubleClicked.connect(lambda: self.colorPicker())

        # Apperance
        if platform.system().lower() == "darwin":
            self.ui.lightRadioButton.setDisabled(True)
            self.ui.darkRadioButton.setDisabled(True)

    def addFileType(self):
        if self.ui.fileTypeLineEdit.text():
            item = "." + str(self.ui.fileTypeLineEdit.text()).strip(".")
            if item not in self.file_types:
                self.ui.fileTypeList.addItem(item)
                self.file_types.append(item)
        self.ui.fileTypeLineEdit.clear()

    def removeFileType(self):
        try:
            self.file_types.remove(self.ui.fileTypeList.currentItem().text())
            self.ui.fileTypeList.takeItem(self.ui.fileTypeList.currentRow())
        except:
            pass

    def resetFileType(self):
        self.ui.fileTypeList.clear()
        self.file_types = [".h5", ".dat", ".ang", ".jpg", ".png", ".txt"]
        for f in self.file_types:
            self.ui.fileTypeList.addItem(f)

    def toggleDefaultDirectory(self):
        if self.ui.directoryBox.isChecked():
            self.ui.directoryEdit.setEnabled(True)
            self.ui.browseDirectoryButton.setEnabled(True)
            if self.ui.directoryEdit.text() == "":
                self.browseDirectory()
        else:
            self.ui.directoryEdit.setDisabled(True)
            self.ui.browseDirectoryButton.setDisabled(True)
            self.directory = False

    def browseDirectory(self):
        if self.fileBrowserOD.getFile():
            self.directory = self.fileBrowserOD.getPaths()[0]
            self.ui.directoryEdit.setText(self.directory)

    def setBruker(self):
        self.convention = "BRUKER"

    def setTSL(self):
        self.convention = "TSL"

    def setIndividualPCData(self):
        self.individual_PC_data = self.ui.savePcsBox.isChecked()

    def setLazy(self):
        self.lazy = self.ui.lazyLoadingBox.isChecked()

    def setSaveIPF(self):
        self.saveIPF = self.ui.checkBoxSaveIPFMap.isChecked()

    def setSavePhase(self):
        self.savePhase = self.ui.checkBoxSavePhaseMap.isChecked()

    def setSaveNumpy(self):
        self.saveNumpy = self.ui.checkBoxSaveNumpy.isChecked()

    def setRefine(self):
        self.refine = self.ui.checkBoxRefine.isChecked()

    def addNewMicroscope(self):
        wdDialog = wdCalibration(parent=self)
        wdDialog.exec()
        try:
            self.setting_file.write(wdDialog.microscope_name, wdDialog.pc_curve)
            if wdDialog.microscope_name not in self.microscopes:
                self.ui.listWidgetMicroscopes.addItem(wdDialog.microscope_name)
                self.microscopes.append(wdDialog.microscope_name)
        except:
            pass

    def removeMicroscope(self):
        try:
            microscope = self.ui.listWidgetMicroscopes.currentItem().text()
            self.microscopes.pop(self.microscopes.index(microscope))
            self.ui.listWidgetMicroscopes.takeItem(self.ui.listWidgetMicroscopes.currentRow())
            self.setting_file.remove(microscope)
        except AttributeError:
            pass
        except Exception as e:
            raise e
        if len(self.microscopes) == 0:
            self.ui.pushButtonRemoveMicroscope.setEnabled(False)
        else:
            self.ui.pushButtonRemoveMicroscope.setEnabled(True)

    def display_calibration_params(self):
        microscope = self.ui.listWidgetMicroscopes.currentItem().text()
        pc_curve = eval(self.setting_file.read(microscope))
        pc_list = [
            ["", "Slope", "Intersept"],
            ["X: ", pc_curve[0][0], pc_curve[0][1]],
            ["Y: ", pc_curve[1][0], pc_curve[1][1]],
            ["Z: ", pc_curve[2][0], pc_curve[2][1]],
        ]

        QMessageBox.about(
            self,
            microscope,
            tabulate(pc_list, headers="firstrow"),
        )

    def colorPicker(self):
        if self.ui.colorTreeWidget.currentItem().parent() is None:
            return
        phase_index = self.ui.colorTreeWidget.currentIndex().row()

        colorPicker = ColorPicker(parent=self)
        colorPicker.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        colorPicker.exec()
        try:
            color = colorPicker.color
            self.ui.colorTreeWidget.currentItem().setForeground(
                1, QColor(mplcolors.to_hex(color))
            )
            self.ui.colorTreeWidget.setCurrentItem(None)
            self.colors[phase_index] = color
        except:
            pass

    def loadSettings(self):
        if exists("advanced_settings.txt"):
            self.setting_file = SettingFile("advanced_settings.txt")
        else:
            self.createSettingsFile()
            self.setting_file = SettingFile("advanced_settings.txt")
        try:
            self.convention = self.setting_file.read("Convention")
        except:
            self.convention = "TSL"
        try:
            theme = self.setting_file.read("theme")
            if theme == "dark":
                self.ui.darkRadioButton.setChecked(True)
        except:
            self.theme = "light"

        file_types_str = self.setting_file.read(Setting.FILE_TYPES.value)
        self.file_types = json.loads(file_types_str)
        for f in self.file_types:
            self.ui.fileTypeList.addItem(f)

        if self.convention == "TSL":
            self.ui.tslButton.setChecked(True)
        if self.convention == "BRUKER":
            self.ui.brukerButton.setChecked(True)

        if self.setting_file.read("Individual PC data") == "True":
            self.ui.savePcsBox.setChecked(True)
            self.individual_PC_data = True
        else:
            self.individual_PC_data = False

        self.lazy = self.loadSetting(Setting.LAZY_LOADING, True)
        self.ui.lazyLoadingBox.setChecked(self.lazy)

        # TODO: Do this instead
        self.saveIPF = self.loadSetting(Setting.SAVE_IPF, True)
        self.savePhase = self.loadSetting(Setting.SAVE_PHASE, True)
        self.saveNumpy = self.loadSetting(Setting.SAVE_NUMPY, False)

        self.ui.checkBoxSaveIPFMap.setChecked(self.saveIPF)
        self.ui.checkBoxSavePhaseMap.setChecked(self.savePhase)
        self.ui.checkBoxSaveNumpy.setChecked(self.saveNumpy)

        try:
            if self.setting_file.read("Refine orientations") == "True":
                self.ui.checkBoxRefine.setChecked(True)
                self.refine = True
            else:
                self.ui.checkBoxRefine.setChecked(False)
                self.refine = False

        except:
            self.refine = False

        if exists(self.setting_file.read("Default Directory")):
            self.ui.directoryBox.setChecked(True)
            self.directory = self.setting_file.read("Default Directory")
            self.ui.directoryEdit.setText(self.directory)
        else:
            self.directory = False
            self.ui.directoryEdit.setDisabled(True)
            self.ui.browseDirectoryButton.setDisabled(True)

        colors_str = self.setting_file.read("Colors")
        self.colors = json.loads(colors_str)
        for i, c in enumerate(self.colors):
            self.ui.colorTreeWidget.itemAt(0, 0).child(i).setForeground(
                1, QColor(mplcolors.to_hex(c))
            )

        try:
            self.microscopes = self.setting_file.read("MICROSCOPES").split(", ")
            self.microscopes = [ms for ms in self.microscopes if ms]
            self.ui.listWidgetMicroscopes.addItems(self.microscopes)
        except:
            self.microscopes = []
        if not len(self.microscopes):
            self.ui.pushButtonRemoveMicroscope.setEnabled(False)

    # TODO: Use this instead (?)
    def loadSetting(self, setting: Setting, default: object = False) -> object:
        try:
            return eval(self.setting_file.read(setting.value))
        except:
            return default
        
    # TODO: And also this (?) 
    def writeToSetting(self, setting: Setting, value: object):
        self.setting_file.write(setting.value, str(value))

    def saveSettings(self):
        if exists(self.ui.directoryEdit.text()) and self.directory:
            self.directory = self.ui.directoryEdit.text()
        else:
            self.directory = False

        self.setting_file.write(Setting.FILE_TYPES.value, json.dumps(self.file_types))
        self.setting_file.write("Individual PC data", str(self.individual_PC_data))
        self.setting_file.write("Convention", str(self.convention))
        self.setting_file.write(Setting.LAZY_LOADING.value, str(self.lazy))
        self.setting_file.write(Setting.SAVE_IPF.value, str(self.saveIPF))
        self.setting_file.write(Setting.SAVE_PHASE.value, str(self.savePhase))
        self.setting_file.write(Setting.SAVE_NUMPY.value, str(self.saveNumpy))
        self.setting_file.write("Refine orientations", str(self.refine))
        self.setting_file.write("Default Directory", str(self.directory))
        self.setting_file.write("Colors", json.dumps(self.colors))
        if self.ui.darkRadioButton.isChecked():
            self.setting_file.write("theme", "dark")
        else:
            self.setting_file.write("theme", "light")

        self.setting_file.write("MICROSCOPES", ", ".join(self.microscopes))
        self.setting_file.save()

    def createSettingsFile(self):
        f = open("advanced_settings.txt", "w+")
        f.close()

        setting_dict = {
            Setting.FILE_TYPES.value: json.dumps([".h5", ".dat", ".ang", ".jpg", ".png", ".txt"]),
            "Individual PC data": False,
            "Convention": "TSL",
            "Lazy Loading": True,
            Setting.SAVE_IPF.value: True,
            Setting.SAVE_PHASE.value: True,
            Setting.SAVE_NUMPY.value: False,
            "Default Directory": False,
            "Colors": json.dumps(["lime", "red", "blue", "yellow"]),
        }

        self.setting_file = SettingFile("advanced_settings.txt")
        for key, value in setting_dict.items():
            self.setting_file.write(key, str(value))
        self.setting_file.save()
