from PyQt6.QtCore import QDir
from PyQt6.QtWidgets import QWidget, QFileDialog

import sys

# sourcecode: https://www.fundza.com/pyqt_pyside2/pyqt5_file_browser/index.html


class FileBrowser(QWidget):

    OpenFile = 0
    OpenFiles = 1
    OpenDirectory = 2
    SaveFile = 3

    def __init__(self, mode=OpenFile):
        QWidget.__init__(self)
        self.browser_mode = mode
        self.filter_name = "All files (*.*)"
        self.dirpath = QDir.currentPath()

    def setMode(self, browser_mode):
        self.browser_mode = browser_mode

    def setFileFilter(self, text):
        self.filter_name = text

    def setDefaultDir(self, path):
        self.dirpath = path

    def getFile(self) -> int:
        """
        Method returns 1 if one or more paths are set. Abort/ cancel returns 0
        """
        self.filepaths = []
        if self.browser_mode == FileBrowser.OpenFile:
            self.filepaths.append(
                QFileDialog.getOpenFileName(
                    self,
                    caption="Choose File",
                    directory=self.dirpath,
                    filter=self.filter_name,
                )[0]
            )
        elif self.browser_mode == FileBrowser.OpenFiles:
            self.filepaths.extend(
                QFileDialog.getOpenFileNames(
                    self,
                    caption="Choose Files",
                    directory=self.dirpath,
                    filter=self.filter_name,
                )[0]
            )
        elif self.browser_mode == FileBrowser.OpenDirectory:
            self.filepaths.append(
                QFileDialog.getExistingDirectory(
                    self, caption="Choose Directory", directory=self.dirpath
                )
            )
        elif self.browser_mode == FileBrowser.SaveFile:
            options = QFileDialog.options(QFileDialog())
            if sys.platform == "darwin":
                options |= QFileDialog.DontUseNativeDialog
            self.filepaths.append(
                QFileDialog.getSaveFileName(
                    self,
                    caption="Save/Save As",
                    directory=self.dirpath,
                    filter=self.filter_name,
                    options=options,
                )[0]
            )
        if self.filepaths[0] == '':
            return 0
        return 1 

    def getPaths(self):
        return self.filepaths
