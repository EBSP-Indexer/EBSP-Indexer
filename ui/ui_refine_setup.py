# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'refine_setup.ui'
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
    QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_RefineSetupDialog(object):
    def setupUi(self, RefineSetupDialog):
        if not RefineSetupDialog.objectName():
            RefineSetupDialog.setObjectName(u"RefineSetupDialog")
        RefineSetupDialog.resize(727, 680)
        self.gridLayout = QGridLayout(RefineSetupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(RefineSetupDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBoxLazy = QCheckBox(self.frame)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxLazy.setCheckable(True)
        self.checkBoxLazy.setChecked(True)
        self.checkBoxLazy.setTristate(False)

        self.verticalLayout_4.addWidget(self.checkBoxLazy)

        self.checkBoxMask = QCheckBox(self.frame)
        self.checkBoxMask.setObjectName(u"checkBoxMask")

        self.verticalLayout_4.addWidget(self.checkBoxMask)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.comboBoxBinning = QComboBox(self.frame)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")
        self.comboBoxBinning.setMaximumSize(QSize(80, 16777215))
        self.comboBoxBinning.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.comboBoxBinning)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.labelSignalShape = QLabel(self.frame)
        self.labelSignalShape.setObjectName(u"labelSignalShape")

        self.horizontalLayout_2.addWidget(self.labelSignalShape)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_15)

        self.spinBoxEnergy = QSpinBox(self.frame)
        self.spinBoxEnergy.setObjectName(u"spinBoxEnergy")
        self.spinBoxEnergy.setMaximumSize(QSize(50, 16777215))
        self.spinBoxEnergy.setMinimum(1)
        self.spinBoxEnergy.setMaximum(30)
        self.spinBoxEnergy.setValue(20)

        self.verticalLayout.addWidget(self.spinBoxEnergy)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_8)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_11)

        self.line_9 = QFrame(self.frame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_9)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.comboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEditRefKwargs = QLineEdit(self.frame)
        self.lineEditRefKwargs.setObjectName(u"lineEditRefKwargs")

        self.horizontalLayout_4.addWidget(self.lineEditRefKwargs)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_12)

        self.line_11 = QFrame(self.frame)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBoxOrientation = QCheckBox(self.frame)
        self.checkBoxOrientation.setObjectName(u"checkBoxOrientation")
        self.checkBoxOrientation.setChecked(True)

        self.verticalLayout_8.addWidget(self.checkBoxOrientation)

        self.IPFExtraOptionsLayout = QHBoxLayout()
        self.IPFExtraOptionsLayout.setObjectName(u"IPFExtraOptionsLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.IPFExtraOptionsLayout.addItem(self.horizontalSpacer_6)

        self.labelColorKey = QLabel(self.frame)
        self.labelColorKey.setObjectName(u"labelColorKey")

        self.IPFExtraOptionsLayout.addWidget(self.labelColorKey)

        self.lineEditColorKey = QLineEdit(self.frame)
        self.lineEditColorKey.setObjectName(u"lineEditColorKey")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditColorKey.sizePolicy().hasHeightForWidth())
        self.lineEditColorKey.setSizePolicy(sizePolicy)
        self.lineEditColorKey.setMaximumSize(QSize(60, 16777215))

        self.IPFExtraOptionsLayout.addWidget(self.lineEditColorKey)

        self.horizontalSpacer_7 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.IPFExtraOptionsLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout_8.addLayout(self.IPFExtraOptionsLayout)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.checkBoxPhase = QCheckBox(self.frame)
        self.checkBoxPhase.setObjectName(u"checkBoxPhase")

        self.verticalLayout.addWidget(self.checkBoxPhase)

        self.checkBoxNCC = QCheckBox(self.frame)
        self.checkBoxNCC.setObjectName(u"checkBoxNCC")

        self.verticalLayout.addWidget(self.checkBoxNCC)

        self.checkBoxEvaluations = QCheckBox(self.frame)
        self.checkBoxEvaluations.setObjectName(u"checkBoxEvaluations")

        self.verticalLayout.addWidget(self.checkBoxEvaluations)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.line_10 = QFrame(self.frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 2, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 3, 3, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_16)

        self.line_17 = QFrame(self.frame)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelXmapPath = QLabel(self.frame)
        self.labelXmapPath.setObjectName(u"labelXmapPath")
        self.labelXmapPath.setStyleSheet(u"font: italic 8pt \"MS Sans Serif\";\n"
"color: rgb(127, 127, 127);")

        self.horizontalLayout_5.addWidget(self.labelXmapPath)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tableWidgetXmap = QTableWidget(self.frame)
        if (self.tableWidgetXmap.columnCount() < 2):
            self.tableWidgetXmap.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetXmap.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetXmap.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetXmap.setObjectName(u"tableWidgetXmap")
        self.tableWidgetXmap.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidgetXmap.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetXmap.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidgetXmap)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.pushButtonLoadXmap = QPushButton(self.frame)
        self.pushButtonLoadXmap.setObjectName(u"pushButtonLoadXmap")

        self.horizontalLayout_9.addWidget(self.pushButtonLoadXmap)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.line_19 = QFrame(self.frame)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_19)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_2.addWidget(self.label_14)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tableWidgetPhase = QTableWidget(self.frame)
        if (self.tableWidgetPhase.columnCount() < 5):
            self.tableWidgetPhase.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidgetPhase.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidgetPhase.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        font1 = QFont()
        font1.setPointSize(9)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidgetPhase.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        font2 = QFont()
        font2.setPointSize(7)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidgetPhase.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        font3 = QFont()
        font3.setPointSize(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tableWidgetPhase.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.tableWidgetPhase.setObjectName(u"tableWidgetPhase")
        self.tableWidgetPhase.setMinimumSize(QSize(250, 50))
        self.tableWidgetPhase.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetPhase.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidgetPhase.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetPhase.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidgetPhase)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButtonLoadMP = QPushButton(self.frame)
        self.pushButtonLoadMP.setObjectName(u"pushButtonLoadMP")

        self.horizontalLayout_3.addWidget(self.pushButtonLoadMP)

        self.pushButtonRemoveMP = QPushButton(self.frame)
        self.pushButtonRemoveMP.setObjectName(u"pushButtonRemoveMP")

        self.horizontalLayout_3.addWidget(self.pushButtonRemoveMP)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.patternCenterX = QDoubleSpinBox(self.frame)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterX, 0, 3, 1, 1)

        self.patternCenterY = QDoubleSpinBox(self.frame)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterY, 1, 3, 1, 1)

        self.patternCenterZ = QDoubleSpinBox(self.frame)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(3.000000000000000)
        self.patternCenterZ.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterZ, 2, 3, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBoxConvention = QComboBox(self.frame)
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.setObjectName(u"comboBoxConvention")

        self.horizontalLayout.addWidget(self.comboBoxConvention)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(16, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 3, 1, 1)

        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(3, 2)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(3, 2)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxPhase, self.checkBoxNCC)
        QWidget.setTabOrder(self.checkBoxNCC, self.pushButtonLoadMP)
        QWidget.setTabOrder(self.pushButtonLoadMP, self.pushButtonRemoveMP)
        QWidget.setTabOrder(self.pushButtonRemoveMP, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterZ)

        self.retranslateUi(RefineSetupDialog)
        self.buttonBox.rejected.connect(RefineSetupDialog.reject)
        self.buttonBox.accepted.connect(RefineSetupDialog.accept)
        self.checkBoxOrientation.toggled.connect(self.lineEditColorKey.setVisible)
        self.checkBoxOrientation.toggled.connect(self.labelColorKey.setVisible)

        QMetaObject.connectSlotsByName(RefineSetupDialog)
    # setupUi

    def retranslateUi(self, RefineSetupDialog):
        RefineSetupDialog.setWindowTitle(QCoreApplication.translate("RefineSetupDialog", u"Refine Crystal Map", None))
        self.label_10.setText(QCoreApplication.translate("RefineSetupDialog", u"Signal", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("RefineSetupDialog", u"Lazy loading of patterns", None))
        self.checkBoxMask.setText(QCoreApplication.translate("RefineSetupDialog", u"Apply circular mask to patterns ", None))
        self.label_7.setText(QCoreApplication.translate("RefineSetupDialog", u"Binning", None))
#if QT_CONFIG(tooltip)
        self.comboBoxBinning.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"<html><head/><body><p>Detector binning, i.e. how many pixels are binned into one, default is no binning</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSignalShape.setText(QCoreApplication.translate("RefineSetupDialog", u"Signal shape: (00x00)", None))
        self.label_15.setText(QCoreApplication.translate("RefineSetupDialog", u"Accelerating Voltage (keV)", None))
        self.label_11.setText(QCoreApplication.translate("RefineSetupDialog", u"Refinement", None))
        self.label_9.setText(QCoreApplication.translate("RefineSetupDialog", u"Method", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("RefineSetupDialog", u"minimze", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("RefineSetupDialog", u"ln_neldermead", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("RefineSetupDialog", u"differential_evolution", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("RefineSetupDialog", u"dual_annealing", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("RefineSetupDialog", u"basinhopping", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("RefineSetupDialog", u"shgo", None))

        self.label_8.setText(QCoreApplication.translate("RefineSetupDialog", u"(Optional) kwargs.", None))
        self.lineEditRefKwargs.setPlaceholderText(QCoreApplication.translate("RefineSetupDialog", u"e.g. method=\"Powell\", tol=1e-4", None))
        self.label_12.setText(QCoreApplication.translate("RefineSetupDialog", u"Maps", None))
#if QT_CONFIG(tooltip)
        self.checkBoxOrientation.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"<html><head/><body><p>Orientations are given a color based on which crystal direction &lt;<span style=\" font-style:italic;\">uvw</span>&gt; points in a certain sample direction, producing the so-called inverse pole figure (IPF) map</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOrientation.setText(QCoreApplication.translate("RefineSetupDialog", u"Refined Inverse Pole Figure", None))
        self.labelColorKey.setText(QCoreApplication.translate("RefineSetupDialog", u"Color Key Direction", None))
        self.lineEditColorKey.setInputMask(QCoreApplication.translate("RefineSetupDialog", u"[0,0,0]", None))
        self.lineEditColorKey.setText(QCoreApplication.translate("RefineSetupDialog", u"0,0,1", None))
        self.lineEditColorKey.setPlaceholderText(QCoreApplication.translate("RefineSetupDialog", u"e.g. 1,0,0", None))
#if QT_CONFIG(tooltip)
        self.checkBoxPhase.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"Map of different phases present", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPhase.setText(QCoreApplication.translate("RefineSetupDialog", u"Refined Phases", None))
#if QT_CONFIG(tooltip)
        self.checkBoxNCC.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"Normalized cross correlation scores plotted on a map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxNCC.setText(QCoreApplication.translate("RefineSetupDialog", u"Normalized Cross Correlation", None))
#if QT_CONFIG(tooltip)
        self.checkBoxEvaluations.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"the number of optimization evaluations (iterations) necessary for each pattern", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxEvaluations.setText(QCoreApplication.translate("RefineSetupDialog", u"Number Of Evaluations", None))
        self.label_16.setText(QCoreApplication.translate("RefineSetupDialog", u"Crystal Map", None))
        self.labelXmapPath.setText(QCoreApplication.translate("RefineSetupDialog", u"No crystal map loaded", None))
        ___qtablewidgetitem = self.tableWidgetXmap.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RefineSetupDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetXmap.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RefineSetupDialog", u"Orientations", None));
#if QT_CONFIG(tooltip)
        self.pushButtonLoadXmap.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"<html><head/><body><p>Add phase from master pattern (*.h5)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLoadXmap.setText(QCoreApplication.translate("RefineSetupDialog", u"Load", None))
        self.label_14.setText(QCoreApplication.translate("RefineSetupDialog", u"Detector", None))
        self.label.setText(QCoreApplication.translate("RefineSetupDialog", u"Master Patterns", None))
        ___qtablewidgetitem2 = self.tableWidgetPhase.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("RefineSetupDialog", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidgetPhase.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("RefineSetupDialog", u"Number", None));
        ___qtablewidgetitem4 = self.tableWidgetPhase.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("RefineSetupDialog", u"ISS", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"International short symbol", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem5 = self.tableWidgetPhase.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("RefineSetupDialog", u"Crystal System", None));
        ___qtablewidgetitem6 = self.tableWidgetPhase.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("RefineSetupDialog", u"Color", None));
#if QT_CONFIG(tooltip)
        self.pushButtonLoadMP.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"<html><head/><body><p>Add phase from master pattern (*.h5)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLoadMP.setText(QCoreApplication.translate("RefineSetupDialog", u"Load", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemoveMP.setToolTip(QCoreApplication.translate("RefineSetupDialog", u"<html><head/><body><p>Remove the selected phase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemoveMP.setText(QCoreApplication.translate("RefineSetupDialog", u"Remove", None))
        self.patternCenterZ.setPrefix("")
        self.label_4.setText(QCoreApplication.translate("RefineSetupDialog", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("RefineSetupDialog", u"Z:", None))
        self.label_3.setText(QCoreApplication.translate("RefineSetupDialog", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("RefineSetupDialog", u"Pattern Center", None))
        self.label_6.setText(QCoreApplication.translate("RefineSetupDialog", u"Convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("RefineSetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("RefineSetupDialog", u"TSL", None))

    # retranslateUi

