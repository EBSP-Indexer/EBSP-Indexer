# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattern_center.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_PatternCenterDialog(object):
    def setupUi(self, PatternCenterDialog):
        if not PatternCenterDialog.objectName():
            PatternCenterDialog.setObjectName(u"PatternCenterDialog")
        PatternCenterDialog.resize(706, 544)
        self.horizontalLayout_2 = QHBoxLayout(PatternCenterDialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.MplWidget = MplWidget(PatternCenterDialog)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(400, 400))

        self.verticalLayout_3.addWidget(self.MplWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.counterLabel = QLabel(PatternCenterDialog)
        self.counterLabel.setObjectName(u"counterLabel")
        self.counterLabel.setMinimumSize(QSize(140, 0))
        self.counterLabel.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout.addWidget(self.counterLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButtonLeft = QToolButton(PatternCenterDialog)
        self.toolButtonLeft.setObjectName(u"toolButtonLeft")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonLeft.sizePolicy().hasHeightForWidth())
        self.toolButtonLeft.setSizePolicy(sizePolicy)
        self.toolButtonLeft.setMinimumSize(QSize(35, 0))
        self.toolButtonLeft.setInputMethodHints(Qt.ImhNone)
        self.toolButtonLeft.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButtonLeft.setAutoRaise(False)
        self.toolButtonLeft.setArrowType(Qt.LeftArrow)

        self.horizontalLayout.addWidget(self.toolButtonLeft)

        self.toolButtonRight = QToolButton(PatternCenterDialog)
        self.toolButtonRight.setObjectName(u"toolButtonRight")
        sizePolicy.setHeightForWidth(self.toolButtonRight.sizePolicy().hasHeightForWidth())
        self.toolButtonRight.setSizePolicy(sizePolicy)
        self.toolButtonRight.setMinimumSize(QSize(35, 0))
        self.toolButtonRight.setArrowType(Qt.RightArrow)

        self.horizontalLayout.addWidget(self.toolButtonRight)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bandButton = QPushButton(PatternCenterDialog)
        self.bandButton.setObjectName(u"bandButton")
        self.bandButton.setMinimumSize(QSize(140, 0))
        self.bandButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout.addWidget(self.bandButton)

        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listPhases = QListWidget(PatternCenterDialog)
        self.listPhases.setObjectName(u"listPhases")

        self.verticalLayout.addWidget(self.listPhases)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonAddPhase = QPushButton(PatternCenterDialog)
        self.buttonAddPhase.setObjectName(u"buttonAddPhase")

        self.horizontalLayout_3.addWidget(self.buttonAddPhase)

        self.buttonRemovePhase = QPushButton(PatternCenterDialog)
        self.buttonRemovePhase.setObjectName(u"buttonRemovePhase")

        self.horizontalLayout_3.addWidget(self.buttonRemovePhase)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(PatternCenterDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelXStar = QLabel(PatternCenterDialog)
        self.labelXStar.setObjectName(u"labelXStar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelXStar.sizePolicy().hasHeightForWidth())
        self.labelXStar.setSizePolicy(sizePolicy1)
        self.labelXStar.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.labelXStar, 0, 0, 1, 1)

        self.spinBoxX = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxX.setObjectName(u"spinBoxX")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBoxX.sizePolicy().hasHeightForWidth())
        self.spinBoxX.setSizePolicy(sizePolicy2)
        self.spinBoxX.setDecimals(4)
        self.spinBoxX.setMaximum(1.000000000000000)
        self.spinBoxX.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.spinBoxX, 0, 1, 1, 1)

        self.spinBoxY = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxY.setObjectName(u"spinBoxY")
        self.spinBoxY.setDecimals(4)
        self.spinBoxY.setMaximum(1.000000000000000)
        self.spinBoxY.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.spinBoxY, 1, 1, 1, 1)

        self.labelYStar = QLabel(PatternCenterDialog)
        self.labelYStar.setObjectName(u"labelYStar")

        self.gridLayout_2.addWidget(self.labelYStar, 1, 0, 1, 1)

        self.labelZStar = QLabel(PatternCenterDialog)
        self.labelZStar.setObjectName(u"labelZStar")

        self.gridLayout_2.addWidget(self.labelZStar, 2, 0, 1, 1)

        self.spinBoxZ = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxZ.setObjectName(u"spinBoxZ")
        self.spinBoxZ.setDecimals(4)
        self.spinBoxZ.setMaximum(3.000000000000000)
        self.spinBoxZ.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.spinBoxZ, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonPlot = QPushButton(PatternCenterDialog)
        self.buttonPlot.setObjectName(u"buttonPlot")

        self.horizontalLayout_4.addWidget(self.buttonPlot)

        self.buttonTune = QPushButton(PatternCenterDialog)
        self.buttonTune.setObjectName(u"buttonTune")
        sizePolicy2.setHeightForWidth(self.buttonTune.sizePolicy().hasHeightForWidth())
        self.buttonTune.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.buttonTune)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_5.setSpacing(-1)
#endif
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelMisfit = QLabel(PatternCenterDialog)
        self.labelMisfit.setObjectName(u"labelMisfit")

        self.horizontalLayout_5.addWidget(self.labelMisfit)

        self.ignoreCheckBox = QCheckBox(PatternCenterDialog)
        self.ignoreCheckBox.setObjectName(u"ignoreCheckBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ignoreCheckBox.sizePolicy().hasHeightForWidth())
        self.ignoreCheckBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.ignoreCheckBox, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(PatternCenterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy4)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(PatternCenterDialog)

        QMetaObject.connectSlotsByName(PatternCenterDialog)
    # setupUi

    def retranslateUi(self, PatternCenterDialog):
        PatternCenterDialog.setWindowTitle(QCoreApplication.translate("PatternCenterDialog", u"Pattern Center Refinement", None))
        self.counterLabel.setText(QCoreApplication.translate("PatternCenterDialog", u"Calibration Pattern: 0/0", None))
        self.toolButtonLeft.setText(QCoreApplication.translate("PatternCenterDialog", u"...", None))
        self.toolButtonRight.setText(QCoreApplication.translate("PatternCenterDialog", u"...", None))
        self.bandButton.setText(QCoreApplication.translate("PatternCenterDialog", u"Show bands", None))
        self.buttonAddPhase.setText(QCoreApplication.translate("PatternCenterDialog", u"Add Phase", None))
        self.buttonRemovePhase.setText(QCoreApplication.translate("PatternCenterDialog", u"Remove Phase", None))
        self.labelXStar.setText(QCoreApplication.translate("PatternCenterDialog", u"X-Star", None))
        self.labelYStar.setText(QCoreApplication.translate("PatternCenterDialog", u"Y-Star", None))
        self.labelZStar.setText(QCoreApplication.translate("PatternCenterDialog", u"Z-Star", None))
        self.buttonPlot.setText(QCoreApplication.translate("PatternCenterDialog", u"Plot", None))
        self.buttonTune.setText(QCoreApplication.translate("PatternCenterDialog", u"Tune", None))
        self.labelMisfit.setText(QCoreApplication.translate("PatternCenterDialog", u"Misfit (\u00b0): 0.0000", None))
        self.ignoreCheckBox.setText(QCoreApplication.translate("PatternCenterDialog", u"Ignore pattern", None))
    # retranslateUi

