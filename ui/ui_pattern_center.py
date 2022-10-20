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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_PatternCenterDialog(object):
    def setupUi(self, PatternCenterDialog):
        if not PatternCenterDialog.objectName():
            PatternCenterDialog.setObjectName(u"PatternCenterDialog")
        PatternCenterDialog.resize(667, 464)
        self.horizontalLayout_7 = QHBoxLayout(PatternCenterDialog)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.MplWidget = MplWidget(PatternCenterDialog)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(400, 400))

        self.verticalLayout_4.addWidget(self.MplWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButtonLeft = QToolButton(PatternCenterDialog)
        self.toolButtonLeft.setObjectName(u"toolButtonLeft")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonLeft.sizePolicy().hasHeightForWidth())
        self.toolButtonLeft.setSizePolicy(sizePolicy)
        self.toolButtonLeft.setInputMethodHints(Qt.ImhNone)
        self.toolButtonLeft.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButtonLeft.setAutoRaise(False)
        self.toolButtonLeft.setArrowType(Qt.LeftArrow)

        self.horizontalLayout.addWidget(self.toolButtonLeft)

        self.toolButtonRight = QToolButton(PatternCenterDialog)
        self.toolButtonRight.setObjectName(u"toolButtonRight")
        sizePolicy.setHeightForWidth(self.toolButtonRight.sizePolicy().hasHeightForWidth())
        self.toolButtonRight.setSizePolicy(sizePolicy)
        self.toolButtonRight.setArrowType(Qt.RightArrow)

        self.horizontalLayout.addWidget(self.toolButtonRight)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelXStar = QLabel(PatternCenterDialog)
        self.labelXStar.setObjectName(u"labelXStar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelXStar.sizePolicy().hasHeightForWidth())
        self.labelXStar.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.labelXStar)

        self.spinBoxX = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxX.setObjectName(u"spinBoxX")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBoxX.sizePolicy().hasHeightForWidth())
        self.spinBoxX.setSizePolicy(sizePolicy2)
        self.spinBoxX.setDecimals(3)
        self.spinBoxX.setMaximum(10.000000000000000)
        self.spinBoxX.setSingleStep(0.001000000000000)

        self.verticalLayout.addWidget(self.spinBoxX)

        self.labelYStar = QLabel(PatternCenterDialog)
        self.labelYStar.setObjectName(u"labelYStar")

        self.verticalLayout.addWidget(self.labelYStar)

        self.spinBoxY = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxY.setObjectName(u"spinBoxY")
        self.spinBoxY.setDecimals(3)
        self.spinBoxY.setMaximum(10.000000000000000)
        self.spinBoxY.setSingleStep(0.001000000000000)

        self.verticalLayout.addWidget(self.spinBoxY)

        self.labelZStar = QLabel(PatternCenterDialog)
        self.labelZStar.setObjectName(u"labelZStar")

        self.verticalLayout.addWidget(self.labelZStar)

        self.spinBoxZ = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxZ.setObjectName(u"spinBoxZ")
        self.spinBoxZ.setDecimals(3)
        self.spinBoxZ.setMaximum(10.000000000000000)
        self.spinBoxZ.setSingleStep(0.001000000000000)

        self.verticalLayout.addWidget(self.spinBoxZ)

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

        self.labelMisfit = QLabel(PatternCenterDialog)
        self.labelMisfit.setObjectName(u"labelMisfit")

        self.verticalLayout.addWidget(self.labelMisfit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(PatternCenterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignRight)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalLayout_7.setStretch(0, 1)

        self.retranslateUi(PatternCenterDialog)

        QMetaObject.connectSlotsByName(PatternCenterDialog)
    # setupUi

    def retranslateUi(self, PatternCenterDialog):
        PatternCenterDialog.setWindowTitle(QCoreApplication.translate("PatternCenterDialog", u"Pattern Center Refinement", None))
        self.toolButtonLeft.setText(QCoreApplication.translate("PatternCenterDialog", u"...", None))
        self.toolButtonRight.setText(QCoreApplication.translate("PatternCenterDialog", u"...", None))
        self.buttonAddPhase.setText(QCoreApplication.translate("PatternCenterDialog", u"Add Phase", None))
        self.buttonRemovePhase.setText(QCoreApplication.translate("PatternCenterDialog", u"Remove Phase", None))
        self.labelXStar.setText(QCoreApplication.translate("PatternCenterDialog", u"X-Star", None))
        self.labelYStar.setText(QCoreApplication.translate("PatternCenterDialog", u"Y-Star", None))
        self.labelZStar.setText(QCoreApplication.translate("PatternCenterDialog", u"Z-Star", None))
        self.buttonPlot.setText(QCoreApplication.translate("PatternCenterDialog", u"Plot", None))
        self.buttonTune.setText(QCoreApplication.translate("PatternCenterDialog", u"Tune", None))
        self.labelMisfit.setText(QCoreApplication.translate("PatternCenterDialog", u"Misfit (\u00b0):", None))
    # retranslateUi

