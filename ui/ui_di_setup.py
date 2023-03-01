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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_DiSetupDialog(object):
    def setupUi(self, DiSetupDialog):
        if not DiSetupDialog.objectName():
            DiSetupDialog.setObjectName(u"DiSetupDialog")
        DiSetupDialog.resize(931, 640)
        self.gridLayout_2 = QGridLayout(DiSetupDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(DiSetupDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 18, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.listWidgetPhase = QListWidget(self.centralwidget)
        self.listWidgetPhase.setObjectName(u"listWidgetPhase")
        self.listWidgetPhase.setMinimumSize(QSize(300, 50))
        self.listWidgetPhase.setMaximumSize(QSize(16000000, 1699999))
        self.listWidgetPhase.setAcceptDrops(False)
        self.listWidgetPhase.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_3.addWidget(self.listWidgetPhase)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddPhase = QPushButton(self.centralwidget)
        self.pushButtonAddPhase.setObjectName(u"pushButtonAddPhase")

        self.horizontalLayout.addWidget(self.pushButtonAddPhase)

        self.pushButtonRemovePhase = QPushButton(self.centralwidget)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout.addWidget(self.pushButtonRemovePhase)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.patternCenterX = QDoubleSpinBox(self.centralwidget)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.001000000000000)

        self.gridLayout_4.addWidget(self.patternCenterX, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.patternCenterZ = QDoubleSpinBox(self.centralwidget)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(1.000000000000000)
        self.patternCenterZ.setSingleStep(0.001000000000000)

        self.gridLayout_4.addWidget(self.patternCenterZ, 2, 1, 1, 1)

        self.patternCenterY = QDoubleSpinBox(self.centralwidget)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.001000000000000)

        self.gridLayout_4.addWidget(self.patternCenterY, 1, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.comboBoxConvention = QComboBox(self.centralwidget)
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.setObjectName(u"comboBoxConvention")

        self.horizontalLayout_3.addWidget(self.comboBoxConvention)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_8)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBoxBinning = QComboBox(self.centralwidget)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")

        self.gridLayout_3.addWidget(self.comboBoxBinning, 1, 1, 1, 1)

        self.sliderBinning = QSlider(self.centralwidget)
        self.sliderBinning.setObjectName(u"sliderBinning")
        self.sliderBinning.setSliderPosition(0)
        self.sliderBinning.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sliderBinning, 1, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.checkBoxMask = QCheckBox(self.centralwidget)
        self.checkBoxMask.setObjectName(u"checkBoxMask")

        self.gridLayout_10.addWidget(self.checkBoxMask, 1, 0, 1, 1)

        self.checkBoxLazy = QCheckBox(self.centralwidget)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setChecked(True)

        self.gridLayout_10.addWidget(self.checkBoxLazy, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_10)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.doubleSpinBoxStepSize = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxStepSize.setObjectName(u"doubleSpinBoxStepSize")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxStepSize.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxStepSize.setSizePolicy(sizePolicy)
        self.doubleSpinBoxStepSize.setMinimumSize(QSize(80, 0))
        self.doubleSpinBoxStepSize.setMaximumSize(QSize(80, 16777215))
        self.doubleSpinBoxStepSize.setMinimum(1.000000000000000)
        self.doubleSpinBoxStepSize.setMaximum(3.000000000000000)
        self.doubleSpinBoxStepSize.setSingleStep(0.100000000000000)
        self.doubleSpinBoxStepSize.setValue(1.600000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBoxStepSize, 0, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.nIterLabel = QLabel(self.centralwidget)
        self.nIterLabel.setObjectName(u"nIterLabel")
        self.nIterLabel.setEnabled(False)

        self.gridLayout_5.addWidget(self.nIterLabel, 2, 0, 1, 1)

        self.checkBoxRefine = QCheckBox(self.centralwidget)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")
        self.checkBoxRefine.setMinimumSize(QSize(200, 0))
        self.checkBoxRefine.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxRefine.setChecked(True)
        self.checkBoxRefine.setTristate(False)

        self.gridLayout_5.addWidget(self.checkBoxRefine, 3, 0, 1, 1)

        self.spinBoxNumIter = QSpinBox(self.centralwidget)
        self.spinBoxNumIter.setObjectName(u"spinBoxNumIter")
        self.spinBoxNumIter.setEnabled(False)
        self.spinBoxNumIter.setMaximum(99)

        self.gridLayout_5.addWidget(self.spinBoxNumIter, 2, 1, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.numSimPatterns = QLabel(self.centralwidget)
        self.numSimPatterns.setObjectName(u"numSimPatterns")
        self.numSimPatterns.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.numSimPatterns, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 2)
        self.gridLayout_5.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout_5)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_4, 0, 0, 1, 1)

        self.checkBoxPM = QCheckBox(self.centralwidget)
        self.checkBoxPM.setObjectName(u"checkBoxPM")

        self.gridLayout_6.addWidget(self.checkBoxPM, 4, 0, 1, 1)

        self.checkBoxNCC = QCheckBox(self.centralwidget)
        self.checkBoxNCC.setObjectName(u"checkBoxNCC")

        self.gridLayout_6.addWidget(self.checkBoxNCC, 1, 0, 1, 1)

        self.checkBoxIPF = QCheckBox(self.centralwidget)
        self.checkBoxIPF.setObjectName(u"checkBoxIPF")
        self.checkBoxIPF.setToolTipDuration(-1)

        self.gridLayout_6.addWidget(self.checkBoxIPF, 3, 0, 1, 1)

        self.checkBoxOSM = QCheckBox(self.centralwidget)
        self.checkBoxOSM.setObjectName(u"checkBoxOSM")

        self.gridLayout_6.addWidget(self.checkBoxOSM, 2, 0, 1, 1)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_10, 5, 0, 1, 1)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_11, 7, 0, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.comboBoxFiletype = QComboBox(self.centralwidget)
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.addItem("")
        self.comboBoxFiletype.setObjectName(u"comboBoxFiletype")

        self.gridLayout_6.addWidget(self.comboBoxFiletype, 8, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(DiSetupDialog)
        self.buttonBox.accepted.connect(DiSetupDialog.accept)
        self.buttonBox.rejected.connect(DiSetupDialog.reject)

        QMetaObject.connectSlotsByName(DiSetupDialog)
    # setupUi

    def retranslateUi(self, DiSetupDialog):
        DiSetupDialog.setWindowTitle(QCoreApplication.translate("DiSetupDialog", u"Dictionary Indexing", None))
        self.label_9.setText(QCoreApplication.translate("DiSetupDialog", u"Phases:", None))
        self.pushButtonAddPhase.setText(QCoreApplication.translate("DiSetupDialog", u"Add Phase", None))
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("DiSetupDialog", u"Remove Phase", None))
        self.label_5.setText(QCoreApplication.translate("DiSetupDialog", u"Pattern center", None))
        self.label_2.setText(QCoreApplication.translate("DiSetupDialog", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("DiSetupDialog", u"Y:", None))
        self.label_4.setText(QCoreApplication.translate("DiSetupDialog", u"Z:", None))
        self.label_12.setText(QCoreApplication.translate("DiSetupDialog", u"PC convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("DiSetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("DiSetupDialog", u"TSL", None))

        self.label.setText(QCoreApplication.translate("DiSetupDialog", u"Pre-processing parameters:", None))
        self.label_7.setText(QCoreApplication.translate("DiSetupDialog", u"Binning shape", None))
        self.checkBoxMask.setText(QCoreApplication.translate("DiSetupDialog", u"Apply circular mask to patterns", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("DiSetupDialog", u"Lazy loading of patterns", None))
        self.label_6.setText(QCoreApplication.translate("DiSetupDialog", u"Dictionary indexing parameters:", None))
        self.label_8.setText(QCoreApplication.translate("DiSetupDialog", u"Angular step size (\u00b0)", None))
        self.nIterLabel.setText(QCoreApplication.translate("DiSetupDialog", u"Matching per iteration", None))
        self.checkBoxRefine.setText(QCoreApplication.translate("DiSetupDialog", u"Refine orientations", None))
        self.label_10.setText(QCoreApplication.translate("DiSetupDialog", u"Expected number of simulated patterns", None))
        self.numSimPatterns.setText(QCoreApplication.translate("DiSetupDialog", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("DiSetupDialog", u"Figures to be saved:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxPM.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Phase map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPM.setText(QCoreApplication.translate("DiSetupDialog", u"Phase map", None))
#if QT_CONFIG(tooltip)
        self.checkBoxNCC.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Nomralized cross correlation", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxNCC.setText(QCoreApplication.translate("DiSetupDialog", u"NCC", None))
#if QT_CONFIG(tooltip)
        self.checkBoxIPF.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Inverse pole figure", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxIPF.setText(QCoreApplication.translate("DiSetupDialog", u"IPF", None))
#if QT_CONFIG(tooltip)
        self.checkBoxOSM.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Orientation simmilairty map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxOSM.setText(QCoreApplication.translate("DiSetupDialog", u"OSM", None))
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

