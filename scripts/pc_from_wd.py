import numpy as np
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from scipy.stats import linregress as linreg

from ui.ui_wd_calibration import Ui_WdCalDialog
from utils import FileBrowser, SettingFile


class wdCalibration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Dialog box ui setup
        self.ui = Ui_WdCalDialog()
        self.ui.setupUi(self)

        self.fileBrowserOD = FileBrowser(
            mode=FileBrowser.OpenFile,
            filter_name="*.txt",
        )
        self.setupConnections()
        self.checkValidInput()

        self.ui.pushButtonRemovePosition.setEnabled(False)

    def setupConnections(self):
        self.ui.pushButtonReadFromFile.clicked.connect(
            lambda: self.get_microscope_name()
        )
        self.ui.buttonBox.accepted.connect(lambda: self.run_calibration())

        self.ui.pushButtonAddPosition.clicked.connect(lambda: self.addRow())
        self.ui.pushButtonRemovePosition.clicked.connect(lambda: self.removeRow())

        self.ui.tableWidget.cellChanged.connect(lambda: self.checkValidInput())
        self.ui.lineEdit.textChanged.connect(lambda: self.checkValidInput())

    def get_microscope_name(self):
        if self.fileBrowserOD.getFile():
            setting_file_path = self.fileBrowserOD.getPaths()[0]
            N = 10
            microscope = {}
            try:
                with open(setting_file_path, "r") as f:
                    for _ in range(N):
                        item = next(f).strip().split("\t")
                        if item[0].lower() in ["manufacturer", "model"]:
                            microscope[item[0]] = item[1]
                microscope_name = microscope["Manufacturer"] + " " + microscope["Model"]
                self.ui.lineEdit.setText(microscope_name)
            except:
                QMessageBox(self).warning(
                    self,
                    "Could not set microscope name",
                    "The file does not contain the keys 'Manufacturer' and 'Model'",
                    QMessageBox.Ok,
                    QMessageBox.Ok,
                )
                return

    def addRow(self):
        rows = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rows)
        labels = [f"Position {i}" for i in range(1, rows + 2)]
        self.ui.tableWidget.setVerticalHeaderLabels(labels)

        if self.ui.tableWidget.rowCount() > 2:
            self.ui.pushButtonRemovePosition.setEnabled(True)

    def removeRow(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

        if self.ui.tableWidget.rowCount() <= 2:
            self.ui.pushButtonRemovePosition.setEnabled(False)

    def checkValidInput(self):
        columns = self.ui.tableWidget.columnCount()
        rows = self.ui.tableWidget.rowCount()
        checksum = columns * rows
        for column in range(self.ui.tableWidget.columnCount()):
            col = []
            for row in range(self.ui.tableWidget.rowCount()):
                try:
                    float(self.ui.tableWidget.item(row, column).text())
                    col.append(float(self.ui.tableWidget.item(row, column).text()))
                except:
                    checksum -= 1
            if column == 0 and len(col) > len(set(col)):
                checksum -= 1

        if checksum == columns * rows:
            self.ui.labelValidInput.setStyleSheet("QLabel{color:green}")
            self.ui.labelValidInput.setText("Valid input.")

        else:
            self.ui.labelValidInput.setStyleSheet("QLabel{color:red}")
            self.ui.labelValidInput.setText("Invalid input.")

        if checksum == columns * rows and self.ui.lineEdit.text():
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setToolTip(
                "Save microscope calibration."
            )
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setToolTip(
                "Missing valid microscope name and/or calibration values."
            )

    def run_calibration(self):
        self.setting_file = SettingFile("advanced_settings.txt")
        self.microscope_name = self.ui.lineEdit.text()
        calibration_values = [[], [], [], []]

        columns = self.ui.tableWidget.columnCount()
        rows = self.ui.tableWidget.rowCount()
        for column in range(columns):
            for row in range(rows):
                calibration_values[column].append(
                    float(self.ui.tableWidget.item(row, column).text())
                )

        x_slope, x_intersept, *_ = linreg(calibration_values[0], calibration_values[1])
        y_slope, y_intersept, *_ = linreg(calibration_values[0], calibration_values[2])
        z_slope, z_intersept, *_ = linreg(calibration_values[0], calibration_values[3])

        self.pc_curve = (
            (round(x_slope, 5), round(x_intersept, 5)),
            (round(y_slope, 5), round(y_intersept, 5)),
            (round(z_slope, 5), round(z_intersept, 5)),
        )


def pc_from_wd(microscope: str, working_distance: float, convention="TSL"):
    """
    Returns pattern center depending microscope, calculated from linear regression of PC's from different working distances.

    If no microsope configuration is found, return (0.5, 0.8, 0.5) TSL
    """
    setting_file = SettingFile("advanced_settings.txt")
    wd = float(working_distance)

    try:
        pc_curve = np.array(eval(setting_file.read(microscope)))
        pc = []
        for i in range(3):
            pc.append(pc_curve[i][0] * wd + pc_curve[i][1])
    except:
        pc = np.array([0.5000, 0.8000, 0.5000])

    if convention == "BRUKER":
        pc[1] = 1 - pc[1]

    return pc
