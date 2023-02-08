import sys
import json
from os.path import basename, splitext, exists
try:
    from os import startfile
except:
    import subprocess
try:
    import pyopencl
    from pyopencl.tools import get_test_platforms_and_devices
except:
    print("PyOpenCL could not be imported")
import platform

from contextlib import redirect_stdout, redirect_stderr
from PySide6.QtCore import QDir, Qt, QThreadPool, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox
from PySide6.QtGui import QFont
try: 
    import pyi_splash
except:
    pass
# Modules available from start in the console
import kikuchipy as kp
import hyperspy.api as hs

# Import something from kikutchipy to avoid load times during dialog initalizations
from kikuchipy import load

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

from ui.ui_main_window import Ui_MainWindow
from utils.filebrowser import FileBrowser
from utils.setting_file import SettingFile
from utils.worker import toWorker
from scripts.hough_indexing import HiSetupDialog
from scripts.pattern_processing import PatternProcessingDialog
from scripts.signal_navigation import open_pattern, get_navigation_figure
from scripts.dictionary_indexing import DiSetupDialog
from scripts.pre_indexing_maps import save_adp_map, save_mean_intensity_map, save_rgb_vbse, save_iq_map
from scripts.advanced_settings import AdvancedSettingsDialog
from scripts.console import Console, Redirect
from scripts.pattern_center import PatterCenterDialog
from scripts.region_of_interest import RegionOfInteresDialog

hs.set_log_level('CRITICAL')

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
        self.ui.systemViewer.doubleClicked.connect(lambda: self.doubleClickEvent())
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

        self.ui.pushButtonMeanNav.clicked.connect(lambda: self.plot_navigator(self.file_selected, "mean_intensity"))
        self.ui.pushButtonIQNav.clicked.connect(lambda: self.plot_navigator(self.file_selected, nav_type="iq"))
    
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

    def doubleClickEvent(self):
        index = self.ui.systemViewer.currentIndex()
        self.file_selected = self.systemModel.filePath(index)
        
        if splitext(self.file_selected)[1] in [".txt"]:
            if platform.system().lower() == "darwin":
                subprocess.call(['open', '-a', 'TextEdit', self.file_selected])
            if platform.system().lower() == "windows":
                startfile(self.file_selected)

        # open dataset for signal navigation
        if splitext(self.file_selected)[1] in [".h5", ".dat"]:
            self.plot_navigator(self.file_selected)

    def process_finished(self):
        print("EBSD pattern closed.")
        self.p = None

    def selectSignalNavigation(self):
        try:
            self.plot_navigator(self.file_selected)
        
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
            self.ui.dockWidgetImageViewer.setWindowTitle(f"Image Viewer")
        else:
            image = mpimg.imread(image_path)
            self.ui.dockWidgetImageViewer.setWindowTitle(f"Image Viewer - {image_path}")
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

    def plot_navigator(self, file_path, nav_type="mean_intensity"):
        try:
            self.ui.navigatorMplWidget.canvas.mpl_disconnect(self.cid)
        except:
            pass

        s = open_pattern(file_path)
        
        navigator = get_navigation_figure(s, nav_type)

        self.ui.navigatorMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.navigatorMplWidget.canvas.ax.clear()
        self.ui.navigatorMplWidget.canvas.ax.axis(False)
        self.cursor = Cursor(self.ui.navigatorMplWidget.canvas.ax, useblit=True, color="yellow", linewidth=3, linestyle="--", alpha=0.8)
        self.cursor.set_active(True)
        self.ui.navigatorMplWidget.canvas.ax.imshow(navigator, cmap="gray")
        self.ui.navigatorMplWidget.canvas.draw()
        #plot pattern from upper left corner
        self.plot_signal(s, 0, 0)
        #canvas id to later disconnect
        self.cid = self.ui.navigatorMplWidget.canvas.mpl_connect("button_press_event", lambda event: self.on_click_navigator(event, s))


    def plot_signal(self, pattern, x_index, y_index):
        
        signal = pattern.data[y_index, x_index]
        
        self.ui.signalMplWidget.vbl.setContentsMargins(0, 0, 0, 0)
        self.ui.signalMplWidget.canvas.ax.clear()
        self.ui.signalMplWidget.canvas.ax.axis(False)
        self.ui.signalMplWidget.canvas.ax.imshow(signal, cmap="gray")
        self.ui.signalMplWidget.canvas.draw()

    def on_click_navigator(self, event, s):
        if event.inaxes:
            self.plot_signal(s, int(event.xdata), int(event.ydata))

        
    @Slot(int)
    def removeWorker(self, worker_id: int):
        jobList = self.ui.jobList
        for i in range(jobList.count()):
            item = jobList.item(i)
            if(jobList.itemWidget(item).id == worker_id):
                jobList.takeItem(jobList.row(item))
                break

    def countWorkers(self) -> int:
        return self.ui.jobList.count()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    APP = AppWindow()
    # Redirect stdout to console.write and stderr to console.errorwrite
    with redirect_stdout(APP.console), redirect_stderr(
        Redirect(APP.console.errorwrite)
    ):
        APP.setCentralWidget(None)  #NB! Only set to none if there are nothing inside the central widget
        APP.show()
        print(f"Multithreading with maximum {QThreadPool.globalInstance().maxThreadCount()} threads")
        print(
            """Use keyword APP to access application components, e.g. 'APP.setWindowTitle("My window")'"""
        )
        print(get_test_platforms_and_devices())
        try:
            sys.exit(app.exec())
        except Exception as e:
            print(e)
            print("A clean exit was not performed")
