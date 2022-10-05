import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from filebrowser import FileBrowser

class Ui_MainWindow(QMainWindow):

    working_dir = ""

    def __init__(self) -> None:
        """
        Initializes the main window by loading the .ui file and initialize functionality
        """
        super(Ui_MainWindow, self).__init__()
        loadUi("designer/main_window.ui", self)
        self.showMaximized()
        self.initFileBrowserPanel()

    def initFileBrowserPanel(self):
        self.dirFB = FileBrowser(FileBrowser.OpenDirectory)
        self.actionOpen_Workfolder.triggered.connect(lambda: self.selectWorkingDirectory())

    def selectWorkingDirectory(self):
        self.dirFB.getFile()
        if self.dirFB.getPaths()[0] != "":
            self.working_dir = self.dirFB.getPaths()[0]
            labeltext = f"Path selected: {self.working_dir}"
            self.pathLabel.setText(labeltext)
            self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec_())