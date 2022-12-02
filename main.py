import sys
import json
from os.path import basename, splitext, exists
try:
    from os import startfile
except:
    import subprocess
import platform

from contextlib import redirect_stdout, redirect_stderr
from PySide6.QtCore import QDir, Qt, QProcess, QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox
from PySide6.QtGui import QFont
try: 
    import pyi_splash
except:
    pass
# Hidden modules for pyinstaller to detect
import hyperspy
import hyperspy._components.eels_arctan
import hyperspy._components.bleasdale
import hyperspy._components.doniach
import hyperspy._components.eels_double_power_law
import hyperspy._components.eels_arctan
import hyperspy._components.eels_cl_edge
import hyperspy._components.error_function
import hyperspy._components.exponential
import hyperspy._components.expression
import hyperspy._components.gaussian
import hyperspy._components.gaussianhf
import hyperspy._components.heaviside
import hyperspy._components.logistic
import hyperspy._components.lorentzian
import hyperspy._components.offset
import hyperspy._components.pes_core_line_shape
import hyperspy._components.pes_voigt
import hyperspy._components.polynomial_deprecated
import hyperspy._components.polynomial
import hyperspy._components.power_law
import hyperspy._components.rc
import hyperspy._components.pes_see
import hyperspy._components.scalable_fixed_pattern
import hyperspy._components.skew_normal
import hyperspy._components.split_voigt
import hyperspy._components.eels_vignetting
import hyperspy._components.pes_voigt
import hyperspy._components.volume_plasmon_drude
import hyperspy._components.expression
import hyperspy._components.gaussian2d

import kikuchipy 
import kikuchipy.generators.virtual_bse_generator
import kikuchipy.generators._transfer_axes
import kikuchipy.io._io
import kikuchipy._util
import kikuchipy.io._util
import kikuchipy.data._data
import kikuchipy.indexing._dictionary_indexing
import kikuchipy.indexing._merge_crystal_maps
import kikuchipy.indexing._orientation_similarity_map
import kikuchipy.indexing._refinement
import kikuchipy.pattern._pattern
import kikuchipy.simulations._kikuchi_pattern_features
import kikuchipy.simulations._kikuchi_pattern_simulation
import kikuchipy.detectors.ebsd_detector
import kikuchipy.signals._kikuchipy_signal
from kikuchipy.signals._kikuchipy_signal import KikuchipySignal2D, LazyKikuchipySignal2D
import kikuchipy.signals._kikuchi_master_pattern
import kikuchipy.signals.ebsd
import kikuchipy.signals.ebsd_master_pattern
import kikuchipy.signals.ecp_master_pattern
import kikuchipy.signals.virtual_bse_image

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from ui.ui_main_window import Ui_MainWindow
from utils.filebrowser import FileBrowser
from utils.setting_file import SettingFile
from utils.worker import toWorker
from scripts.hough_indexing import HiSetupDialog
from scripts.pattern_processing import PatternProcessingDialog
from scripts.dictionary_indexing import DiSetupDialog
from scripts.pre_indexing_maps import *
from scripts.advanced_settings import AdvancedSettingsDialog
from scripts.console import Console, Redirect
from scripts.pattern_center import PatterCenterDialog
from scripts.region_of_interest import RegionOfInteresDialog

KP_EXTENSIONS = (".h5", ".dat")
IMAGE_EXTENSIONS = ()


class AppWindow(QMainWindow):
    """
    The main app window that is present at all times
    """

    working_dir = QDir.currentPath()
    file_selected = None

    def __init__(self) -> None:
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()

        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.systemModel = QFileSystemModel()

        #Check platform and set windowStayOnTopHint
        if platform.system() == "Darwin":
            self.stayOnTopHint = True
        else:
            self.stayOnTopHint = False

        self.ui.systemViewer.setModel(self.systemModel)
        self.setupConnections()

        self.console = Console(parent=self, context=globals())
        self.console.setfont(QFont("Lucida Sans Typewriter", 10))

        self.showImage(self.file_selected)
        self.importSettings()
        try:
            pyi_splash.close()
        except Exception as e:
            pass

    def setupConnections(self):
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.selectionModel().selectionChanged.connect(
            lambda new, old: self.onSystemModelChanged(new, old)
        )
        self.ui.systemViewer.doubleClicked.connect(lambda: self.openTextFile())
        self.ui.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )
        self.ui.actionSettings.triggered.connect(lambda: self.openSettings())
        self.ui.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())
        self.ui.actionROI.triggered.connect(lambda: self.selectROI())
        self.ui.actionSignalNavigation.triggered.connect(
            lambda: self.selectSignalNavigation()
        )
        self.ui.actionDictionary_indexing.triggered.connect(
            lambda: self.selectDictionaryIndexingSetup()
        )
        self.ui.actionHough_indexing.triggered.connect(
            lambda: self.selectHoughIndexingSetup()
        )
        self.ui.actionPattern_Center.triggered.connect(
            lambda: self.selectPatternCenter()
        )
        self.ui.actionAverage_dot_product.triggered.connect(lambda: toWorker(save_adp_map, self.console, self.file_selected))
        self.ui.actionImage_quality.triggered.connect(lambda: toWorker(save_iq_map, self.console, self.file_selected))
        self.ui.actionMean_intensity.triggered.connect(lambda: toWorker(save_mean_intensity_map, self.console, self.file_selected))
        self.ui.actionVirtual_backscatter_electron.triggered.connect(lambda: toWorker(save_rgb_vbse, self.console, self.file_selected))
    
    def selectWorkingDirectory(self):
        if self.fileBrowserOD.getFile():
            self.working_dir = self.fileBrowserOD.getPaths()[0]
            self.file_selected = None
            self.fileBrowserOD.setDefaultDir(self.working_dir)
            self.setSystemViewer(self.working_dir)

    def setSystemViewer(self, working_dir):
        self.systemModel.setRootPath(working_dir)
        self.systemModel.setNameFilters(self.system_view_filter)
        self.systemModel.setNameFilterDisables(0)
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.setRootIndex(self.systemModel.index(working_dir))
        self.ui.systemViewer.setColumnWidth(0, 250)
        self.ui.systemViewer.hideColumn(2)

        self.ui.folderLabel.setText(basename(working_dir))
        self.setWindowTitle(f"EBSD-GUI - {working_dir}")

    def importSettings(self):
        if exists("advanced_settings.txt"):
            setting_file = SettingFile("advanced_settings.txt")
            try:
                file_types = json.loads(setting_file.read("File Types"))
                self.system_view_filter = ["*" + x for x in file_types]
            except:
                self.system_view_filter = [
                    "*.h5",
                    "*.dat",
                    "*.ang",
                    "*.jpg",
                    "*.png",
                    "*.txt",
                ]

            if exists(setting_file.read("Default Directory")):
                self.working_dir = setting_file.read("Default Directory")
                self.setSystemViewer(self.working_dir)
        else:
            AdvancedSettingsDialog(parent=self).createSettingsFile()
            setting_file = SettingFile("advanced_settings.txt")
            file_types = json.loads(setting_file.read("File Types"))
            self.system_view_filter = ["*" + x for x in file_types]

    def openSettings(self):
        try:
            self.settingsDialog = AdvancedSettingsDialog(parent=self)
            self.settingsDialog.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.settingsDialog.exec()
        except Exception as e:
            self.console.errorwrite(
                f"Could not initialize settings dialog:\n{str(e)}\n"
            )

        # updates file browser to changes:
        setting_file = SettingFile("advanced_settings.txt")
        file_types = json.loads(setting_file.read("File Types"))
        self.system_view_filter = ["*" + x for x in file_types]
        if setting_file.read("Default Directory") not in ["False", ""]:
            if self.working_dir == QDir.currentPath():
                self.working_dir = setting_file.read("Default Directory")
            self.setSystemViewer(self.working_dir)

        self.systemModel.setNameFilters(self.system_view_filter)

    def selectProcessing(self):
        try:
            self.processingDialog = PatternProcessingDialog(
                parent=self, pattern_path=self.file_selected
            )
            self.processingDialog.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.processingDialog.exec()
        except Exception as e:
            self.console.errorwrite(
                f"Could not initialize processing dialog:\n{str(e)}\n"
            )

    def selectROI(self):
        try:
            plt.close("all")
        except Exception as e:
            print(e)
            pass
        try:
            self.ROIDialog = RegionOfInteresDialog(
                parent=self, pattern_path=self.file_selected
            )
            self.ROIDialog.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.ROIDialog.exec()
        except Exception as e:
            self.console.errorwrite(f"Could not initialize ROI dialog:\n{str(e)}\n")

    def onSystemModelChanged(self, new_selected, old_selected):
        if new_selected.empty():
            self.file_selected = None
        else:
            self.file_selected = self.systemModel.filePath(
                self.ui.systemViewer.currentIndex()
            )
        self.updateMenuButtons(self.file_selected)
        self.showImage(self.file_selected)

    def openTextFile(self):
        index = self.ui.systemViewer.currentIndex()
        self.file_selected = self.systemModel.filePath(index)
        
        if splitext(self.file_selected)[1] in [".txt"]:
            if platform.system().lower() == "darwin":
                subprocess.call(['open', '-a', 'TextEdit', self.file_selected])
            if platform.system().lower() == "windows":
                startfile(self.file_selected)

    def process_finished(self):
        print("EBSD pattern closed.")
        self.p = None

    def selectSignalNavigation(self):
        try:
            self.p = QProcess()
            print("Loading EBSD patterns ...")
            self.p.start("python", ['scripts/signal_navigation.py', self.file_selected])
            self.p.finished.connect(self.process_finished)
            #subprocess.run(["python", "scripts/signal_navigation.py"], text=True, input=self.file_selected)
    
        
        except Exception as e:
            if self.file_selected == "":
                dlg = QMessageBox(self)
                dlg.setWindowTitle("No file")
                dlg.setText("You have to choose a pattern.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Warning)
                dlg.exec()
            self.console.errorwrite(
                f"Could not initialize signal navigation:\n{str(e)}\n"
            )

    def selectDictionaryIndexingSetup(self):
        try:
            self.diSetup = DiSetupDialog(parent=self, pattern_path=self.file_selected)
            self.diSetup.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.diSetup.show()
        except Exception as e:
            self.console.errorwrite(
                f"Could not initialize dictionary indexing:\n{str(e)}\n"
            )

    def selectHoughIndexingSetup(self):
        try:
            self.hiSetup = HiSetupDialog(parent=self, pattern_path=self.file_selected)
            self.hiSetup.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.hiSetup.show()
        except Exception as e:
            self.console.errorwrite(f"Could not initialize hough indexing:\n{str(e)}\n")

    def selectPatternCenter(self):
        try:
            self.patternCenter = PatterCenterDialog(
                parent=self, file_selected=self.file_selected
            )
            self.patternCenter.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.patternCenter.show()
        except Exception as e:
            self.console.errorwrite(
                f"Could not initialize pattern center refinement:\n{str(e)}\n"
            )

    def showImage(self, image_path):
        if image_path == None or not splitext(image_path)[1] in [
            ".jpg",
            ".png",
            ".gif",
            ".bmp",
        ]:
            image = mpimg.imread("resources/ebsd_gui.png")
        else:
            image = mpimg.imread(image_path)
        self.ui.MplWidget.canvas.ax.clear()
        self.ui.MplWidget.canvas.ax.axis(False)
        self.ui.MplWidget.canvas.ax.imshow(image)
        self.ui.MplWidget.canvas.draw()

    def updateMenuButtons(self, file_path):
        """
        Updates the menu buttons based on the extension of file_path
        """

        def setAllMenu(enabled):
            self.ui.menuProcessing.setEnabled(enabled)
            self.ui.menuPlot.setEnabled(enabled)
            self.ui.menuIndexing.setEnabled(enabled)
            self.ui.menuPre_indexing_maps.setEnabled(enabled)
            self.ui.actionSignalNavigation.setEnabled(enabled)

        if file_path == None:
            return
        file_extension = splitext(file_path)[1]

        if file_extension in KP_EXTENSIONS:
            kp_enabled = True
        else:
            kp_enabled = False
        setAllMenu(kp_enabled)

        # Special case for plotting calibration patterns from Settings.txt
        if basename(file_path) == "Setting.txt":
            self.ui.menuPlot.setEnabled(True)
            self.ui.actionSignalNavigation.setEnabled(True)
            self.ui.menuPre_indexing_maps.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP = AppWindow()

    # Redirect stdout to console.write and stderr to console.errorwrite
    with redirect_stdout(APP.console), redirect_stderr(
        Redirect(APP.console.errorwrite)
    ):
        APP.show()
        print(f"Multithreading with maximum {QThreadPool.globalInstance().maxThreadCount()} threads")
        print(
            """Use keyword APP to access application components, e.g. 'APP.setWindowTitle("My window")'"""
        )
        try:
            sys.exit(app.exec())
        except Exception as e:
            print(e)
            print("A clean exit was not performed")
