import sys
from os.path import join
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from ui.ui_main_window import Ui_MainWindow

from scripts.filebrowser import FileBrowser
from scripts.pattern_processing import background_processor


class Ui_MainWindow(QMainWindow):

    working_dir = ""

    def __init__(self) -> None:
        """
        Initializes the main window by loading the .ui file and initialize functionality
        """
        super(Ui_MainWindow, self).__init__()
        loadUi("ui/main_window.ui", self)
        self.showMaximized()
        self.file_browser = FileBrowser(FileBrowser.OpenDirectory)
        self.initFileBrowserPanel()
        self.initProcessingPanel()

    def initFileBrowserPanel(self):
        self.actionOpen_Workfolder.triggered.connect(
            lambda: self.selectWorkingDirectory()
        )

    def initProcessingPanel(self):
        self.actionProcessingMenu.triggered.connect(lambda: self.selectProcessing())

    def selectWorkingDirectory(self):
        self.file_browser.setMode(FileBrowser.OpenDirectory)
        self.file_browser.setFileFilter("All files (*.*)")
        if self.file_browser.getFile():
            self.working_dir = self.file_browser.getPaths()[0]
            self.file_browser.setDefaultDir(self.working_dir)
            labeltext = f"Path selected: {self.working_dir}"
            self.pathLabel.setText(labeltext)

    def selectProcessing(self):
        self.file_browser.setMode(FileBrowser.SaveFile)
        self.file_browser.setDefaultDir(self.working_dir)
        self.file_browser.setFileFilter("Hierarchical Data Format (*.h5);;EDAX (*.ang)")
        if self.file_browser.getFile():
            save_path = self.file_browser.getPaths()[0]
            processor = background_processor(self.working_dir)
            processor.remove_static()
            processor.remove_dynamic()
            processor.averaging()
            try:
                processor.save_to_file(join(self.working_dir, save_path))
            except:
                print("An exception occured")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())
