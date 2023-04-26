# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pc_selection.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_PCSelection(object):
    def setupUi(self, PCSelection):
        if not PCSelection.objectName():
            PCSelection.setObjectName(u"PCSelection")
        PCSelection.resize(1211, 753)
        self.horizontalLayout_6 = QHBoxLayout(PCSelection)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelNavigation = QLabel(PCSelection)
        self.labelNavigation.setObjectName(u"labelNavigation")

        self.horizontalLayout_9.addWidget(self.labelNavigation)

        self.labelIndex = QLabel(PCSelection)
        self.labelIndex.setObjectName(u"labelIndex")
        self.labelIndex.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.labelIndex)

        self.labelxy = QLabel(PCSelection)
        self.labelxy.setObjectName(u"labelxy")
        self.labelxy.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.labelxy)

        self.horizontalLayout_9.setStretch(0, 5)
        self.horizontalLayout_9.setStretch(1, 4)
        self.horizontalLayout_9.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.line_6 = QFrame(PCSelection)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.MplWidget = MplWidget(PCSelection)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setMinimumSize(QSize(400, 400))
        self.MplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_3.addWidget(self.MplWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelPhases = QLabel(PCSelection)
        self.labelPhases.setObjectName(u"labelPhases")

        self.verticalLayout.addWidget(self.labelPhases)

        self.line_4 = QFrame(PCSelection)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.listPhases = QListWidget(PCSelection)
        self.listPhases.setObjectName(u"listPhases")

        self.verticalLayout.addWidget(self.listPhases)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttonAddPhase = QPushButton(PCSelection)
        self.buttonAddPhase.setObjectName(u"buttonAddPhase")

        self.horizontalLayout_3.addWidget(self.buttonAddPhase)

        self.buttonRemovePhase = QPushButton(PCSelection)
        self.buttonRemovePhase.setObjectName(u"buttonRemovePhase")
        self.buttonRemovePhase.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.buttonRemovePhase)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(PCSelection)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelCalibrationPatterns = QLabel(PCSelection)
        self.labelCalibrationPatterns.setObjectName(u"labelCalibrationPatterns")

        self.verticalLayout.addWidget(self.labelCalibrationPatterns)

        self.line_5 = QFrame(PCSelection)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonGrid = QRadioButton(PCSelection)
        self.buttonGrid.setObjectName(u"buttonGrid")

        self.horizontalLayout_7.addWidget(self.buttonGrid)

        self.spinBoxGridX = QSpinBox(PCSelection)
        self.spinBoxGridX.setObjectName(u"spinBoxGridX")
        self.spinBoxGridX.setEnabled(False)
        self.spinBoxGridX.setMinimum(1)
        self.spinBoxGridX.setMaximum(12)
        self.spinBoxGridX.setValue(4)

        self.horizontalLayout_7.addWidget(self.spinBoxGridX)

        self.labelMultiplicator = QLabel(PCSelection)
        self.labelMultiplicator.setObjectName(u"labelMultiplicator")
        self.labelMultiplicator.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.labelMultiplicator)

        self.spinBoxGridY = QSpinBox(PCSelection)
        self.spinBoxGridY.setObjectName(u"spinBoxGridY")
        self.spinBoxGridY.setEnabled(False)
        self.spinBoxGridY.setMinimum(1)
        self.spinBoxGridY.setMaximum(12)
        self.spinBoxGridY.setValue(4)

        self.horizontalLayout_7.addWidget(self.spinBoxGridY)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.buttonUpdateGrid = QPushButton(PCSelection)
        self.buttonUpdateGrid.setObjectName(u"buttonUpdateGrid")
        self.buttonUpdateGrid.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.buttonUpdateGrid)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MplWidgetPattern = MplWidget(PCSelection)
        self.MplWidgetPattern.setObjectName(u"MplWidgetPattern")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidgetPattern.sizePolicy().hasHeightForWidth())
        self.MplWidgetPattern.setSizePolicy(sizePolicy)
        self.MplWidgetPattern.setMinimumSize(QSize(200, 200))
        self.MplWidgetPattern.setStyleSheet(u"background-color: transparent")

        self.horizontalLayout_2.addWidget(self.MplWidgetPattern)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listCoordinates = QListWidget(PCSelection)
        self.listCoordinates.setObjectName(u"listCoordinates")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listCoordinates.sizePolicy().hasHeightForWidth())
        self.listCoordinates.setSizePolicy(sizePolicy1)
        self.listCoordinates.setMinimumSize(QSize(0, 0))
        self.listCoordinates.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_2.addWidget(self.listCoordinates)

        self.buttonRemovePattern = QPushButton(PCSelection)
        self.buttonRemovePattern.setObjectName(u"buttonRemovePattern")
        self.buttonRemovePattern.setEnabled(False)

        self.verticalLayout_2.addWidget(self.buttonRemovePattern)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line_7 = QFrame(PCSelection)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPC = QLabel(PCSelection)
        self.labelPC.setObjectName(u"labelPC")

        self.horizontalLayout.addWidget(self.labelPC)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.labelXStar = QLabel(PCSelection)
        self.labelXStar.setObjectName(u"labelXStar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelXStar.sizePolicy().hasHeightForWidth())
        self.labelXStar.setSizePolicy(sizePolicy2)
        self.labelXStar.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.labelXStar)

        self.spinBoxX = QDoubleSpinBox(PCSelection)
        self.spinBoxX.setObjectName(u"spinBoxX")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBoxX.sizePolicy().hasHeightForWidth())
        self.spinBoxX.setSizePolicy(sizePolicy3)
        self.spinBoxX.setDecimals(4)
        self.spinBoxX.setMaximum(1.000000000000000)
        self.spinBoxX.setSingleStep(0.001000000000000)

        self.horizontalLayout.addWidget(self.spinBoxX)

        self.labelYStar = QLabel(PCSelection)
        self.labelYStar.setObjectName(u"labelYStar")

        self.horizontalLayout.addWidget(self.labelYStar)

        self.spinBoxY = QDoubleSpinBox(PCSelection)
        self.spinBoxY.setObjectName(u"spinBoxY")
        self.spinBoxY.setDecimals(4)
        self.spinBoxY.setMaximum(1.000000000000000)
        self.spinBoxY.setSingleStep(0.001000000000000)

        self.horizontalLayout.addWidget(self.spinBoxY)

        self.labelZStar = QLabel(PCSelection)
        self.labelZStar.setObjectName(u"labelZStar")

        self.horizontalLayout.addWidget(self.labelZStar)

        self.spinBoxZ = QDoubleSpinBox(PCSelection)
        self.spinBoxZ.setObjectName(u"spinBoxZ")
        self.spinBoxZ.setDecimals(4)
        self.spinBoxZ.setMaximum(3.000000000000000)
        self.spinBoxZ.setSingleStep(0.001000000000000)

        self.horizontalLayout.addWidget(self.spinBoxZ)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.conventionLabel = QLabel(PCSelection)
        self.conventionLabel.setObjectName(u"conventionLabel")

        self.horizontalLayout_8.addWidget(self.conventionLabel)

        self.conventionBox = QComboBox(PCSelection)
        self.conventionBox.addItem("")
        self.conventionBox.addItem("")
        self.conventionBox.setObjectName(u"conventionBox")

        self.horizontalLayout_8.addWidget(self.conventionBox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.line_3 = QFrame(PCSelection)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.workingDistanceLabel = QLabel(PCSelection)
        self.workingDistanceLabel.setObjectName(u"workingDistanceLabel")

        self.horizontalLayout_5.addWidget(self.workingDistanceLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label = QLabel(PCSelection)
        self.label.setObjectName(u"label")
        self.label.setToolTipDuration(-1)

        self.horizontalLayout_5.addWidget(self.label)

        self.spinBoxInlier = QDoubleSpinBox(PCSelection)
        self.spinBoxInlier.setObjectName(u"spinBoxInlier")
        self.spinBoxInlier.setMaximum(1.000000000000000)
        self.spinBoxInlier.setSingleStep(0.010000000000000)
        self.spinBoxInlier.setValue(0.400000000000000)

        self.horizontalLayout_5.addWidget(self.spinBoxInlier)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_2 = QFrame(PCSelection)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.buttonBox = QDialogButtonBox(PCSelection)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy4)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_10.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 50)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(12, 1)
        self.verticalLayout.setStretch(13, 1)
        self.verticalLayout.setStretch(14, 1)
        self.verticalLayout.setStretch(16, 1)
        self.verticalLayout.setStretch(17, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.retranslateUi(PCSelection)
        self.buttonBox.accepted.connect(PCSelection.accept)
        self.buttonBox.rejected.connect(PCSelection.reject)

        QMetaObject.connectSlotsByName(PCSelection)
    # setupUi

    def retranslateUi(self, PCSelection):
        PCSelection.setWindowTitle(QCoreApplication.translate("PCSelection", u"Pattern Center Refinement", None))
        self.labelNavigation.setText(QCoreApplication.translate("PCSelection", u"Navigation", None))
        self.labelIndex.setText(QCoreApplication.translate("PCSelection", u"Index:", None))
        self.labelxy.setText(QCoreApplication.translate("PCSelection", u"(x, y)", None))
        self.labelPhases.setText(QCoreApplication.translate("PCSelection", u"Phases", None))
        self.buttonAddPhase.setText(QCoreApplication.translate("PCSelection", u"Add Phase", None))
        self.buttonRemovePhase.setText(QCoreApplication.translate("PCSelection", u"Remove Phase", None))
        self.labelCalibrationPatterns.setText(QCoreApplication.translate("PCSelection", u"Calibration patterns", None))
        self.buttonGrid.setText(QCoreApplication.translate("PCSelection", u"Grid     ", None))
        self.labelMultiplicator.setText(QCoreApplication.translate("PCSelection", u"x", None))
        self.buttonUpdateGrid.setText(QCoreApplication.translate("PCSelection", u"Update grid", None))
        self.buttonRemovePattern.setText(QCoreApplication.translate("PCSelection", u"Remove Pattern", None))
        self.labelPC.setText(QCoreApplication.translate("PCSelection", u"Pattern center:", None))
        self.labelXStar.setText(QCoreApplication.translate("PCSelection", u"X:", None))
        self.labelYStar.setText(QCoreApplication.translate("PCSelection", u"Y:", None))
        self.labelZStar.setText(QCoreApplication.translate("PCSelection", u"Z:", None))
        self.conventionLabel.setText(QCoreApplication.translate("PCSelection", u"PC Convention", None))
        self.conventionBox.setItemText(0, QCoreApplication.translate("PCSelection", u"BRUKER", None))
        self.conventionBox.setItemText(1, QCoreApplication.translate("PCSelection", u"TSL", None))

        self.workingDistanceLabel.setText(QCoreApplication.translate("PCSelection", u"Working Distance (mm): 0.0", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PCSelection", u"Inlier criteria", None))
    # retranslateUi

