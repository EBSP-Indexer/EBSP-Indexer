import json
from os.path import exists

import matplotlib.colors as mplcolors
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog

from scripts.color_picker import ColorPicker
from ui.ui_advanced_settings import Ui_AdvancedSettings
from utils import FileBrowser, SettingFile


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
        self.ui.addFileTypeButton.clicked.connect(lambda: self.addFileType())
        self.ui.removeFileTypeButton.clicked.connect(lambda: self.removeFileType())
        self.ui.resetFileTypeButton.clicked.connect(lambda: self.resetFileType())
        self.ui.brukerButton.clicked.connect(lambda: self.setBruker())
        self.ui.tslButton.clicked.connect(lambda: self.setTSL())
        self.ui.lazyLoadingBox.clicked.connect(lambda: self.setLazy())
        self.ui.checkBoxRefine.clicked.connect(lambda: self.setRefine())
        self.ui.savePcsBox.clicked.connect(lambda: self.setIndividualPCData())
        self.ui.buttonBox.accepted.connect(lambda: self.saveSettings())
        self.ui.directoryBox.clicked.connect(lambda: self.toggleDefaultDirectory())
        self.ui.browseDirectoryButton.clicked.connect(lambda: self.browseDirectory())
        self.ui.colorTreeWidget.doubleClicked.connect(lambda: self.colorPicker())

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
        if self.ui.savePcsBox.isChecked():
            self.individual_PC_data = True
        else:
            self.individual_PC_data = False

    def setLazy(self):
        if self.ui.lazyLoadingBox.isChecked():
            self.lazy = True
        else:
            self.lazy = False

    def setRefine(self):
        self.refine = self.ui.checkBoxRefine.isChecked()

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

        file_types_str = self.setting_file.read("File Types")
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

        if self.setting_file.read("Lazy Loading") == "True":
            self.ui.lazyLoadingBox.setChecked(True)
            self.lazy = True
        else:
            self.lazy = False

        try:
            if self.setting_file.read("Refine orientations") == "True":
                self.ui.checkBoxRefine.setChecked(True)
                self.refine = True
            else:
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

    def saveSettings(self):
        if exists(self.ui.directoryEdit.text()) and self.directory:
            self.directory = self.ui.directoryEdit.text()
        else:
            self.directory = False

        self.setting_file.write("File Types", json.dumps(self.file_types))
        self.setting_file.write("Individual PC data", str(self.individual_PC_data))
        self.setting_file.write("Convention", str(self.convention))
        self.setting_file.write("Lazy Loading", str(self.lazy))
        self.setting_file.write("Refine orientations", str(self.refine))
        self.setting_file.write("Default Directory", str(self.directory))
        self.setting_file.write("Colors", json.dumps(self.colors))
        self.setting_file.save()

    def createSettingsFile(self):
        f = open("advanced_settings.txt", "w+")
        f.close()

        setting_dict = {
            "File Types": json.dumps([".h5", ".dat", ".ang", ".jpg", ".png", ".txt"]),
            "Individual PC data": False,
            "Convention": "TSL",
            "Lazy Loading": True,
            "Default Directory": False,
            "Colors": json.dumps(["lime", "red", "blue", "yellow"]),
        }

        self.setting_file = SettingFile("advanced_settings.txt")
        for key, value in setting_dict.items():
            self.setting_file.write(key, str(value))
        self.setting_file.save()
