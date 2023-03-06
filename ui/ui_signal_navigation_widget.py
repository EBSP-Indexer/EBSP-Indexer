# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal_navigation_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_SignalNavigationWidget(object):
    def setupUi(self, SignalNavigationWidget):
        if not SignalNavigationWidget.objectName():
            SignalNavigationWidget.setObjectName(u"SignalNavigationWidget")
        SignalNavigationWidget.resize(648, 392)
        self.gridLayout_3 = QGridLayout(SignalNavigationWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigatorLabel = QLabel(SignalNavigationWidget)
        self.navigatorLabel.setObjectName(u"navigatorLabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.navigatorLabel.setFont(font)
        self.navigatorLabel.setScaledContents(False)

        self.verticalLayout.addWidget(self.navigatorLabel)

        self.line_2 = QFrame(SignalNavigationWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelPhase1 = QLabel(SignalNavigationWidget)
        self.labelPhase1.setObjectName(u"labelPhase1")

        self.horizontalLayout_3.addWidget(self.labelPhase1)

        self.labelPhaseHover = QLabel(SignalNavigationWidget)
        self.labelPhaseHover.setObjectName(u"labelPhaseHover")
        self.labelPhaseHover.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.labelPhaseHover)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.label = QLabel(SignalNavigationWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.comboBoxNavigator = QComboBox(SignalNavigationWidget)
        self.comboBoxNavigator.setObjectName(u"comboBoxNavigator")

        self.gridLayout.addWidget(self.comboBoxNavigator, 1, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(SignalNavigationWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.navigatorCoordinates = QLabel(SignalNavigationWidget)
        self.navigatorCoordinates.setObjectName(u"navigatorCoordinates")

        self.horizontalLayout.addWidget(self.navigatorCoordinates)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line_4 = QFrame(SignalNavigationWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.navigatorMplWidget = MplWidget(SignalNavigationWidget)
        self.navigatorMplWidget.setObjectName(u"navigatorMplWidget")
        self.navigatorMplWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigatorMplWidget.sizePolicy().hasHeightForWidth())
        self.navigatorMplWidget.setSizePolicy(sizePolicy)
        self.navigatorMplWidget.setMinimumSize(QSize(0, 0))
        self.navigatorMplWidget.setCursor(QCursor(Qt.CrossCursor))
        self.navigatorMplWidget.setAutoFillBackground(False)
        self.navigatorMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout.addWidget(self.navigatorMplWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 1)

        self.line = QFrame(SignalNavigationWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 1, 2, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.signalLabel = QLabel(SignalNavigationWidget)
        self.signalLabel.setObjectName(u"signalLabel")
        self.signalLabel.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.signalLabel.setFont(font1)
        self.signalLabel.setTextFormat(Qt.AutoText)
        self.signalLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.signalLabel)

        self.line_3 = QFrame(SignalNavigationWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LabelPhase2 = QLabel(SignalNavigationWidget)
        self.LabelPhase2.setObjectName(u"LabelPhase2")
        font2 = QFont()
        font2.setKerning(True)
        self.LabelPhase2.setFont(font2)
        self.LabelPhase2.setAutoFillBackground(False)

        self.horizontalLayout_5.addWidget(self.LabelPhase2)

        self.labelPhaseClick = QLabel(SignalNavigationWidget)
        self.labelPhaseClick.setObjectName(u"labelPhaseClick")

        self.horizontalLayout_5.addWidget(self.labelPhaseClick)

        self.label_6 = QLabel(SignalNavigationWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(SignalNavigationWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.signalIndex = QLabel(SignalNavigationWidget)
        self.signalIndex.setObjectName(u"signalIndex")

        self.horizontalLayout_2.addWidget(self.signalIndex)

        self.label_3 = QLabel(SignalNavigationWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_6 = QFrame(SignalNavigationWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.signalMplWidget = MplWidget(SignalNavigationWidget)
        self.signalMplWidget.setObjectName(u"signalMplWidget")
        sizePolicy.setHeightForWidth(self.signalMplWidget.sizePolicy().hasHeightForWidth())
        self.signalMplWidget.setSizePolicy(sizePolicy)
        self.signalMplWidget.setMinimumSize(QSize(0, 0))
        self.signalMplWidget.setCursor(QCursor(Qt.CrossCursor))
        self.signalMplWidget.setAutoFillBackground(False)
        self.signalMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_2.addWidget(self.signalMplWidget)

        self.checkBox = QCheckBox(SignalNavigationWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.line_5 = QFrame(SignalNavigationWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButtonExportImage = QPushButton(SignalNavigationWidget)
        self.pushButtonExportImage.setObjectName(u"pushButtonExportImage")

        self.horizontalLayout_4.addWidget(self.pushButtonExportImage)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 3, 1, 1)


        self.retranslateUi(SignalNavigationWidget)

        QMetaObject.connectSlotsByName(SignalNavigationWidget)
    # setupUi

    def retranslateUi(self, SignalNavigationWidget):
        SignalNavigationWidget.setWindowTitle(QCoreApplication.translate("SignalNavigationWidget", u"Form", None))
        self.navigatorLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation", None))
        self.labelPhase1.setText(QCoreApplication.translate("SignalNavigationWidget", u"Phase:", None))
        self.labelPhaseHover.setText("")
        self.label.setText(QCoreApplication.translate("SignalNavigationWidget", u"Select navigator:", None))
        self.label_7.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation index:", None))
        self.navigatorCoordinates.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.signalLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"EBSD signal", None))
        self.LabelPhase2.setText(QCoreApplication.translate("SignalNavigationWidget", u"Phase:", None))
        self.labelPhaseClick.setText("")
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation index:", None))
        self.signalIndex.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("SignalNavigationWidget", u"<html><head/><body><p>Simulate positions of Kikuchi lines and zone axes onto the experimental EBSD signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("SignalNavigationWidget", u"Show geometrical simulation", None))
        self.pushButtonExportImage.setText(QCoreApplication.translate("SignalNavigationWidget", u"Save image", None))
    # retranslateUi

