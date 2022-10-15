import sys
from os.path import basename
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from ui.ui_main_window import Ui_MainWindow

from scripts.filebrowser import FileBrowser
from scripts.pattern_processing import PatternProcessingDialog
from scripts.signal_navigation import SignalNavigation
from scripts.dictionary_indexing import DiSetupDialog
from scripts.interpreter import ConsoleWidget
from scripts.pattern_center import PatterCenterDialog

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

        self.fileBrowserOD = FileBrowser(FileBrowser.OpenDirectory)
        self.systemModel = QFileSystemModel()

        variables = globals()   #TEMPERORY!!!: accessing variables in different thread may lead to crash
        self.console = ConsoleWidget(self.ui, variables)

    def setupConnections(self):
        self.ui.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )
        self.ui.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())
        self.ui.systemViewer.clicked.connect(
            lambda index: self.onSystemViewClicked(index)
        )
        self.ui.actionSignalNavigation.triggered.connect(lambda: self.selectSignalNavigation())
        self.ui.actionDictinary_indexing_setup.triggered.connect(lambda: self.selectDictionaryIndexingSetup())
        self.ui.actionPattern_Center.triggered.connect(lambda: self.selectPatternCenter())

    def selectWorkingDirectory(self):
        if self.fileBrowserOD.getFile():
            self.working_dir = self.fileBrowserOD.getPaths()[0]
            self.file_selected = None
            self.fileBrowserOD.setDefaultDir(self.working_dir)

            # Setting the system viewer
            self.systemModel.setRootPath(self.working_dir)
            self.systemModel.setNameFilters(["*.h5","*.dat"])
            self.systemModel.setNameFilterDisables(0)
            self.ui.systemViewer.setModel(self.systemModel)
            self.ui.systemViewer.setRootIndex(self.systemModel.index(self.working_dir))
            self.ui.systemViewer.setColumnWidth(0, 250)
            self.ui.systemViewer.hideColumn(2)

            self.ui.folderLabel.setText(basename(self.working_dir))
            self.setWindowTitle(f"EBSD-GUI - {self.working_dir}")

    def selectProcessing(self):
        try:
            self.processingDialog = PatternProcessingDialog(self.working_dir, pattern_path=self.file_selected)
            self.processingDialog.show()
        except Exception as e:
            self.console.send_console_log(f"Could not initialize processing dialog:\n{str(e)}\n")

    def onSystemViewClicked(self, index):
        self.file_selected = self.systemModel.filePath(index)

    def selectSignalNavigation(self):
        try:
            self.signalNavigation = SignalNavigation(file_path=self.file_selected)
        except Exception as e:
            self.console.send_console_log(f"Could not initialize signal navigation:\n{str(e)}\n")

    def selectDictionaryIndexingSetup(self):
        try:
            self.diSetup = DiSetupDialog(self.working_dir, pattern_path=self.file_selected)
            self.diSetup.show()
        except Exception as e:
            self.console.send_console_log(f"Could not initialize dictionary indexing:\n{str(e)}\n")
            print(e)
            print("Could not initialize dictionary indexing")
            
    def selectPatternCenter(self):
        try:
            self.patternCenter = PatterCenterDialog()
            self.patternCenter.show()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appWindow = AppWindow()
    appWindow.show()
    try:
        sys.exit(app.exec())
    except Exception as e:
        print(e)
        print("A clean exit was not performed")
