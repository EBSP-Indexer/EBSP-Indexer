import sys
from os.path import basename
from contextlib import redirect_stdout, redirect_stderr
from PySide6.QtCore import QDir, QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QMessageBox
from PySide6.QtGui import QFont
from scripts.hough_indexing import HiSetupDialog
from ui.ui_main_window import Ui_MainWindow

from utils.filebrowser import FileBrowser
from scripts.pattern_processing import PatternProcessingDialog
from scripts.signal_navigation import SignalNavigation
from scripts.dictionary_indexing import DiSetupDialog

# from scripts.interpreter import ConsoleWidget
from scripts.console import Console, Redirect
from scripts.pattern_center import PatterCenterDialog
from scripts.region_of_interest import RegionOfInteresDialog
from scripts.setting_file import SettingFile

SYSTEM_VIEWER_FILTER = ["*.h5", "*.dat", "*.ang", "*.jpg", "*.png", "*.gif", "*.txt"]


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
        self.setupConnections()

        self.threadPool = QThreadPool()

        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.systemModel = QFileSystemModel()

        # variables = (
        #     globals()
        # )  # TEMPERORY!!!: accessing variables in different thread may lead to crash
        # self.console = ConsoleWidget(self.ui, variables)
        self.console = Console(parent=self, context=globals())
        self.console.setfont(QFont("Lucida Sans Typewriter", 10))

    def setupConnections(self):
        self.ui.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )
        self.ui.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())
        self.ui.actionROI.triggered.connect(lambda: self.selectROI())
        self.ui.systemViewer.clicked.connect(
            lambda index: self.onSystemViewClicked(index)
        )
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

    def selectWorkingDirectory(self):
        if self.fileBrowserOD.getFile():
            self.working_dir = self.fileBrowserOD.getPaths()[0]
            self.file_selected = None
            self.fileBrowserOD.setDefaultDir(self.working_dir)

            # Setting the system viewer
            self.systemModel.setRootPath(self.working_dir)
            self.systemModel.setNameFilters(SYSTEM_VIEWER_FILTER)
            self.systemModel.setNameFilterDisables(0)
            self.ui.systemViewer.setModel(self.systemModel)
            self.ui.systemViewer.setRootIndex(self.systemModel.index(self.working_dir))
            self.ui.systemViewer.setColumnWidth(0, 250)
            self.ui.systemViewer.hideColumn(2)

            self.ui.folderLabel.setText(basename(self.working_dir))
            self.setWindowTitle(f"EBSD-GUI - {self.working_dir}")

    def selectProcessing(self):
        try:
            self.processingDialog = PatternProcessingDialog(
                parent=self, pattern_path=self.file_selected
            )
            self.processingDialog.exec()
        except Exception as e:
            print(f"Could not initialize processing dialog:\n{str(e)}\n")

    def selectROI(self):
        try:
            self.ROIDialog = RegionOfInteresDialog(pattern_path=self.file_selected)
            self.ROIDialog.exec()
        except Exception as e:
            print(f"Could not initialize ROI dialog:\n{str(e)}\n")

    def onSystemViewClicked(self, index):
        self.file_selected = self.systemModel.filePath(index)

    def selectSignalNavigation(self):
        try:
            self.signalNavigation = SignalNavigation(file_path=self.file_selected)
        except Exception as e:
            if self.file_selected == "":
                dlg = QMessageBox(self)
                dlg.setWindowTitle("No file")
                dlg.setText("You have to choose a pattern.")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Warning)
                dlg.exec()
            print(f"Could not initialize signal navigation:\n{str(e)}\n")

    def selectDictionaryIndexingSetup(self):
        try:
            self.diSetup = DiSetupDialog(parent=self, pattern_path=self.file_selected)
            self.diSetup.show()
        except Exception as e:
            print(f"Could not initialize dictionary indexing:\n{str(e)}\n")

    def selectHoughIndexingSetup(self):
        try:
            self.hiSetup = HiSetupDialog(parent=self, pattern_path=self.file_selected)
            self.hiSetup.show()
        except Exception as e:
            print(f"Could not initialize hough indexing:\n{str(e)}\n")

    def selectPatternCenter(self):
        try:
            self.patternCenter = PatterCenterDialog(self.working_dir)
            self.patternCenter.show()
        except Exception as e:
            print(f"Could not initialize pattern center refinement:\n{str(e)}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = AppWindow()

    # Redirect stdout to console.write and stderr to console.errorwrite
    redirect = Redirect(appWindow.console.errorwrite)
    with redirect_stdout(appWindow.console), redirect_stderr(redirect):
        appWindow.show()
        print(
            f"Multithreading with maximum {appWindow.threadPool.maxThreadCount()} threads"
        )
        try:
            sys.exit(app.exec())
        except Exception as e:
            print(e)
            print("A clean exit was not performed")
