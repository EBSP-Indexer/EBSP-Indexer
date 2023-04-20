# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_phase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_NewPhaseDialog(object):
    def setupUi(self, NewPhaseDialog):
        if not NewPhaseDialog.objectName():
            NewPhaseDialog.setObjectName(u"NewPhaseDialog")
        NewPhaseDialog.resize(861, 445)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewPhaseDialog.sizePolicy().hasHeightForWidth())
        NewPhaseDialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(NewPhaseDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonBox = QDialogButtonBox(NewPhaseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.labelName = QLabel(NewPhaseDialog)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.labelSpaceGroup = QLabel(NewPhaseDialog)
        self.labelSpaceGroup.setObjectName(u"labelSpaceGroup")

        self.gridLayout.addWidget(self.labelSpaceGroup, 1, 0, 1, 1)

        self.lineName = QLineEdit(NewPhaseDialog)
        self.lineName.setObjectName(u"lineName")

        self.gridLayout.addWidget(self.lineName, 0, 2, 1, 1)

        self.lineSpaceGroup = QLineEdit(NewPhaseDialog)
        self.lineSpaceGroup.setObjectName(u"lineSpaceGroup")

        self.gridLayout.addWidget(self.lineSpaceGroup, 1, 2, 1, 1)

        self.label_2 = QLabel(NewPhaseDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.labelColor = QLabel(NewPhaseDialog)
        self.labelColor.setObjectName(u"labelColor")

        self.gridLayout.addWidget(self.labelColor, 2, 0, 1, 1)

        self.label = QLabel(NewPhaseDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBoxStructure = QCheckBox(NewPhaseDialog)
        self.checkBoxStructure.setObjectName(u"checkBoxStructure")

        self.horizontalLayout_3.addWidget(self.checkBoxStructure)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.labelAtoms = QLabel(NewPhaseDialog)
        self.labelAtoms.setObjectName(u"labelAtoms")
        self.labelAtoms.setEnabled(False)

        self.verticalLayout_2.addWidget(self.labelAtoms)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonAddAtom = QPushButton(NewPhaseDialog)
        self.pushButtonAddAtom.setObjectName(u"pushButtonAddAtom")
        self.pushButtonAddAtom.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pushButtonAddAtom)

        self.pushButtonRemoveAtom = QPushButton(NewPhaseDialog)
        self.pushButtonRemoveAtom.setObjectName(u"pushButtonRemoveAtom")
        self.pushButtonRemoveAtom.setEnabled(False)

        self.verticalLayout_3.addWidget(self.pushButtonRemoveAtom)

        self.verticalSpacerMenuAtom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacerMenuAtom)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.tableWidgetAtoms = QTableWidget(NewPhaseDialog)
        if (self.tableWidgetAtoms.columnCount() < 5):
            self.tableWidgetAtoms.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetAtoms.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetAtoms.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetAtoms.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetAtoms.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetAtoms.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidgetAtoms.rowCount() < 1):
            self.tableWidgetAtoms.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetAtoms.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetAtoms.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetAtoms.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetAtoms.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetAtoms.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetAtoms.setItem(0, 4, __qtablewidgetitem10)
        self.tableWidgetAtoms.setObjectName(u"tableWidgetAtoms")
        self.tableWidgetAtoms.setEnabled(False)
        self.tableWidgetAtoms.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetAtoms.horizontalHeader().setDefaultSectionSize(85)
        self.tableWidgetAtoms.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetAtoms.verticalHeader().setVisible(True)
        self.tableWidgetAtoms.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tableWidgetAtoms)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.labelLattice = QLabel(NewPhaseDialog)
        self.labelLattice.setObjectName(u"labelLattice")
        self.labelLattice.setEnabled(False)

        self.verticalLayout_2.addWidget(self.labelLattice)

        self.tableWidgetLattice = QTableWidget(NewPhaseDialog)
        if (self.tableWidgetLattice.columnCount() < 6):
            self.tableWidgetLattice.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidgetLattice.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        if (self.tableWidgetLattice.rowCount() < 1):
            self.tableWidgetLattice.setRowCount(1)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidgetLattice.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidgetLattice.setItem(0, 5, __qtablewidgetitem23)
        self.tableWidgetLattice.setObjectName(u"tableWidgetLattice")
        self.tableWidgetLattice.setEnabled(False)
        self.tableWidgetLattice.setMaximumSize(QSize(16777215, 70))
        self.tableWidgetLattice.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidgetLattice.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidgetLattice.horizontalHeader().setStretchLastSection(False)
        self.tableWidgetLattice.verticalHeader().setVisible(False)
        self.tableWidgetLattice.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidgetLattice)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)

        self.lineColor = QLineEdit(NewPhaseDialog)
        self.lineColor.setObjectName(u"lineColor")

        self.gridLayout.addWidget(self.lineColor, 2, 2, 1, 1)

        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.labelMessage = QLabel(NewPhaseDialog)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_11.addWidget(self.labelMessage)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineName, self.lineSpaceGroup)
        QWidget.setTabOrder(self.lineSpaceGroup, self.lineColor)
        QWidget.setTabOrder(self.lineColor, self.checkBoxStructure)
        QWidget.setTabOrder(self.checkBoxStructure, self.pushButtonAddAtom)
        QWidget.setTabOrder(self.pushButtonAddAtom, self.pushButtonRemoveAtom)
        QWidget.setTabOrder(self.pushButtonRemoveAtom, self.tableWidgetAtoms)
        QWidget.setTabOrder(self.tableWidgetAtoms, self.tableWidgetLattice)

        self.retranslateUi(NewPhaseDialog)
        self.buttonBox.rejected.connect(NewPhaseDialog.reject)
        self.checkBoxStructure.toggled.connect(self.tableWidgetAtoms.setEnabled)
        self.checkBoxStructure.toggled.connect(self.labelAtoms.setEnabled)
        self.checkBoxStructure.toggled.connect(self.labelLattice.setEnabled)
        self.checkBoxStructure.toggled.connect(self.pushButtonAddAtom.setEnabled)
        self.checkBoxStructure.toggled.connect(self.pushButtonRemoveAtom.setEnabled)
        self.checkBoxStructure.toggled.connect(self.tableWidgetLattice.setEnabled)

        QMetaObject.connectSlotsByName(NewPhaseDialog)
    # setupUi

    def retranslateUi(self, NewPhaseDialog):
        NewPhaseDialog.setWindowTitle(QCoreApplication.translate("NewPhaseDialog", u"Create Phase", None))
        self.labelName.setText(QCoreApplication.translate("NewPhaseDialog", u"Name*", None))
        self.labelSpaceGroup.setText(QCoreApplication.translate("NewPhaseDialog", u"Space Group Number*", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. al or aluminium", None))
        self.lineSpaceGroup.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. 225 ", None))
        self.label_2.setText("")
        self.labelColor.setText(QCoreApplication.translate("NewPhaseDialog", u"Color", None))
        self.label.setText(QCoreApplication.translate("NewPhaseDialog", u"Structure", None))
        self.checkBoxStructure.setText(QCoreApplication.translate("NewPhaseDialog", u"Define Custom Structure", None))
#if QT_CONFIG(tooltip)
        self.labelAtoms.setToolTip(QCoreApplication.translate("NewPhaseDialog", u"<html><head/><body><p>Storage of structure information relevant for a single atom, Element is the symbol of the element (e.g. Ni for Nickel), X,Y,Z are fractional coordinates within the associated lattice (e.g. 0,0,0)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelAtoms.setText(QCoreApplication.translate("NewPhaseDialog", u"Atoms*", None))
        self.pushButtonAddAtom.setText(QCoreApplication.translate("NewPhaseDialog", u"Add", None))
        self.pushButtonRemoveAtom.setText(QCoreApplication.translate("NewPhaseDialog", u"Remove", None))
        ___qtablewidgetitem = self.tableWidgetAtoms.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewPhaseDialog", u"Element", None));
        ___qtablewidgetitem1 = self.tableWidgetAtoms.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewPhaseDialog", u"X", None));
        ___qtablewidgetitem2 = self.tableWidgetAtoms.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewPhaseDialog", u"Y", None));
        ___qtablewidgetitem3 = self.tableWidgetAtoms.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewPhaseDialog", u"Z", None));
        ___qtablewidgetitem4 = self.tableWidgetAtoms.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewPhaseDialog", u"Occupancy", None));
        ___qtablewidgetitem5 = self.tableWidgetAtoms.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NewPhaseDialog", u"Atom 1", None));

        __sortingEnabled = self.tableWidgetAtoms.isSortingEnabled()
        self.tableWidgetAtoms.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidgetAtoms.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("NewPhaseDialog", u"0", None));
        ___qtablewidgetitem7 = self.tableWidgetAtoms.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("NewPhaseDialog", u"0", None));
        ___qtablewidgetitem8 = self.tableWidgetAtoms.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("NewPhaseDialog", u"0", None));
        ___qtablewidgetitem9 = self.tableWidgetAtoms.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("NewPhaseDialog", u"1", None));
        self.tableWidgetAtoms.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.labelLattice.setToolTip(QCoreApplication.translate("NewPhaseDialog", u"<html><head/><body><p>Create coordinate system with the cell lengths a, b, c and cell angles alpha, beta, gamma in degrees</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelLattice.setText(QCoreApplication.translate("NewPhaseDialog", u"Lattice*", None))
        ___qtablewidgetitem10 = self.tableWidgetLattice.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("NewPhaseDialog", u"a", None));
        ___qtablewidgetitem11 = self.tableWidgetLattice.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("NewPhaseDialog", u"b", None));
        ___qtablewidgetitem12 = self.tableWidgetLattice.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("NewPhaseDialog", u"c", None));
        ___qtablewidgetitem13 = self.tableWidgetLattice.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("NewPhaseDialog", u"\u03b1", None));
        ___qtablewidgetitem14 = self.tableWidgetLattice.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("NewPhaseDialog", u"\u03b2", None));
        ___qtablewidgetitem15 = self.tableWidgetLattice.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("NewPhaseDialog", u"\u03b3", None));

        __sortingEnabled1 = self.tableWidgetLattice.isSortingEnabled()
        self.tableWidgetLattice.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.tableWidgetLattice.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("NewPhaseDialog", u"1", None));
        ___qtablewidgetitem17 = self.tableWidgetLattice.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("NewPhaseDialog", u"1", None));
        ___qtablewidgetitem18 = self.tableWidgetLattice.item(0, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("NewPhaseDialog", u"1", None));
        ___qtablewidgetitem19 = self.tableWidgetLattice.item(0, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("NewPhaseDialog", u"90", None));
        ___qtablewidgetitem20 = self.tableWidgetLattice.item(0, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("NewPhaseDialog", u"90", None));
        ___qtablewidgetitem21 = self.tableWidgetLattice.item(0, 5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("NewPhaseDialog", u"90", None));
        self.tableWidgetLattice.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.tableWidgetLattice.setToolTip(QCoreApplication.translate("NewPhaseDialog", u"<html><head/><body><p>Create coordinate system with the cell lengths a, b, c and cell angles alpha, beta, gamma in degrees</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineColor.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. blue", None))
        self.labelMessage.setText(QCoreApplication.translate("NewPhaseDialog", u"*Message", None))
    # retranslateUi

