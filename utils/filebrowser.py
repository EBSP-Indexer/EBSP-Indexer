import os
import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileDialog, QWidget


class FileBrowser(QWidget):
    OpenFile = 0
    OpenFiles = 1
    OpenDirectory = 2
    SaveFile = 3

    def __init__(
        self, mode=OpenFile, dirpath=QDir.currentPath(), filter_name="All files (*.*)"
    ):
        QWidget.__init__(self)
        self.browser_mode = mode
        if os.path.exists(dirpath):
            self.dirpath = dirpath
        else:
            self.dirpath = QDir.currentPath()
        self.filter_name = filter_name

    def setMode(self, browser_mode):
        self.browser_mode = browser_mode

    def setFileFilter(self, text):
        self.filter_name = text

    def setDefaultDir(self, path):
        if os.path.exists(path):
            self.dirpath = path

    def getFile(self) -> int:
        """
        Method returns 1 if one or more paths are set. Abort/ cancel returns 0
        """
        self.filepaths: list[str] = []
        if self.browser_mode == FileBrowser.OpenFile:
            self.filepaths.append(
                QFileDialog.getOpenFileName(
                    self,
                    caption="Choose File",
                    dir=self.dirpath,
                    filter=self.filter_name,
                )[0]
            )
        elif self.browser_mode == FileBrowser.OpenFiles:
            self.filepaths.extend(
                QFileDialog.getOpenFileNames(
                    self,
                    caption="Choose Files",
                    dir=self.dirpath,
                    filter=self.filter_name,
                )[0]
            )
        elif self.browser_mode == FileBrowser.OpenDirectory:
            self.filepaths.append(
                QFileDialog.getExistingDirectory(
                    self, caption="Choose Directory", dir=self.dirpath
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
                    dir=self.dirpath,
                    filter=self.filter_name,
                    options=options,
                )[0]
            )
        if not len(self.filepaths) or False in (len(path) for path in self.filepaths):
            return 0
        return 1

    def getPaths(self) -> list[str]:
        return self.filepaths
