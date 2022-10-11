from os import path
from kikuchipy import load, filters
from PySide6.QtWidgets import QDialog

from scripts.filebrowser import FileBrowser
from ui.ui_pattern_center import Ui_PatternCenterDialog

class PatterCenterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PatternCenterDialog()
        self.ui.setupUi(self)
        self.setupConnections()


    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.function)