import kikuchipy as kp
import hyperspy as hp
import pyebsdindex
import orix 
import diffpy.structure
import diffsims

from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.ui_about import Ui_AboutDialog

DEPENDENCIES = {
        "kikuchipy": kp.__version__,
        "PyEBSDIndex": pyebsdindex.__version__,
        "orix": orix.__version__,
        "diffpy.structure": diffpy.structure.__version__,
        "diffsims": diffsims.__version__,
        "HyperSpy": hp.__version__
    }

VERSION_TAG = "v0.2.0"


class AboutDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.setCurrentVersion()
        self.populateVersionTable()

    def setCurrentVersion(self):
        self.ui.softwareVersionLabel.setText(f"EBSP Indexer - {VERSION_TAG}")    

    def populateVersionTable(self):
        table = self.ui.dependenciesTableWidget
        
        table.setRowCount(len(DEPENDENCIES.items()))
        row = 0
        for name, version in DEPENDENCIES.items():
            name_item = QTableWidgetItem(str(name))
            version_item = QTableWidgetItem(str(version))
            table.setItem(row, 0, name_item)
            table.setItem(row, 1, version_item)
            row += 1