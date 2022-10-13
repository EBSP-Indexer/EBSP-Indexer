from os import path
from kikuchipy import load, filters
from PySide6.QtWidgets import QDialog

from scripts.filebrowser import FileBrowser
from ui.ui_pattern_center import Ui_PatternCenterDialog

from mplwidget import MplWidget

class PatterCenterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PatternCenterDialog()
        self.ui.setupUi(self)
        self.setupConnections()


    def setupConnections(self):
        self.ui.buttonBox.accepted.connect(lambda: self.function)
        self.ui.buttonTune.clicked.connect(self.plot_data)
        
    def plot_data(self):
        self.plotWidget.canvas.ax.plot([0,1,2,3,4,5], [10,1,20,4,7,4])
        self.plotWidget.canvas.draw()
