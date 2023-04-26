# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hi_setup.ui'
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
    QSlider, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_HISetupDialog(object):
    def setupUi(self, HISetupDialog):
        if not HISetupDialog.objectName():
            HISetupDialog.setObjectName(u"HISetupDialog")
        HISetupDialog.resize(814, 624)
        self.gridLayout = QGridLayout(HISetupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(HISetupDialog)
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
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBoxLazy = QCheckBox(self.frame)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxLazy.setCheckable(True)
        self.checkBoxLazy.setChecked(True)
        self.checkBoxLazy.setTristate(False)

        self.horizontalLayout_10.addWidget(self.checkBoxLazy)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.comboBoxBinning = QComboBox(self.frame)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")

        self.horizontalLayout_13.addWidget(self.comboBoxBinning)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.line_13 = QFrame(self.frame)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_13)

        self.labelOriginalSignalShape = QLabel(self.frame)
        self.labelOriginalSignalShape.setObjectName(u"labelOriginalSignalShape")

        self.horizontalLayout_13.addWidget(self.labelOriginalSignalShape)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.labelNewSignalShape = QLabel(self.frame)
        self.labelNewSignalShape.setObjectName(u"labelNewSignalShape")

        self.horizontalLayout_13.addWidget(self.labelNewSignalShape)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 2)
        self.horizontalLayout_13.setStretch(4, 1)
        self.horizontalLayout_13.setStretch(6, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_8)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"")

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

        self.spinBoxBands = QSpinBox(self.frame)
        self.spinBoxBands.setObjectName(u"spinBoxBands")
        self.spinBoxBands.setMaximumSize(QSize(60, 16777215))
        self.spinBoxBands.setMinimum(3)
        self.spinBoxBands.setMaximum(20)
        self.spinBoxBands.setValue(9)

        self.verticalLayout_5.addWidget(self.spinBoxBands)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSliderRho = QSlider(self.frame)
        self.horizontalSliderRho.setObjectName(u"horizontalSliderRho")
        self.horizontalSliderRho.setMinimum(40)
        self.horizontalSliderRho.setMaximum(100)
        self.horizontalSliderRho.setValue(85)
        self.horizontalSliderRho.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSliderRho)

        self.labelRho = QLabel(self.frame)
        self.labelRho.setObjectName(u"labelRho")

        self.horizontalLayout_5.addWidget(self.labelRho)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.line_17 = QFrame(self.frame)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_17)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_20)

        self.line_18 = QFrame(self.frame)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_18)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBoxIndexData = QCheckBox(self.frame)
        self.checkBoxIndexData.setObjectName(u"checkBoxIndexData")
        self.checkBoxIndexData.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBoxIndexData)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_12)

        self.line_11 = QFrame(self.frame)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxOrientation = QCheckBox(self.frame)
        self.checkBoxOrientation.setObjectName(u"checkBoxOrientation")
        self.checkBoxOrientation.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBoxOrientation)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

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

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBoxPhase = QCheckBox(self.frame)
        self.checkBoxPhase.setObjectName(u"checkBoxPhase")

        self.horizontalLayout_8.addWidget(self.checkBoxPhase)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBoxQuality = QCheckBox(self.frame)
        self.checkBoxQuality.setObjectName(u"checkBoxQuality")

        self.horizontalLayout_6.addWidget(self.checkBoxQuality)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"")

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
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidgetPhase.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidgetPhase.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font3 = QFont()
        font3.setPointSize(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidgetPhase.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font4 = QFont()
        font4.setPointSize(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidgetPhase.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font5 = QFont()
        font5.setPointSize(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidgetPhase.setHorizontalHeaderItem(4, __qtablewidgetitem4)
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

        self.pushButtonCreatePhase = QPushButton(self.frame)
        self.pushButtonCreatePhase.setObjectName(u"pushButtonCreatePhase")
        self.pushButtonCreatePhase.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.pushButtonCreatePhase)

        self.pushButtonLoadPhase = QPushButton(self.frame)
        self.pushButtonLoadPhase.setObjectName(u"pushButtonLoadPhase")

        self.horizontalLayout_3.addWidget(self.pushButtonLoadPhase)

        self.pushButtonRemovePhase = QPushButton(self.frame)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout_3.addWidget(self.pushButtonRemovePhase)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.patternCenterX = QDoubleSpinBox(self.frame)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.001000000000000)

        self.horizontalLayout_4.addWidget(self.patternCenterX)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.patternCenterY = QDoubleSpinBox(self.frame)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.001000000000000)

        self.horizontalLayout_4.addWidget(self.patternCenterY)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.patternCenterZ = QDoubleSpinBox(self.frame)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(3.000000000000000)
        self.patternCenterZ.setSingleStep(0.001000000000000)

        self.horizontalLayout_4.addWidget(self.patternCenterZ)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

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

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.labelMessage = QLabel(self.frame)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_11.addWidget(self.labelMessage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(5, 5)
        self.verticalLayout_2.setStretch(10, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 3, 3, 1, 1)

        self.line_10 = QFrame(self.frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 2, 2, 1, 1)

        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setColumnStretch(3, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.spinBoxBands, self.horizontalSliderRho)
        QWidget.setTabOrder(self.horizontalSliderRho, self.lineEditColorKey)
        QWidget.setTabOrder(self.lineEditColorKey, self.tableWidgetPhase)
        QWidget.setTabOrder(self.tableWidgetPhase, self.pushButtonCreatePhase)
        QWidget.setTabOrder(self.pushButtonCreatePhase, self.pushButtonLoadPhase)
        QWidget.setTabOrder(self.pushButtonLoadPhase, self.pushButtonRemovePhase)
        QWidget.setTabOrder(self.pushButtonRemovePhase, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterZ)
        QWidget.setTabOrder(self.patternCenterZ, self.comboBoxConvention)

        self.retranslateUi(HISetupDialog)
        self.buttonBox.rejected.connect(HISetupDialog.reject)
        self.buttonBox.accepted.connect(HISetupDialog.accept)
        self.checkBoxOrientation.toggled.connect(self.lineEditColorKey.setVisible)
        self.checkBoxOrientation.toggled.connect(self.labelColorKey.setVisible)

        QMetaObject.connectSlotsByName(HISetupDialog)
    # setupUi

    def retranslateUi(self, HISetupDialog):
        HISetupDialog.setWindowTitle(QCoreApplication.translate("HISetupDialog", u"Hough Indexing", None))
        self.label_10.setText(QCoreApplication.translate("HISetupDialog", u"Signal", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("HISetupDialog", u"Lazy loading of patterns", None))
        self.label_15.setText(QCoreApplication.translate("HISetupDialog", u"Binning", None))
        self.labelOriginalSignalShape.setText(QCoreApplication.translate("HISetupDialog", u"(x, y)", None))
        self.label_18.setText(QCoreApplication.translate("HISetupDialog", u"<p> &rarr; </p>", None))
        self.labelNewSignalShape.setText(QCoreApplication.translate("HISetupDialog", u"(x, y)", None))
        self.label_11.setText(QCoreApplication.translate("HISetupDialog", u"Hough Transform", None))
        self.label_9.setText(QCoreApplication.translate("HISetupDialog", u"Number of bands", None))
#if QT_CONFIG(tooltip)
        self.spinBoxBands.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Number of detected bands to use in triplet voting, default is 9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("HISetupDialog", u"Rho fraction (\u03c1) ", None))
#if QT_CONFIG(tooltip)
        self.horizontalSliderRho.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>The fraction of the pattern to be considered when detecting bands, default is 85%. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelRho.setText(QCoreApplication.translate("HISetupDialog", u"85%", None))
        self.label_20.setText(QCoreApplication.translate("HISetupDialog", u"Crystal map", None))
#if QT_CONFIG(tooltip)
        self.checkBoxIndexData.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Whether to save the index data array\u00a0as *.npy in addition to the resulting crystal map, can be used to refine orientations later</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxIndexData.setText(QCoreApplication.translate("HISetupDialog", u"Save Index Data as .npy", None))
        self.label_12.setText(QCoreApplication.translate("HISetupDialog", u"Images", None))
#if QT_CONFIG(tooltip)
        self.checkBoxOrientation.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Orientations are given a color based on which crystal direction &lt;<span style=\" font-style:italic;\">uvw</span>&gt; points in a certain sample direction, producing the so-called inverse pole figure (IPF) map</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOrientation.setText(QCoreApplication.translate("HISetupDialog", u"Inverse Pole Figure Map", None))
        self.labelColorKey.setText(QCoreApplication.translate("HISetupDialog", u"Color Key Direction", None))
        self.lineEditColorKey.setInputMask(QCoreApplication.translate("HISetupDialog", u"[0,0,0]", None))
        self.lineEditColorKey.setText(QCoreApplication.translate("HISetupDialog", u"0,0,1", None))
        self.lineEditColorKey.setPlaceholderText(QCoreApplication.translate("HISetupDialog", u"e.g. 1,0,0", None))
#if QT_CONFIG(tooltip)
        self.checkBoxPhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"Generate map of different phases present", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPhase.setText(QCoreApplication.translate("HISetupDialog", u"Phase Map", None))
#if QT_CONFIG(tooltip)
        self.checkBoxQuality.setToolTip(QCoreApplication.translate("HISetupDialog", u"Generate quality metrics for combined maps", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxQuality.setText(QCoreApplication.translate("HISetupDialog", u"Quality Metric Maps", None))
        self.label_14.setText(QCoreApplication.translate("HISetupDialog", u"Detector", None))
        self.label.setText(QCoreApplication.translate("HISetupDialog", u"Phases", None))
        ___qtablewidgetitem = self.tableWidgetPhase.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HISetupDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetPhase.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HISetupDialog", u"Number", None));
        ___qtablewidgetitem2 = self.tableWidgetPhase.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HISetupDialog", u"ISS", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("HISetupDialog", u"International short symbol", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tableWidgetPhase.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HISetupDialog", u"Crystal System", None));
        ___qtablewidgetitem4 = self.tableWidgetPhase.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("HISetupDialog", u"Color", None));
#if QT_CONFIG(tooltip)
        self.pushButtonCreatePhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Create and add a custom phase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCreatePhase.setText(QCoreApplication.translate("HISetupDialog", u"Create", None))
#if QT_CONFIG(tooltip)
        self.pushButtonLoadPhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Add phase from master pattern (*.h5)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLoadPhase.setText(QCoreApplication.translate("HISetupDialog", u"Load", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemovePhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Remove the selected phase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("HISetupDialog", u"Remove", None))
        self.label_2.setText(QCoreApplication.translate("HISetupDialog", u"Pattern Center", None))
        self.label_3.setText(QCoreApplication.translate("HISetupDialog", u"X:", None))
        self.label_4.setText(QCoreApplication.translate("HISetupDialog", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("HISetupDialog", u"Z:", None))
        self.patternCenterZ.setPrefix("")
        self.label_6.setText(QCoreApplication.translate("HISetupDialog", u"Convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("HISetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("HISetupDialog", u"TSL", None))

        self.labelMessage.setText(QCoreApplication.translate("HISetupDialog", u"*Message", None))
    # retranslateUi

