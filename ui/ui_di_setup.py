# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'di_setup.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_DiSetupDialog(object):
    def setupUi(self, DiSetupDialog):
        if not DiSetupDialog.objectName():
            DiSetupDialog.setObjectName(u"DiSetupDialog")
        DiSetupDialog.resize(950, 501)
        self.gridLayout_4 = QGridLayout(DiSetupDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.centralwidget = QFrame(DiSetupDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_9.setFont(font)

        self.verticalLayout_4.addWidget(self.label_9)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_9)

        self.tableWidgetPhase = QTableWidget(self.centralwidget)
        if (self.tableWidgetPhase.columnCount() < 5):
            self.tableWidgetPhase.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetPhase.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetPhase.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetPhase.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetPhase.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetPhase.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetPhase.setObjectName(u"tableWidgetPhase")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetPhase.sizePolicy().hasHeightForWidth())
        self.tableWidgetPhase.setSizePolicy(sizePolicy)
        self.tableWidgetPhase.setMinimumSize(QSize(510, 0))
        self.tableWidgetPhase.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidgetPhase.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetPhase.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidgetPhase)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonAddPhase = QPushButton(self.centralwidget)
        self.pushButtonAddPhase.setObjectName(u"pushButtonAddPhase")

        self.horizontalLayout_3.addWidget(self.pushButtonAddPhase)

        self.pushButtonRemovePhase = QPushButton(self.centralwidget)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout_3.addWidget(self.pushButtonRemovePhase)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_4.addWidget(self.label_16)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.patternCenterX = QDoubleSpinBox(self.centralwidget)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.001000000000000)

        self.horizontalLayout_6.addWidget(self.patternCenterX)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.patternCenterY = QDoubleSpinBox(self.centralwidget)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.001000000000000)

        self.horizontalLayout_6.addWidget(self.patternCenterY)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.patternCenterZ = QDoubleSpinBox(self.centralwidget)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(1.000000000000000)
        self.patternCenterZ.setSingleStep(0.001000000000000)

        self.horizontalLayout_6.addWidget(self.patternCenterZ)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.comboBoxConvention = QComboBox(self.centralwidget)
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.setObjectName(u"comboBoxConvention")

        self.horizontalLayout_7.addWidget(self.comboBoxConvention)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBoxLazy = QCheckBox(self.centralwidget)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBoxLazy)

        self.checkBoxMask = QCheckBox(self.centralwidget)
        self.checkBoxMask.setObjectName(u"checkBoxMask")

        self.verticalLayout_2.addWidget(self.checkBoxMask)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.comboBoxBinning = QComboBox(self.centralwidget)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")

        self.horizontalLayout.addWidget(self.comboBoxBinning)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_8)

        self.labelOriginalSigShape = QLabel(self.centralwidget)
        self.labelOriginalSigShape.setObjectName(u"labelOriginalSigShape")

        self.horizontalLayout.addWidget(self.labelOriginalSigShape)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.labelNewSignalShape = QLabel(self.centralwidget)
        self.labelNewSignalShape.setObjectName(u"labelNewSignalShape")

        self.horizontalLayout.addWidget(self.labelNewSignalShape)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.doubleSpinBoxStepSize = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxStepSize.setObjectName(u"doubleSpinBoxStepSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleSpinBoxStepSize.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxStepSize.setSizePolicy(sizePolicy1)
        self.doubleSpinBoxStepSize.setMinimumSize(QSize(0, 0))
        self.doubleSpinBoxStepSize.setMaximumSize(QSize(80, 16777215))
        self.doubleSpinBoxStepSize.setMinimum(1.000000000000000)
        self.doubleSpinBoxStepSize.setMaximum(3.000000000000000)
        self.doubleSpinBoxStepSize.setSingleStep(0.100000000000000)
        self.doubleSpinBoxStepSize.setValue(1.600000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBoxStepSize)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.numSimPatterns = QLabel(self.centralwidget)
        self.numSimPatterns.setObjectName(u"numSimPatterns")
        sizePolicy1.setHeightForWidth(self.numSimPatterns.sizePolicy().hasHeightForWidth())
        self.numSimPatterns.setSizePolicy(sizePolicy1)
        self.numSimPatterns.setMinimumSize(QSize(70, 0))
        self.numSimPatterns.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.numSimPatterns)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nIterLabel = QLabel(self.centralwidget)
        self.nIterLabel.setObjectName(u"nIterLabel")
        self.nIterLabel.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.nIterLabel)

        self.spinBoxNumIter = QSpinBox(self.centralwidget)
        self.spinBoxNumIter.setObjectName(u"spinBoxNumIter")
        self.spinBoxNumIter.setEnabled(False)
        self.spinBoxNumIter.setMaximum(99)

        self.horizontalLayout_4.addWidget(self.spinBoxNumIter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBoxRefine = QCheckBox(self.centralwidget)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")
        self.checkBoxRefine.setMinimumSize(QSize(200, 0))
        self.checkBoxRefine.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxRefine.setChecked(False)
        self.checkBoxRefine.setTristate(False)

        self.verticalLayout.addWidget(self.checkBoxRefine)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_3.addWidget(self.label_15)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.checkBoxOSM = QCheckBox(self.centralwidget)
        self.checkBoxOSM.setObjectName(u"checkBoxOSM")

        self.gridLayout.addWidget(self.checkBoxOSM, 1, 1, 1, 1)

        self.checkBoxNCC = QCheckBox(self.centralwidget)
        self.checkBoxNCC.setObjectName(u"checkBoxNCC")

        self.gridLayout.addWidget(self.checkBoxNCC, 1, 2, 1, 1)

        self.checkBoxPM = QCheckBox(self.centralwidget)
        self.checkBoxPM.setObjectName(u"checkBoxPM")

        self.gridLayout.addWidget(self.checkBoxPM, 0, 2, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.checkBoxIPF = QCheckBox(self.centralwidget)
        self.checkBoxIPF.setObjectName(u"checkBoxIPF")
        self.checkBoxIPF.setToolTipDuration(-1)
        self.checkBoxIPF.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.checkBoxIPF, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.comboBoxFiletype = QComboBox(self.centralwidget)
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.setObjectName(u"comboBoxFiletype")

        self.horizontalLayout_5.addWidget(self.comboBoxFiletype)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.centralwidget, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxLazy, self.checkBoxMask)
        QWidget.setTabOrder(self.checkBoxMask, self.comboBoxBinning)
        QWidget.setTabOrder(self.comboBoxBinning, self.doubleSpinBoxStepSize)
        QWidget.setTabOrder(self.doubleSpinBoxStepSize, self.spinBoxNumIter)
        QWidget.setTabOrder(self.spinBoxNumIter, self.checkBoxRefine)
        QWidget.setTabOrder(self.checkBoxRefine, self.checkBoxIPF)
        QWidget.setTabOrder(self.checkBoxIPF, self.checkBoxPM)
        QWidget.setTabOrder(self.checkBoxPM, self.checkBoxOSM)
        QWidget.setTabOrder(self.checkBoxOSM, self.checkBoxNCC)
        QWidget.setTabOrder(self.checkBoxNCC, self.comboBoxFiletype)
        QWidget.setTabOrder(self.comboBoxFiletype, self.tableWidgetPhase)
        QWidget.setTabOrder(self.tableWidgetPhase, self.pushButtonAddPhase)
        QWidget.setTabOrder(self.pushButtonAddPhase, self.pushButtonRemovePhase)
        QWidget.setTabOrder(self.pushButtonRemovePhase, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterZ)
        QWidget.setTabOrder(self.patternCenterZ, self.comboBoxConvention)

        self.retranslateUi(DiSetupDialog)
        self.buttonBox.accepted.connect(DiSetupDialog.accept)
        self.buttonBox.rejected.connect(DiSetupDialog.reject)

        QMetaObject.connectSlotsByName(DiSetupDialog)
    # setupUi

    def retranslateUi(self, DiSetupDialog):
        DiSetupDialog.setWindowTitle(QCoreApplication.translate("DiSetupDialog", u"Dictionary Indexing", None))
        self.label_9.setText(QCoreApplication.translate("DiSetupDialog", u"Phases", None))
        ___qtablewidgetitem = self.tableWidgetPhase.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DiSetupDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetPhase.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DiSetupDialog", u"Number", None));
        ___qtablewidgetitem2 = self.tableWidgetPhase.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DiSetupDialog", u"ISS", None));
        ___qtablewidgetitem3 = self.tableWidgetPhase.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DiSetupDialog", u"Crystal System", None));
        ___qtablewidgetitem4 = self.tableWidgetPhase.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DiSetupDialog", u"Color", None));
        self.pushButtonAddPhase.setText(QCoreApplication.translate("DiSetupDialog", u"Add Phase", None))
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("DiSetupDialog", u"Remove Phase", None))
        self.label_16.setText(QCoreApplication.translate("DiSetupDialog", u"Detector", None))
        self.label_5.setText(QCoreApplication.translate("DiSetupDialog", u"Pattern center:", None))
        self.label_2.setText(QCoreApplication.translate("DiSetupDialog", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("DiSetupDialog", u"Y:", None))
        self.label_4.setText(QCoreApplication.translate("DiSetupDialog", u"Z:", None))
        self.label_12.setText(QCoreApplication.translate("DiSetupDialog", u"PC convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("DiSetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("DiSetupDialog", u"TSL", None))

        self.label.setText(QCoreApplication.translate("DiSetupDialog", u"Signal", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("DiSetupDialog", u"Lazy loading of patterns", None))
        self.checkBoxMask.setText(QCoreApplication.translate("DiSetupDialog", u"Apply circular mask to patterns", None))
        self.label_7.setText(QCoreApplication.translate("DiSetupDialog", u"Binning", None))
        self.labelOriginalSigShape.setText(QCoreApplication.translate("DiSetupDialog", u"(x, y)", None))
        self.label_17.setText(QCoreApplication.translate("DiSetupDialog", u"<p> &rarr; </p>", None))
        self.labelNewSignalShape.setText(QCoreApplication.translate("DiSetupDialog", u"(x, y)", None))
        self.label_6.setText(QCoreApplication.translate("DiSetupDialog", u"Dictionary indexing parameters", None))
        self.label_8.setText(QCoreApplication.translate("DiSetupDialog", u"Angular step size (\u00b0)", None))
        self.label_10.setText(QCoreApplication.translate("DiSetupDialog", u"# simulated patterns", None))
        self.numSimPatterns.setText(QCoreApplication.translate("DiSetupDialog", u"N/A", None))
        self.nIterLabel.setText(QCoreApplication.translate("DiSetupDialog", u"Number of chunks", None))
        self.checkBoxRefine.setText(QCoreApplication.translate("DiSetupDialog", u"Refine orientations", None))
        self.label_15.setText(QCoreApplication.translate("DiSetupDialog", u"Figures to be saved:", None))
        self.label_14.setText(QCoreApplication.translate("DiSetupDialog", u"Quality metric maps:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxOSM.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Orientation simmilairty map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOSM.setText(QCoreApplication.translate("DiSetupDialog", u"OSM", None))
#if QT_CONFIG(tooltip)
        self.checkBoxNCC.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Nomralized cross correlation", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxNCC.setText(QCoreApplication.translate("DiSetupDialog", u"NCC", None))
#if QT_CONFIG(tooltip)
        self.checkBoxPM.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Phase map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPM.setText(QCoreApplication.translate("DiSetupDialog", u"Phase map", None))
        self.label_11.setText(QCoreApplication.translate("DiSetupDialog", u"Crystal maps:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxIPF.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Inverse pole figure", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxIPF.setText(QCoreApplication.translate("DiSetupDialog", u"Inverse pole figure", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("DiSetupDialog", u"<html><head/><body><p>ATEX fileformat: .ang</p><p>Kikuchip format: .h5</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("DiSetupDialog", u"Filetype for saving crystal maps:", None))
        self.comboBoxFiletype.setItemText(0, QCoreApplication.translate("DiSetupDialog", u".ang, .h5", None))
        self.comboBoxFiletype.setItemText(1, QCoreApplication.translate("DiSetupDialog", u".ang", None))
        self.comboBoxFiletype.setItemText(2, QCoreApplication.translate("DiSetupDialog", u".h5", None))

#if QT_CONFIG(tooltip)
        self.comboBoxFiletype.setToolTip(QCoreApplication.translate("DiSetupDialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

