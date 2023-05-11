# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wd_calibration.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_WdCalDialog(object):
    def setupUi(self, WdCalDialog):
        if not WdCalDialog.objectName():
            WdCalDialog.setObjectName(u"WdCalDialog")
        WdCalDialog.resize(484, 290)
        self.gridLayout = QGridLayout(WdCalDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(WdCalDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(WdCalDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButtonReadFromFile = QPushButton(WdCalDialog)
        self.pushButtonReadFromFile.setObjectName(u"pushButtonReadFromFile")

        self.horizontalLayout.addWidget(self.pushButtonReadFromFile)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.tableWidget = QTableWidget(WdCalDialog)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(400, 80))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonAddPosition = QPushButton(WdCalDialog)
        self.pushButtonAddPosition.setObjectName(u"pushButtonAddPosition")

        self.horizontalLayout_2.addWidget(self.pushButtonAddPosition)

        self.pushButtonRemovePosition = QPushButton(WdCalDialog)
        self.pushButtonRemovePosition.setObjectName(u"pushButtonRemovePosition")

        self.horizontalLayout_2.addWidget(self.pushButtonRemovePosition)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(WdCalDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.labelValidInput = QLabel(WdCalDialog)
        self.labelValidInput.setObjectName(u"labelValidInput")
        self.labelValidInput.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.labelValidInput, 2, 1, 1, 1)


        self.retranslateUi(WdCalDialog)
        self.buttonBox.accepted.connect(WdCalDialog.accept)
        self.buttonBox.rejected.connect(WdCalDialog.reject)

        QMetaObject.connectSlotsByName(WdCalDialog)
    # setupUi

    def retranslateUi(self, WdCalDialog):
        WdCalDialog.setWindowTitle(QCoreApplication.translate("WdCalDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("WdCalDialog", u"Microscope name", None))
        self.pushButtonReadFromFile.setText(QCoreApplication.translate("WdCalDialog", u"Import from setting file", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WdCalDialog", u"WD [mm]", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("WdCalDialog", u"Working distance in mm", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WdCalDialog", u"x", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WdCalDialog", u"y", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WdCalDialog", u"z", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WdCalDialog", u"Postion 1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WdCalDialog", u"Position 2", None));
        self.pushButtonAddPosition.setText(QCoreApplication.translate("WdCalDialog", u"Add position", None))
        self.pushButtonRemovePosition.setText(QCoreApplication.translate("WdCalDialog", u"Remove position", None))
        self.labelValidInput.setText(QCoreApplication.translate("WdCalDialog", u"Invalid input.", None))
    # retranslateUi

