import gc
import os.path as path
import platform
import webbrowser
from typing import Optional, Sequence

try:
    from os import startfile
except:
    import subprocess

import kikuchipy as kp
from kikuchipy.signals.ebsd import EBSD, LazyEBSD
from orix import io
from orix.crystal_map import CrystalMap
from PySide6.QtCore import QDir, Qt, Signal
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFileSystemModel, QMenu, QMessageBox, QWidget

from ui.ui_system_explorer_widget import Ui_SystemExplorerWidget


class SystemExplorerWidget(QWidget):
    # TODO Load this from advanced_settings
    SYSTEM_VIEW_FILTER = (
        "*.h5",
        "*.dat",
        "*.ang",
        "*.jpg",
        "*.png",
        "*.txt",
    )
    KP_EXTENSIONS = (".h5", ".dat")
    IMAGE_EXTENSIONS = (".jpg", ".png", ".gif", ".bmp",)

    pathChanged = Signal(str)
    requestSignalNavigation = Signal(str)
    requestImageViewer = Signal(str)

    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_SystemExplorerWidget()
        self.ui.setupUi(self)
        self.app = self.window()

        self.systemModel = QFileSystemModel()
        self.selected_path = ""

        self.setupConnections()

    def setupConnections(self):
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.selectionModel().selectionChanged.connect(
            lambda new, old: self.onSystemModelChanged(new, old)
        )
        self.ui.systemViewer.doubleClicked.connect(lambda: self.doubleClickEvent())
        self.ui.systemViewer.setSortingEnabled(True)
        # self.ui.systemViewer. sortItems(column, order)
        self.ui.systemViewer.setCursor(Qt.PointingHandCursor)
        self.ui.systemViewer.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.systemViewer.customContextMenuRequested.connect(self.contextMenu)

    def setSystemViewer(
        self, working_dir: str, filters: Optional[Sequence[str]] = SYSTEM_VIEW_FILTER
    ):
        self.selected_path = ""
        self.systemModel.setRootPath(working_dir)
        self.systemModel.setNameFilters(filters)
        self.systemModel.setNameFilterDisables(0)
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.setRootIndex(self.systemModel.index(working_dir))
        self.ui.systemViewer.clearSelection()
        self.ui.systemViewer.setColumnWidth(0, 200)
        self.ui.systemViewer.hideColumn(2)
        self.ui.folderLabel.setText(path.basename(working_dir))
        self.app.setWindowTitle(f"EBSP Indexer - {working_dir}")

    def contextMenu(self):
        menu = QMenu()
        menu_path = self.selected_path
        menu.setCursor(Qt.PointingHandCursor)
        file = path.isfile(menu_path)
        directory = path.isdir(menu_path)
        if not (file or directory):
            revealAction = menu.addAction("Reveal in File Explorer")
            revealAction.triggered.connect(
                lambda: revealInExplorer(self.systemModel.rootPath())
            )
            cursor = QCursor()
            menu.exec(cursor.pos())
        ext = path.splitext(menu_path)[-1]
        # Kikuchipy available actions
        if ext in self.KP_EXTENSIONS:
            snAction = menu.addAction("Open in Signal Navigation")
            snAction.triggered.connect(
                lambda: self.requestSignalNavigation.emit(menu_path)
            )
            try:
                s_prew = kp.load(menu_path, lazy=True)
                if isinstance(s_prew, (EBSD, LazyEBSD)):
                    menu.addSeparator()
                    hiAction = menu.addAction("Hough Indexing")
                    diAction = menu.addAction("Dictionary Indexing")
                    # Replace these two with signals for more flexible implementation
                    hiAction.triggered.connect(
                        lambda: self.app.selectHoughIndexingSetup(menu_path)
                    )
                    diAction.triggered.connect(
                        lambda: self.app.selectDictionaryIndexingSetup(menu_path)
                    )
                del s_prew
                gc.collect()
            except:
                try:
                    xmap_prew = io.load(menu_path)
                    if isinstance(xmap_prew, CrystalMap):
                        menu.addSeparator()
                        refineAction = menu.addAction("Refine Orientations")
                        refineAction.triggered.connect(
                            lambda: self.app.selectRefineOrientations(menu_path)
                        )
                except Exception as e:
                    pass
        # Misc available actions
        elif ext in [".txt"]:
            txtAction = menu.addAction("Open Text")
            txtAction.triggered.connect(lambda: openTxtFile(menu_path))
        elif ext in self.IMAGE_EXTENSIONS:
            imageAction = menu.addAction("Open Image")
            imageAction.triggered.connect(lambda: self.requestImageViewer.emit(menu_path))

        # Globally available actions
        menu.addSeparator()
        revealAction = menu.addAction("Reveal in File Explorer")
        deleteAction = menu.addAction("Delete")
        revealAction.triggered.connect(
            lambda: revealInExplorer(self.selected_path)
        )
        deleteAction.triggered.connect(
            lambda: self.displayDeleteWarning(self.selected_path)
        )
        cursor = QCursor()
        menu.exec(cursor.pos())

    def displayDeleteWarning(self, deletion_path):
        reply = QMessageBox.question(
            self,
            f"Delete {path.basename(deletion_path)}",
            f"Are you sure you want to permentantly delete '{path.basename(deletion_path)}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,  # Default button
        )
        if reply == QMessageBox.Yes:
            self.deleteSelected(deletion_path)

    def deleteSelected(self, deletion_path):
        if path.isdir(deletion_path):
            result = self.systemModel.rmdir(self.ui.systemViewer.currentIndex())
            if not result:
                dir = QDir(deletion_path)
                dir.removeRecursively()
        elif path.isfile(deletion_path):
            result = self.systemModel.remove(self.ui.systemViewer.currentIndex())
        self.ui.systemViewer.selectionModel().clearCurrentIndex()

    def onSystemModelChanged(self, new_selected, old_selected):
        if new_selected == old_selected:
            return
        if new_selected.empty():
            self.selected_path = ""
        else:
            self.selected_path = self.systemModel.filePath(
                self.ui.systemViewer.currentIndex()
            )
        self.pathChanged.emit(self.selected_path)

    def doubleClickEvent(self):
        index = self.ui.systemViewer.currentIndex()
        self.selected_path = self.systemModel.filePath(index)
        ext = path.splitext(self.selected_path)[1]
        if ext in [".txt"]:
            if platform.system().lower() == "darwin":
                subprocess.call(["open", "-a", "TextEdit", self.selected_path])
            if platform.system().lower() == "windows":
                startfile(self.selected_path)
        # TODO: more functionality, open dataset for signal navigation
        elif ext in self.KP_EXTENSIONS:
            self.requestSignalNavigation.emit(self.selected_path)
        elif ext in self.IMAGE_EXTENSIONS:
            self.requestImageViewer.emit(self.selected_path)

def revealInExplorer(revealed_path):
    if path.isdir(revealed_path):
        webbrowser.open(revealed_path)
    elif path.isfile(revealed_path):
        webbrowser.open(path.dirname(revealed_path))
    else:
        webbrowser.open()

def openTxtFile(txt_path: str):
        if platform.system().lower() == "darwin":
            subprocess.call(["open", "-a", "TextEdit", txt_path])
        if platform.system().lower() == "windows":
            startfile(txt_path)