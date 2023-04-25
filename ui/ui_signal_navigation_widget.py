# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal_navigation_widget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_SignalNavigationWidget(object):
    def setupUi(self, SignalNavigationWidget):
        if not SignalNavigationWidget.objectName():
            SignalNavigationWidget.setObjectName(u"SignalNavigationWidget")
        SignalNavigationWidget.resize(842, 532)
        self.gridLayout_3 = QGridLayout(SignalNavigationWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonBox = QDialogButtonBox(SignalNavigationWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(16777215, 16777215))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_3.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.signalLabel = QLabel(SignalNavigationWidget)
        self.signalLabel.setObjectName(u"signalLabel")
        self.signalLabel.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.signalLabel.setFont(font)
        self.signalLabel.setTextFormat(Qt.AutoText)
        self.signalLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.signalLabel)

        self.line_3 = QFrame(SignalNavigationWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.signalMplWidget = MplWidget(SignalNavigationWidget)
        self.signalMplWidget.setObjectName(u"signalMplWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalMplWidget.sizePolicy().hasHeightForWidth())
        self.signalMplWidget.setSizePolicy(sizePolicy)
        self.signalMplWidget.setMinimumSize(QSize(200, 200))
        font1 = QFont()
        font1.setKerning(True)
        self.signalMplWidget.setFont(font1)
        self.signalMplWidget.setCursor(QCursor(Qt.CrossCursor))
        self.signalMplWidget.setAcceptDrops(False)
        self.signalMplWidget.setAutoFillBackground(False)
        self.signalMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_2.addWidget(self.signalMplWidget)

        self.line_6 = QFrame(SignalNavigationWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.signalIndex = QLabel(SignalNavigationWidget)
        self.signalIndex.setObjectName(u"signalIndex")

        self.gridLayout_2.addWidget(self.signalIndex, 0, 1, 1, 1)

        self.LabelPhase2 = QLabel(SignalNavigationWidget)
        self.LabelPhase2.setObjectName(u"LabelPhase2")
        self.LabelPhase2.setFont(font1)
        self.LabelPhase2.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.LabelPhase2, 0, 2, 1, 1)

        self.labelPhaseClick = QLabel(SignalNavigationWidget)
        self.labelPhaseClick.setObjectName(u"labelPhaseClick")

        self.gridLayout_2.addWidget(self.labelPhaseClick, 0, 3, 1, 1)

        self.label_4 = QLabel(SignalNavigationWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.checkBox = QCheckBox(SignalNavigationWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigatorLabel = QLabel(SignalNavigationWidget)
        self.navigatorLabel.setObjectName(u"navigatorLabel")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        self.navigatorLabel.setFont(font2)
        self.navigatorLabel.setScaledContents(False)

        self.verticalLayout.addWidget(self.navigatorLabel)

        self.line_2 = QFrame(SignalNavigationWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(SignalNavigationWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBoxNavigator = QComboBox(SignalNavigationWidget)
        self.comboBoxNavigator.setObjectName(u"comboBoxNavigator")

        self.gridLayout.addWidget(self.comboBoxNavigator, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelPhaseHover = QLabel(SignalNavigationWidget)
        self.labelPhaseHover.setObjectName(u"labelPhaseHover")
        self.labelPhaseHover.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.labelPhaseHover, 0, 3, 1, 1)

        self.navigatorCoordinates = QLabel(SignalNavigationWidget)
        self.navigatorCoordinates.setObjectName(u"navigatorCoordinates")
        self.navigatorCoordinates.setMinimumSize(QSize(60, 0))

        self.gridLayout_4.addWidget(self.navigatorCoordinates, 0, 1, 1, 1)

        self.label_7 = QLabel(SignalNavigationWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.labelPhase1 = QLabel(SignalNavigationWidget)
        self.labelPhase1.setObjectName(u"labelPhase1")

        self.gridLayout_4.addWidget(self.labelPhase1, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.line_4 = QFrame(SignalNavigationWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.navigatorMplWidget = MplWidget(SignalNavigationWidget)
        self.navigatorMplWidget.setObjectName(u"navigatorMplWidget")
        self.navigatorMplWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.navigatorMplWidget.sizePolicy().hasHeightForWidth())
        self.navigatorMplWidget.setSizePolicy(sizePolicy)
        self.navigatorMplWidget.setMinimumSize(QSize(200, 200))
        self.navigatorMplWidget.setCursor(QCursor(Qt.CrossCursor))
        self.navigatorMplWidget.setAutoFillBackground(False)
        self.navigatorMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout.addWidget(self.navigatorMplWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.comboBoxNavigator, self.checkBox)

        self.retranslateUi(SignalNavigationWidget)

        QMetaObject.connectSlotsByName(SignalNavigationWidget)
    # setupUi

    def retranslateUi(self, SignalNavigationWidget):
        SignalNavigationWidget.setWindowTitle(QCoreApplication.translate("SignalNavigationWidget", u"Form", None))
        self.signalLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"EBSD signal", None))
        self.signalIndex.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.LabelPhase2.setText(QCoreApplication.translate("SignalNavigationWidget", u"Phase:", None))
        self.labelPhaseClick.setText("")
        self.label_4.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation index:", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("SignalNavigationWidget", u"<html><head/><body><p>Simulate positions of Kikuchi lines and zone axes onto the experimental EBSD signal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("SignalNavigationWidget", u"Show geometrical simulation", None))
        self.navigatorLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation", None))
        self.label.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigator:", None))
        self.labelPhaseHover.setText("")
        self.navigatorCoordinates.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.label_7.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation index:", None))
        self.labelPhase1.setText(QCoreApplication.translate("SignalNavigationWidget", u"Phase:", None))
    # retranslateUi

