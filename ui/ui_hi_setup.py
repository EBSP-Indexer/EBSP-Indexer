# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hi_setup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_HISetupDialog(object):
    def setupUi(self, HISetupDialog):
        if not HISetupDialog.objectName():
            HISetupDialog.setObjectName(u"HISetupDialog")
        HISetupDialog.resize(676, 497)
        self.gridLayout = QGridLayout(HISetupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(HISetupDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.comboBoxBinning = QComboBox(self.frame)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")
        self.comboBoxBinning.setMaximumSize(QSize(80, 16777215))
        self.comboBoxBinning.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.comboBoxBinning)


        self.verticalLayout.addLayout(self.verticalLayout_4)

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

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.checkBoxLazy = QCheckBox(self.frame)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxLazy.setCheckable(True)
        self.checkBoxLazy.setChecked(True)
        self.checkBoxLazy.setTristate(False)

        self.verticalLayout.addWidget(self.checkBoxLazy)

        self.checkBoxOrientation = QCheckBox(self.frame)
        self.checkBoxOrientation.setObjectName(u"checkBoxOrientation")
        self.checkBoxOrientation.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxOrientation)

        self.checkBoxPhase = QCheckBox(self.frame)
        self.checkBoxPhase.setObjectName(u"checkBoxPhase")

        self.verticalLayout.addWidget(self.checkBoxPhase)

        self.checkBoxQuality = QCheckBox(self.frame)
        self.checkBoxQuality.setObjectName(u"checkBoxQuality")

        self.verticalLayout.addWidget(self.checkBoxQuality)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.listWidgetPhase = QListWidget(self.frame)
        self.listWidgetPhase.setObjectName(u"listWidgetPhase")
        self.listWidgetPhase.setEditTriggers(QAbstractItemView.EditKeyPressed)
        self.listWidgetPhase.setAlternatingRowColors(False)
        self.listWidgetPhase.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.listWidgetPhase)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonAddPhase = QPushButton(self.frame)
        self.pushButtonAddPhase.setObjectName(u"pushButtonAddPhase")

        self.horizontalLayout_3.addWidget(self.pushButtonAddPhase)

        self.pushButtonRemovePhase = QPushButton(self.frame)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout_3.addWidget(self.pushButtonRemovePhase)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.patternCenterY = QDoubleSpinBox(self.frame)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.000100000000000)

        self.gridLayout_2.addWidget(self.patternCenterY, 1, 1, 1, 1)

        self.patternCenterX = QDoubleSpinBox(self.frame)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.000100000000000)

        self.gridLayout_2.addWidget(self.patternCenterX, 0, 1, 1, 1)

        self.patternCenterZ = QDoubleSpinBox(self.frame)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(1.000000000000000)
        self.patternCenterZ.setSingleStep(0.000100000000000)

        self.gridLayout_2.addWidget(self.patternCenterZ, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

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

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(9, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(134, 388, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxLazy, self.checkBoxPhase)
        QWidget.setTabOrder(self.checkBoxPhase, self.checkBoxQuality)
        QWidget.setTabOrder(self.checkBoxQuality, self.listWidgetPhase)
        QWidget.setTabOrder(self.listWidgetPhase, self.pushButtonAddPhase)
        QWidget.setTabOrder(self.pushButtonAddPhase, self.pushButtonRemovePhase)
        QWidget.setTabOrder(self.pushButtonRemovePhase, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterZ)

        self.retranslateUi(HISetupDialog)
        self.buttonBox.rejected.connect(HISetupDialog.reject)
        self.buttonBox.accepted.connect(HISetupDialog.accept)

        QMetaObject.connectSlotsByName(HISetupDialog)
    # setupUi

    def retranslateUi(self, HISetupDialog):
        HISetupDialog.setWindowTitle(QCoreApplication.translate("HISetupDialog", u"Hough Indexing", None))
        self.label_7.setText(QCoreApplication.translate("HISetupDialog", u"Binning shape", None))
        self.label_9.setText(QCoreApplication.translate("HISetupDialog", u"Number of bands", None))
        self.label_8.setText(QCoreApplication.translate("HISetupDialog", u"Rho fraction (\u03c1) ", None))
        self.labelRho.setText(QCoreApplication.translate("HISetupDialog", u"85%", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("HISetupDialog", u"Lazy loading of patterns", None))
        self.checkBoxOrientation.setText(QCoreApplication.translate("HISetupDialog", u"Generate orientation maps", None))
        self.checkBoxPhase.setText(QCoreApplication.translate("HISetupDialog", u"Generate phase maps", None))
        self.checkBoxQuality.setText(QCoreApplication.translate("HISetupDialog", u"Generate quality metrics for combined maps", None))
        self.label.setText(QCoreApplication.translate("HISetupDialog", u"Phases", None))
        self.pushButtonAddPhase.setText(QCoreApplication.translate("HISetupDialog", u"Add Phase", None))
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("HISetupDialog", u"Remove Phase", None))
        self.label_2.setText(QCoreApplication.translate("HISetupDialog", u"Pattern center", None))
        self.patternCenterZ.setPrefix("")
        self.label_4.setText(QCoreApplication.translate("HISetupDialog", u"Y:", None))
        self.label_3.setText(QCoreApplication.translate("HISetupDialog", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("HISetupDialog", u"Z:", None))
        self.label_6.setText(QCoreApplication.translate("HISetupDialog", u"PC convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("HISetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("HISetupDialog", u"TSL", None))

    # retranslateUi

