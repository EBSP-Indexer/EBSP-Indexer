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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_DiSetupDialog(object):
    def setupUi(self, DiSetupDialog):
        if not DiSetupDialog.objectName():
            DiSetupDialog.setObjectName(u"DiSetupDialog")
        DiSetupDialog.resize(792, 531)
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
        self.listWidgetPhase.setMinimumSize(QSize(0, 50))
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

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)


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
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.checkBoxLazy = QCheckBox(self.centralwidget)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBoxLazy, 1, 0, 1, 1)

        self.comboBoxBinning = QComboBox(self.centralwidget)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")

        self.gridLayout_3.addWidget(self.comboBoxBinning, 0, 1, 1, 1)

        self.checkBoxMask = QCheckBox(self.centralwidget)
        self.checkBoxMask.setObjectName(u"checkBoxMask")

        self.gridLayout_3.addWidget(self.checkBoxMask, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

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
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.doubleSpinBoxStepSize = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxStepSize.setObjectName(u"doubleSpinBoxStepSize")
        self.doubleSpinBoxStepSize.setMinimum(0.010000000000000)
        self.doubleSpinBoxStepSize.setMaximum(3.000000000000000)
        self.doubleSpinBoxStepSize.setSingleStep(0.100000000000000)
        self.doubleSpinBoxStepSize.setValue(2.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBoxStepSize, 0, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.spinBoxNumIter = QSpinBox(self.centralwidget)
        self.spinBoxNumIter.setObjectName(u"spinBoxNumIter")
        self.spinBoxNumIter.setEnabled(True)
        self.spinBoxNumIter.setMaximum(99)

        self.gridLayout_5.addWidget(self.spinBoxNumIter, 1, 1, 1, 1)

        self.checkBoxRefine = QCheckBox(self.centralwidget)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")
        self.checkBoxRefine.setMinimumSize(QSize(200, 0))
        self.checkBoxRefine.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxRefine.setChecked(True)
        self.checkBoxRefine.setTristate(False)

        self.gridLayout_5.addWidget(self.checkBoxRefine, 2, 0, 1, 1)


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

        self.checkBoxVBSE = QCheckBox(self.centralwidget)
        self.checkBoxVBSE.setObjectName(u"checkBoxVBSE")
        self.checkBoxVBSE.setToolTipDuration(-1)

        self.gridLayout_6.addWidget(self.checkBoxVBSE, 3, 0, 1, 1)

        self.checkBoxADP = QCheckBox(self.centralwidget)
        self.checkBoxADP.setObjectName(u"checkBoxADP")

        self.gridLayout_6.addWidget(self.checkBoxADP, 2, 0, 1, 1)

        self.checkBoxIQ = QCheckBox(self.centralwidget)
        self.checkBoxIQ.setObjectName(u"checkBoxIQ")

        self.gridLayout_6.addWidget(self.checkBoxIQ, 1, 0, 1, 1)

        self.checkBoxMI = QCheckBox(self.centralwidget)
        self.checkBoxMI.setObjectName(u"checkBoxMI")

        self.gridLayout_6.addWidget(self.checkBoxMI, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(DiSetupDialog)

        QMetaObject.connectSlotsByName(DiSetupDialog)
    # setupUi

    def retranslateUi(self, DiSetupDialog):
        DiSetupDialog.setWindowTitle(QCoreApplication.translate("DiSetupDialog", u"Pattern Processing", None))
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
        self.checkBoxLazy.setText(QCoreApplication.translate("DiSetupDialog", u"Lazy loading of patterns", None))
        self.checkBoxMask.setText(QCoreApplication.translate("DiSetupDialog", u"Apply circular mask to pattern", None))
        self.label_6.setText(QCoreApplication.translate("DiSetupDialog", u"Dictionary indexing parameters:", None))
        self.label_10.setText(QCoreApplication.translate("DiSetupDialog", u"Matching per iteration", None))
        self.label_8.setText(QCoreApplication.translate("DiSetupDialog", u"Angular step size (\u00b0)", None))
        self.checkBoxRefine.setText(QCoreApplication.translate("DiSetupDialog", u"Refine orientations", None))
        self.label_11.setText(QCoreApplication.translate("DiSetupDialog", u"Figures to be saved:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxVBSE.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Virtual backscatter image ", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxVBSE.setText(QCoreApplication.translate("DiSetupDialog", u"VBSE image", None))
#if QT_CONFIG(tooltip)
        self.checkBoxADP.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Average dot product map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxADP.setText(QCoreApplication.translate("DiSetupDialog", u"ADP map", None))
#if QT_CONFIG(tooltip)
        self.checkBoxIQ.setToolTip(QCoreApplication.translate("DiSetupDialog", u"Image quality map", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxIQ.setText(QCoreApplication.translate("DiSetupDialog", u"IQ map", None))
        self.checkBoxMI.setText(QCoreApplication.translate("DiSetupDialog", u"Mean intensity image", None))
    # retranslateUi

