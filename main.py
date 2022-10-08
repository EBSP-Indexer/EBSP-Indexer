import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.ui_main_window import Ui_MainWindow

from scripts.filebrowser import FileBrowser
from scripts.pattern_processing import PatternProcessingDialog


class AppWindow(QMainWindow):
    """
    The main app window that is present at all times
    """

    working_dir = ""

    def __init__(self) -> None:
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.fileBrowser = FileBrowser(FileBrowser.OpenDirectory)
        self.setupConnections()

    def setupConnections(self):
        self.ui.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )
        self.ui.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())

    def selectWorkingDirectory(self):
        if self.fileBrowser.getFile():
            self.working_dir = self.fileBrowser.getPaths()[0]
            self.fileBrowser.setDefaultDir(self.working_dir)
            self.setWindowTitle(f"EBSD-GUI - {self.working_dir}")

    def selectProcessing(self):
        #try:
        self.processingDialog = PatternProcessingDialog(self.working_dir)
        self.processingDialog.show()
        #except Exception as e:
        #    print(e)
        #    print("Could not initialize processing dialog")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec())
