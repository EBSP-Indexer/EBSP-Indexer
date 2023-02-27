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

    pathChanged = Signal(str)
    requestSignalNavigation = Signal(str)

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
        menu_path = self.selected_path
        file = path.isfile(menu_path)
        ext = path.splitext(menu_path)[-1]
        # Kikuchipy available actions
        if file and ext in self.KP_EXTENSIONS:
            snAction = menu.addAction("Open in Signal Navigation")
            snAction.triggered.connect(lambda: self.requestSignalNavigation.emit(menu_path))
            menu.addSeparator()
            hiAction = menu.addAction("Index with HI")
            diAction = menu.addAction("Index with DI")
            # Replace these two with signals for more flexible implementation
            hiAction.triggered.connect(lambda: self.app.selectHoughIndexingSetup(menu_path))
            diAction.triggered.connect(lambda: self.app.selectDictionaryIndexingSetup(menu_path))
        # Misc available actions
        elif file and ext in [".txt"]:
            txtAction = menu.addAction("Open")
            txtAction.triggered.connect(lambda: self.openTxtFile(menu_path))
            
        # Globally available actions
        menu.addSeparator()
        revealAction = menu.addAction("Reveal in File Explorer")
        deleteAction = menu.addAction("Delete")
        revealAction.triggered.connect(lambda: self.revealInExplorer(self.selected_path))
        deleteAction.triggered.connect(lambda: self.displayDeleteWarning(self.selected_path))
        
        cursor = QCursor()
        menu.exec(cursor.pos())

    def openTxtFile(self, txt_path: str):
        if platform.system().lower() == "darwin":
                subprocess.call(["open", "-a", "TextEdit", txt_path])
        if platform.system().lower() == "windows":
            startfile(txt_path)

    def revealInExplorer(self, revealed_path):
        if path.isdir(revealed_path):
            webbrowser.open(revealed_path)
        elif path.isfile(revealed_path):
            webbrowser.open(path.dirname(revealed_path))
    
    def displayDeleteWarning(self, deletion_path):
        msg = QMessageBox(self)
        msg.setWindowTitle("EBSD-GUI Delete Information")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Are you sure you want to permentantly delete '{path.basename(deletion_path)}'?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.accepted.connect(lambda: self.deleteSelected(deletion_path))
        msg.exec()

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
        if path.splitext(self.selected_path)[1] in [".txt"]:
            if platform.system().lower() == "darwin":
                subprocess.call(["open", "-a", "TextEdit", self.selected_path])
            if platform.system().lower() == "windows":
                startfile(self.selected_path)
        # TODO: more functionality, open dataset for signal navigation
        if path.splitext(self.selected_path)[1] in self.KP_EXTENSIONS:
            self.requestSignalNavigation.emit(self.selected_path)