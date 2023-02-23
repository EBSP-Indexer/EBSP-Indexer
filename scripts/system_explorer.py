import platform
import os.path as path
import webbrowser
from typing import Optional, Sequence
try:
    from os import startfile
except:
    import subprocess

from PySide6.QtCore import Qt, Signal, QDir
from PySide6.QtWidgets import QWidget, QFileSystemModel, QMessageBox, QMenu
from PySide6.QtGui import QCursor

from ui.ui_system_explorer_widget import Ui_SystemExplorerWidget
from scripts.advanced_settings import AdvancedSettingsDialog

#TODO Load this from advanced_settings

class SystemExplorerWidget(QWidget):

    SYSTEM_VIEW_FILTER = (
        "*.h5",
        "*.dat",
        "*.ang",
        "*.jpg",
        "*.png",
        "*.txt",
    )
    KP_EXTENSIONS = (".h5", ".dat")

    pathChangedSignal = Signal(str)
    selected_path = ""

    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_SystemExplorerWidget()
        self.ui.setupUi(self)
        self.app = self.window()

        self.systemModel = QFileSystemModel()

        self.setupConnections()

    def setupConnections(self):
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.selectionModel().selectionChanged.connect(
            lambda new, old: self.onSystemModelChanged(new, old)
        )
        self.ui.systemViewer.doubleClicked.connect(lambda: self.openTextFile())
        self.ui.systemViewer.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.systemViewer.customContextMenuRequested.connect(self.contextMenu)

    def setSystemViewer(self, working_dir: str, filters : Optional[Sequence[str]] = SYSTEM_VIEW_FILTER):
        self.selected_path = ""
        self.systemModel.setRootPath(working_dir)
        self.systemModel.setNameFilters(filters)
        self.systemModel.setNameFilterDisables(0)
        self.ui.systemViewer.setModel(self.systemModel)
        self.ui.systemViewer.setRootIndex(self.systemModel.index(working_dir))
        self.ui.systemViewer.setColumnWidth(0, 250)
        self.ui.systemViewer.hideColumn(2)
        self.ui.folderLabel.setText(path.basename(working_dir))

    def contextMenu(self):
        menu = QMenu()
        # Kikuchipy available actions
        if path.isfile(self.selected_path) and path.splitext(self.selected_path)[-1] in self.KP_EXTENSIONS:
            hiAction = menu.addAction("Index with HI")
            diAction = menu.addAction("Index with DI")
            hiAction.triggered.connect(lambda: self.app.selectHoughIndexingSetup(self.selected_path))
            diAction.triggered.connect(lambda: self.app.selectDictionaryIndexingSetup(self.selected_path))
        # Globally available actions
        menu.addSeparator()
        revealAction = menu.addAction("Reveal in File Explorer")
        deleteAction = menu.addAction("Delete")
        revealAction.triggered.connect(self.revealInExplorer)
        deleteAction.triggered.connect(self.displayDeleteWarning)
        
        cursor = QCursor()
        menu.exec(cursor.pos())

    def revealInExplorer(self):
        if path.isdir(self.selected_path):
            webbrowser.open(self.selected_path)
        elif path.isfile(self.selected_path):
            webbrowser.open(path.dirname(self.selected_path))
    
    def displayDeleteWarning(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("EBSD-GUI Delete Information")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Are you sure you want to permentantly delete '{path.basename(self.selected_path)}'?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.accepted.connect(self.deleteSelected)
        msg.exec()

    def deleteSelected(self):
        if path.isdir(self.selected_path):
            result = self.systemModel.rmdir(self.ui.systemViewer.currentIndex())
            if not result:
                dir = QDir(self.selected_path)
                dir.removeRecursively()
        elif path.isfile(self.selected_path):
            result = self.systemModel.remove(self.ui.systemViewer.currentIndex())
        self.ui.systemViewer.selectionModel().clearCurrentIndex()

    def onSystemModelChanged(self, new_selected, old_selected):
        if new_selected.empty():
            self.selected_path = ""
        else:
            self.selected_path = self.systemModel.filePath(
                self.ui.systemViewer.currentIndex()
            )
        self.pathChangedSignal.emit(self.selected_path)

    def openTextFile(self):
        index = self.ui.systemViewer.currentIndex()
        self.selected_path = self.systemModel.filePath(index)

        if path.splitext(self.selected_path)[1] in [".txt"]:
            if platform.system().lower() == "darwin":
                subprocess.call(["open", "-a", "TextEdit", self.selected_path])
            if platform.system().lower() == "windows":
                startfile(self.selected_path)