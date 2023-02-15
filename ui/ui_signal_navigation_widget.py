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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_SignalNavigationWidget(object):
    def setupUi(self, SignalNavigationWidget):
        if not SignalNavigationWidget.objectName():
            SignalNavigationWidget.setObjectName(u"SignalNavigationWidget")
        SignalNavigationWidget.resize(591, 317)
        self.gridLayout = QGridLayout(SignalNavigationWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navigatorLabel = QLabel(SignalNavigationWidget)
        self.navigatorLabel.setObjectName(u"navigatorLabel")

        self.verticalLayout.addWidget(self.navigatorLabel)

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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonMeanNav = QPushButton(SignalNavigationWidget)
        self.pushButtonMeanNav.setObjectName(u"pushButtonMeanNav")

        self.horizontalLayout.addWidget(self.pushButtonMeanNav)

        self.pushButtonIQNav = QPushButton(SignalNavigationWidget)
        self.pushButtonIQNav.setObjectName(u"pushButtonIQNav")

        self.horizontalLayout.addWidget(self.pushButtonIQNav)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(SignalNavigationWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.signalLabel = QLabel(SignalNavigationWidget)
        self.signalLabel.setObjectName(u"signalLabel")

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

        self.verticalLayout_2.addWidget(self.checkBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(SignalNavigationWidget)

        QMetaObject.connectSlotsByName(SignalNavigationWidget)
    # setupUi

    def retranslateUi(self, SignalNavigationWidget):
        SignalNavigationWidget.setWindowTitle(QCoreApplication.translate("SignalNavigationWidget", u"Form", None))
        self.navigatorLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Dataset", None))
#if QT_CONFIG(whatsthis)
        self.pushButtonMeanNav.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButtonMeanNav.setText(QCoreApplication.translate("SignalNavigationWidget", u"Mean instensity", None))
        self.pushButtonIQNav.setText(QCoreApplication.translate("SignalNavigationWidget", u"Image quality", None))
        self.signalLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Index", None))
        self.signalIndex.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.checkBox.setText(QCoreApplication.translate("SignalNavigationWidget", u"Gemoetrical simulation", None))
    # retranslateUi

