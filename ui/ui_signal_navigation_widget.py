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
        self.navigatorLabel = QLabel(SignalNavigationWidget)
        self.navigatorLabel.setObjectName(u"navigatorLabel")

        self.horizontalLayout_3.addWidget(self.navigatorLabel)

        self.navigatorCoordinates = QLabel(SignalNavigationWidget)
        self.navigatorCoordinates.setObjectName(u"navigatorCoordinates")

        self.horizontalLayout_3.addWidget(self.navigatorCoordinates)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.line = QFrame(SignalNavigationWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)

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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalMplWidget.sizePolicy().hasHeightForWidth())
        self.signalMplWidget.setSizePolicy(sizePolicy)
        self.signalMplWidget.setMinimumSize(QSize(0, 0))
        self.signalMplWidget.setAutoFillBackground(False)
        self.signalMplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_2.addWidget(self.signalMplWidget)

        self.checkBox = QCheckBox(SignalNavigationWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 3, 1)

        self.navigatorMplWidget = MplWidget(SignalNavigationWidget)
        self.navigatorMplWidget.setObjectName(u"navigatorMplWidget")
        self.navigatorMplWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.navigatorMplWidget.sizePolicy().hasHeightForWidth())
        self.navigatorMplWidget.setSizePolicy(sizePolicy)
        self.navigatorMplWidget.setMinimumSize(QSize(0, 0))
        self.navigatorMplWidget.setAutoFillBackground(False)
        self.navigatorMplWidget.setStyleSheet(u"background-color: transparent")

        self.gridLayout.addWidget(self.navigatorMplWidget, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonNav_1 = QPushButton(SignalNavigationWidget)
        self.pushButtonNav_1.setObjectName(u"pushButtonNav_1")

        self.horizontalLayout.addWidget(self.pushButtonNav_1)

        self.pushButtonNav_2 = QPushButton(SignalNavigationWidget)
        self.pushButtonNav_2.setObjectName(u"pushButtonNav_2")

        self.horizontalLayout.addWidget(self.pushButtonNav_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(SignalNavigationWidget)

        QMetaObject.connectSlotsByName(SignalNavigationWidget)
    # setupUi

    def retranslateUi(self, SignalNavigationWidget):
        SignalNavigationWidget.setWindowTitle(QCoreApplication.translate("SignalNavigationWidget", u"Form", None))
        self.navigatorLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Dataset", None))
        self.navigatorCoordinates.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.signalLabel.setText(QCoreApplication.translate("SignalNavigationWidget", u"Index", None))
        self.signalIndex.setText(QCoreApplication.translate("SignalNavigationWidget", u"(x, y)", None))
        self.checkBox.setText(QCoreApplication.translate("SignalNavigationWidget", u"Geometrical simulation", None))
#if QT_CONFIG(whatsthis)
        self.pushButtonNav_1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButtonNav_1.setText(QCoreApplication.translate("SignalNavigationWidget", u"Mean instensity", None))
        self.pushButtonNav_2.setText(QCoreApplication.translate("SignalNavigationWidget", u"Image quality", None))
    # retranslateUi

