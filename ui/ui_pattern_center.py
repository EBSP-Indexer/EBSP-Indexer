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
    QDoubleSpinBox, QHBoxLayout, QLabel, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget

class Ui_PatternCenterDialog(object):
    def setupUi(self, PatternCenterDialog):
        if not PatternCenterDialog.objectName():
            PatternCenterDialog.setObjectName(u"PatternCenterDialog")
        PatternCenterDialog.resize(598, 447)
        self.horizontalLayout = QHBoxLayout(PatternCenterDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MplWidget = MplWidget(PatternCenterDialog)
        self.MplWidget.setObjectName(u"MplWidget")

        self.horizontalLayout.addWidget(self.MplWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonAddPhase = QPushButton(PatternCenterDialog)
        self.buttonAddPhase.setObjectName(u"buttonAddPhase")

        self.verticalLayout.addWidget(self.buttonAddPhase)

        self.listPhases = QListView(PatternCenterDialog)
        self.listPhases.setObjectName(u"listPhases")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listPhases.sizePolicy().hasHeightForWidth())
        self.listPhases.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.listPhases)

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

        self.labelZStatr = QLabel(PatternCenterDialog)
        self.labelZStatr.setObjectName(u"labelZStatr")

        self.verticalLayout.addWidget(self.labelZStatr)

        self.spinBoxZ = QDoubleSpinBox(PatternCenterDialog)
        self.spinBoxZ.setObjectName(u"spinBoxZ")
        self.spinBoxZ.setDecimals(3)
        self.spinBoxZ.setMaximum(10.000000000000000)
        self.spinBoxZ.setSingleStep(0.001000000000000)

        self.verticalLayout.addWidget(self.spinBoxZ)

        self.labelMisfit = QLabel(PatternCenterDialog)
        self.labelMisfit.setObjectName(u"labelMisfit")

        self.verticalLayout.addWidget(self.labelMisfit)

        self.buttonTune = QPushButton(PatternCenterDialog)
        self.buttonTune.setObjectName(u"buttonTune")

        self.verticalLayout.addWidget(self.buttonTune)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(PatternCenterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy2)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(PatternCenterDialog)

        QMetaObject.connectSlotsByName(PatternCenterDialog)
    # setupUi

    def retranslateUi(self, PatternCenterDialog):
        PatternCenterDialog.setWindowTitle(QCoreApplication.translate("PatternCenterDialog", u"Pattern Center Refinement", None))
        self.buttonAddPhase.setText(QCoreApplication.translate("PatternCenterDialog", u"Add Phase", None))
        self.labelXStar.setText(QCoreApplication.translate("PatternCenterDialog", u"X-Star", None))
        self.labelYStar.setText(QCoreApplication.translate("PatternCenterDialog", u"Y-Star", None))
        self.labelZStatr.setText(QCoreApplication.translate("PatternCenterDialog", u"Z-Star", None))
        self.labelMisfit.setText(QCoreApplication.translate("PatternCenterDialog", u"Misfit (\u00b0):", None))
        self.buttonTune.setText(QCoreApplication.translate("PatternCenterDialog", u"Tune", None))
    # retranslateUi

