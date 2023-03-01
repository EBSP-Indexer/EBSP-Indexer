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
        SignalNavigationWidget.resize(645, 392)
        self.gridLayout = QGridLayout(SignalNavigationWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navigatorLabel = QLabel(SignalNavigationWidget)
        self.navigatorLabel.setObjectName(u"navigatorLabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.navigatorLabel.setFont(font)
        self.navigatorLabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.navigatorLabel)

        self.navigatorCoordinates = QLabel(SignalNavigationWidget)
        self.navigatorCoordinates.setObjectName(u"navigatorCoordinates")

        self.horizontalLayout.addWidget(self.navigatorCoordinates)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(SignalNavigationWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBoxNavigator = QComboBox(SignalNavigationWidget)
        self.comboBoxNavigator.setObjectName(u"comboBoxNavigator")

        self.horizontalLayout_3.addWidget(self.comboBoxNavigator)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.navigatorMplWidget = MplWidget(SignalNavigationWidget)
        self.navigatorMplWidget.setObjectName(u"navigatorMplWidget")
        self.navigatorMplWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigatorMplWidget.sizePolicy().hasHeightForWidth())
        self.navigatorMplWidget.setSizePolicy(sizePolicy)
        self.navigatorMplWidget.setMinimumSize(QSize(0, 0))
        self.navigatorMplWidget.setAutoFillBackground(False)
        self.navigatorMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout.addWidget(self.navigatorMplWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.signalLabel = QLabel(SignalNavigationWidget)
        self.signalLabel.setObjectName(u"signalLabel")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.signalLabel.setFont(font1)
        self.signalLabel.setTextFormat(Qt.AutoText)

        self.horizontalLayout_2.addWidget(self.signalLabel)

        self.signalIndex = QLabel(SignalNavigationWidget)
        self.signalIndex.setObjectName(u"signalIndex")

        self.horizontalLayout_2.addWidget(self.signalIndex)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.signalMplWidget = MplWidget(SignalNavigationWidget)
        self.signalMplWidget.setObjectName(u"signalMplWidget")
        sizePolicy.setHeightForWidth(self.signalMplWidget.sizePolicy().hasHeightForWidth())
        self.signalMplWidget.setSizePolicy(sizePolicy)
        self.signalMplWidget.setMinimumSize(QSize(0, 0))
        self.signalMplWidget.setAutoFillBackground(False)
        self.signalMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_2.addWidget(self.signalMplWidget)

        self.checkBox = QCheckBox(SignalNavigationWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)

        self.verticalLayout_2.addWidget(self.checkBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.line = QFrame(SignalNavigationWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)

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
        self.horizontalLayout_4.setStretch(1, 3)

        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 3, 1, 1)


        self.retranslateUi(SignalNavigationWidget)

        QMetaObject.connectSlotsByName(SignalNavigationWidget)
    # setupUi

    def retranslateUi(self, SignalNavigationWidget):
        SignalNavigationWidget.setWindowTitle(QCoreApplication.translate("SignalNavigationWidget", u"Form", None))
        self.navigatorLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Navigation:", None))
        self.navigatorCoordinates.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.label.setText(QCoreApplication.translate("SignalNavigationWidget", u"Select navigator:", None))
        self.signalLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"EBSD signal:", None))
        self.signalIndex.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.checkBox.setText(QCoreApplication.translate("SignalNavigationWidget", u"Geometrical simulation", None))
        self.pushButtonExportImage.setText(QCoreApplication.translate("SignalNavigationWidget", u"Export image", None))
    # retranslateUi

