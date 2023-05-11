# Copyright (c) 2022 EBSP Indexer developers
#
# This file is part of EBSP Indexer.

# EBSP Indexer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# EBSP Indexer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import multiprocessing

multiprocessing.freeze_support()  # Pyinstaller fix for MacOS

import json
import logging
import os
import platform
import sys
from contextlib import redirect_stderr, redirect_stdout

from PySide6.QtCore import QDir, Qt, QThreadPool, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

if platform.system().lower() != "darwin":
    import qdarktheme
logging.getLogger("pyopencl").setLevel(logging.WARNING)
logging.getLogger("hyperspy").setLevel(logging.WARNING)
logging.getLogger("kikuchipy").setLevel(logging.WARNING)

# Modules available from start in the console
import hyperspy as hs
import kikuchipy as kp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from kikuchipy import (
    load,
)  # Import something from kikutchipy to avoid load times during dialog initalizations

import resources_rc  # Imports resources in a pythonic way from resources.qrc
from scripts.advanced_settings import AdvancedSettingsDialog
from scripts.console import Console
from scripts.dictionary_indexing import DiSetupDialog
from scripts.hough_indexing import HiSetupDialog
from scripts.pattern_center import PatterCenterDialog
from scripts.pc_selection import PCSelectionDialog
from scripts.pattern_processing import PatternProcessingDialog
from scripts.pre_indexing_maps import (
    save_adp_map,
    save_iq_map,
    save_mean_intensity_map,
    save_rgb_vbse,
)
from scripts.refinement import RefineSetupDialog
from scripts.region_of_interest import RegionOfInteresDialog
from scripts.signal_navigation_widget import SignalNavigationWidget
from scripts.system_explorer import SystemExplorerWidget
from ui.ui_main_window import Ui_MainWindow
from utils import FileBrowser, Redirect, SettingFile, sendToWorker, resource_path

NUM_OF_THREADS = 1

KP_EXTENSIONS = (".h5", ".dat")
IMAGE_EXTENSIONS = ()


class AppWindow(QMainWindow):
    """
    The main app window that is present at all times
    """

    working_dir = QDir.currentPath()

    def __init__(self) -> None:
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(
            None
        )  # NB! Only set to none if there are nothing inside the central widget
        self.showMaximized()

        self.systemExplorer = SystemExplorerWidget(self)
        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.console = Console(parent=self, context=globals())
        self.signalNavigationWidget = SignalNavigationWidget(mainWindow=self)

        # Check platform and set windowStayOnTopHint
        if platform.system() == "Darwin":
            self.stayOnTopHint = True
        else:
            self.stayOnTopHint = False

        self.setupConnections()
        self.importSettings()
        self.showImage()
        self.updateActiveJobs()

    def setupConnections(self):
        self.ui.dockWidgetSystemExplorer.setWidget(self.systemExplorer)
        self.ui.dockWidgetSignalNavigation.setWidget(self.signalNavigationWidget)
        self.tabifyDockWidget(
            self.ui.dockWidgetImageViewer, self.ui.dockWidgetSignalNavigation
        )
        self.ui.dockWidgetImageViewer.setFocus()
        self.ui.dockWidgetJobManager.setHidden(True)
        self.ui.dockWidgetSignalNavigation.setHidden(True)
        self.ui.statusbar.addPermanentWidget(self.ui.threadsLabel)
        self.systemExplorer.pathChanged.connect(
            lambda new_path: self.updateMenuButtons(new_path)
        )
        # self.systemExplorer.pathChanged.connect(
        #     lambda new_path: self.showImage(new_path)
        # )
        self.systemExplorer.requestImageViewer.connect(
            lambda image_path: self.showImage(image_path)
        )
        self.systemExplorer.requestSignalNavigation.connect(
            lambda signal_path: self.selectSignalNavigation(signal_path)
        )

        self.ui.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )
        self.ui.actionSettings.triggered.connect(lambda: self.openSettings())
        self.ui.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())
        self.ui.actionROI.triggered.connect(lambda: self.selectROI())
        self.ui.actionSignalNavigation.triggered.connect(
            lambda: self.selectSignalNavigation(signal_path=self.getSelectedPath())
        )
        self.ui.actionDictionaryIndexing.triggered.connect(
            lambda: self.selectDictionaryIndexingSetup(
                pattern_path=self.getSelectedPath()
            )
        )
        self.ui.actionHoughIndexing.triggered.connect(
            lambda: self.selectHoughIndexingSetup(pattern_path=self.getSelectedPath())
        )
        self.ui.actionRefineOrientations.triggered.connect(
            lambda: self.selectRefineOrientations(file_path=self.getSelectedPath())
        )
        self.ui.actionCalibration_patterns.triggered.connect(
            lambda: self.selectPatternCenter()
        )
        self.ui.actionPattern_selection.triggered.connect(
            lambda: self.openPCSelection(pattern_path=self.getSelectedPath())
        )
        # if platform.system().lower() != "darwin":
        # self.ui.actionAverage_dot_product.triggered.connect(
        #     lambda: save_adp_map(pattern_path=self.getSelectedPath())
        # )
        # self.ui.actionImage_quality.triggered.connect(
        #     lambda: save_iq_map(pattern_path=self.getSelectedPath())
        # )
        # self.ui.actionMean_intensity.triggered.connect(
        #     lambda: save_mean_intensity_map(pattern_path=self.getSelectedPath())
        # )
        # self.ui.actionVirtual_backscatter_electron.triggered.connect(
        #     lambda: save_rgb_vbse(pattern_path=self.getSelectedPath())
        # )

        # else:
        
        self.ui.actionAverage_dot_product.triggered.connect(
            lambda: self.generatePreIndexingMap(map=0)
        )
        self.ui.actionImage_quality.triggered.connect(
            lambda: self.generatePreIndexingMap(map=1)
        )
        self.ui.actionMean_intensity.triggered.connect(
            lambda: self.generatePreIndexingMap(map=2)
        )
        self.ui.actionVirtual_backscatter_electron.triggered.connect(
            lambda: self.generatePreIndexingMap(map=3)
        )

    def generatePreIndexingMap(self, map: int):
        """
        0 = average dot product map
        1 = image quality map
        2 = mean intensity map
        3 = virual BSE image
        """

        def image_saved():
            sb.showMessage("Image saved", 3000)

        pattern_path = self.getSelectedPath()
        sb = self.ui.statusbar

        if map == 0:
            sb.showMessage("Generating average dot product map ...")
            worker = sendToWorker(self, save_adp_map, pattern_path=pattern_path)
        if map == 1:
            sb.showMessage("Generating image quality map ...")
            worker = sendToWorker(self, save_iq_map, pattern_path=pattern_path)
        if map == 2:
            sb.showMessage("Generating mean intensity map ...")
            worker = sendToWorker(
                self, save_mean_intensity_map, pattern_path=pattern_path
            )
        if map == 3:
            sb.showMessage("Generating VBSE image ...")
            worker = sendToWorker(self, save_rgb_vbse, pattern_path=pattern_path)

        worker.isFinished.connect(image_saved)

    # Override closeEvent from QMainWindow
    def closeEvent(self, event):
        if QThreadPool.globalInstance().activeThreadCount() != 0:
            reply = QMessageBox.question(
                self,
                "Close EBSP Indexer",
                "Some jobs are still running.\nAre you sure you want to close EBSP Indexer?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,  # Default button
            )
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def selectWorkingDirectory(self):
        if self.fileBrowserOD.getFile():
            self.working_dir = self.fileBrowserOD.getPaths()[0]
            self.fileBrowserOD.setDefaultDir(self.working_dir)
            if os.path.exists("advanced_settings.txt"):
                setting_file = SettingFile("advanced_settings.txt")
                try:
                    file_types = json.loads(setting_file.read("File Types"))
                    system_view_filter = ["*" + x for x in file_types]
                    self.systemExplorer.setSystemViewer(
                        self.working_dir, system_view_filter
                    )
                except:
                    self.systemExplorer.setSystemViewer(self.working_dir)
            else:
                self.systemExplorer.setSystemViewer(self.working_dir)

    def getSelectedPath(self) -> str:
        return self.systemExplorer.selected_path

    def importSettings(self):
        if os.path.exists("advanced_settings.txt"):
            setting_file = SettingFile("advanced_settings.txt")
            if platform.system().lower() != "darwin":
                try:
                    self.theme = setting_file.read("theme")
                except:
                    self.theme = "light"
                qdarktheme.setup_theme(self.theme)
            try:
                file_types = json.loads(setting_file.read("File Types"))
                system_view_filter = ["*" + x for x in file_types]
            except:
                system_view_filter = [
                    "*.h5",
                    "*.dat",
                    "*.ang",
                    "*.jpg",
                    "*.png",
                    "*.txt",
                ]

            if os.path.exists(setting_file.read("Default Directory")):
                self.working_dir = setting_file.read("Default Directory")
                self.systemExplorer.setSystemViewer(
                    self.working_dir, system_view_filter
                )
        else:
            AdvancedSettingsDialog(parent=self).createSettingsFile()
            setting_file = SettingFile("advanced_settings.txt")
            file_types = json.loads(setting_file.read("File Types"))
            self.system_view_filter = ["*" + x for x in file_types]
            self.theme = "light"

    def openSettings(self):
        try:
            self.settingsDialog = AdvancedSettingsDialog(parent=self)
            self.settingsDialog.setWindowFlag(
                Qt.WindowStaysOnTopHint, self.stayOnTopHint
            )
            if self.settingsDialog.exec() == QDialog.Accepted:
                setting_file = SettingFile("advanced_settings.txt")
                file_types = json.loads(setting_file.read("File Types"))
                self.theme = setting_file.read("theme")
                system_view_filters = ["*" + x for x in file_types]
                if setting_file.read("Default Directory") not in ["False", ""]:
                    new_dir = setting_file.read("Default Directory")
                    if self.working_dir != new_dir:
                        self.working_dir = new_dir
                    self.systemExplorer.setSystemViewer(
                        self.working_dir, filters=system_view_filters
                    )
                if platform.system().lower() != "darwin":
                    qdarktheme.setup_theme(self.theme)
                self.showImage()
        except Exception as e:
            raise e

    def selectRefineOrientations(self, file_path: str):
        try:
            self.refineDialog = RefineSetupDialog(parent=self, file_path=file_path)
            self.refineDialog.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.refineDialog.exec()
        except Exception as e:
            raise e

    def selectProcessing(self):
        try:
            self.processingDialog = PatternProcessingDialog(
                parent=self, pattern_path=self.getSelectedPath()
            )
            self.processingDialog.setWindowFlag(
                Qt.WindowStaysOnTopHint, self.stayOnTopHint
            )
            self.processingDialog.exec()
        except Exception as e:
            raise e

    def selectROI(self):
        try:
            plt.close("all")
        except Exception as e:
            self.console.errorwrite(e)
        try:
            self.ROIDialog = RegionOfInteresDialog(
                parent=self, pattern_path=self.getSelectedPath()
            )
            self.ROIDialog.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.ROIDialog.exec()
        except Exception as e:
            raise e

    def selectSignalNavigation(self, signal_path: str):
        try:
            self.signalNavigationWidget.load_dataset(signal_path)
            dw = self.ui.dockWidgetSignalNavigation
            dw.setWindowTitle(f"Signal Navigation - {os.path.basename(signal_path)}")
            if dw.isHidden():
                dw.setVisible(True)
            dw.raise_()
        except Exception as e:
            if self.getSelectedPath() == "":
                dlg = QMessageBox(self)
                dlg.setWindowTitle("No file")
                dlg.setText("You have to choose a pattern.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Warning)
                dlg.exec()
            raise e

    def selectDictionaryIndexingSetup(self, pattern_path: str):
        try:
            self.diSetup = DiSetupDialog(self, pattern_path)
            self.diSetup.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.diSetup.show()
        except Exception as e:
            raise e

    def selectHoughIndexingSetup(self, pattern_path: str):
        try:
            self.hiSetup = HiSetupDialog(self, pattern_path)
            self.hiSetup.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.hiSetup.show()
        except Exception as e:
            raise e

    def selectPatternCenter(self):
        try:
            self.patternCenter = PatterCenterDialog(
                parent=self, file_selected=self.getSelectedPath()
            )
            self.patternCenter.setWindowFlag(
                Qt.WindowStaysOnTopHint, self.stayOnTopHint
            )
            self.patternCenter.show()
        except Exception as e:
            raise e

    def openPCSelection(self, pattern_path: str):
        try:
            self.PCSelection = PCSelectionDialog(self, pattern_path)
            self.PCSelection.setWindowFlag(Qt.WindowStaysOnTopHint, self.stayOnTopHint)
            self.PCSelection.show()
        except Exception as e:
            raise e

    def showImage(self, image_path: str = ""):
        imageViewer = self.ui.dockWidgetImageViewer
        if imageViewer.isHidden():
            imageViewer.setVisible(True)
        imageViewer.raise_()
        try:
            if len(image_path):
                image = mpimg.imread(resource_path(image_path))
                imageViewer.setWindowTitle(
                    f"Image Viewer - {os.path.basename(image_path)}"
                )
            else:
                if self.theme == "dark":
                    im_path = resource_path("resources/ebsp_indexer_logo_dark_hd.png")
                else:
                    im_path = resource_path("resources/ebsd_gui.png")                    
                image = mpimg.imread(im_path) 
                imageViewer.setWindowTitle(f"Image Viewer")
            self.ui.MplWidget.canvas.ax.clear()
            self.ui.MplWidget.canvas.ax.axis(False)
            self.ui.MplWidget.canvas.ax.imshow(image)
            self.ui.MplWidget.canvas.draw()
        except:
            pass

    def updateMenuButtons(self, file_path):
        """
        Updates the menu buttons based on the extension of file_path
        """

        def setAvailableMenuActions(enabled):
            self.ui.menuProcessing.setEnabled(enabled)
            self.ui.menuPatternInspection.setEnabled(enabled)
            self.ui.menuIndexing.setEnabled(enabled)
            self.ui.menuPre_indexing_maps.setEnabled(enabled)
            self.ui.actionSignalNavigation.setEnabled(enabled)
            self.ui.menuRefinement.setEnabled(enabled)

        if file_path == "":
            setAvailableMenuActions(False)
            return
        file_extension = os.path.splitext(file_path)[1]

        if file_extension in KP_EXTENSIONS:
            kp_enabled = True
        else:
            kp_enabled = False
        setAvailableMenuActions(kp_enabled)

        # Special case for plotting calibration patterns from Settings.txt, currently not avaiable
        # if os.path.basename(file_path) == "Setting.txt":
        #     self.ui.menuPatternInspection.setEnabled(True)
        #     self.ui.actionSignalNavigation.setEnabled(True)
        #     self.ui.menuPre_indexing_maps.setEnabled(False)

    # TODO Move removeWorker and updateActiveJobs to a jobmanagerlist class
    @Slot(int)
    def removeWorker(self, worker_id: int):
        jobList = self.ui.jobList
        for i in range(jobList.count()):
            item = jobList.item(i)
            if jobList.itemWidget(item).id == worker_id:
                jobList.takeItem(jobList.row(item))
                break

    @Slot()
    def updateActiveJobs(self):
        msg = f"{QThreadPool.globalInstance().activeThreadCount()} out of {QThreadPool.globalInstance().maxThreadCount()} active jobs"
        self.ui.threadsLabel.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QThreadPool.globalInstance().setMaxThreadCount(NUM_OF_THREADS)
    if platform.system().lower() != "darwin":
        qdarktheme.setup_theme("light")
    app.setWindowIcon(QIcon(":/icons/app_icon.ico"))
    APP = AppWindow()
    # Redirect stdout to console.write and stderr to console.errorwrite
    with redirect_stdout(APP.console), redirect_stderr(
        Redirect(APP.console.errorwrite)
    ):
        APP.show()
        print(
            """EBSP Indexer  Copyright (C) 2023  EBSP Indexer Developers 
This program comes with ABSOLUTELY NO WARRANTY; for details see COPYING.txt.
This is free software, and you are welcome to redistribute it under certain conditions; see COPYING.txt for details.""",
        )
        try:
            sys.exit(app.exec())
        except Exception as e:
            print(e)
            print("A clean exit was not performed")
