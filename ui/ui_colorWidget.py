# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colorWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QToolButton,
    QWidget)

class Ui_colorPicker(object):
    def setupUi(self, colorPicker):
        if not colorPicker.objectName():
            colorPicker.setObjectName(u"colorPicker")
        colorPicker.resize(200, 200)
        colorPicker.setMinimumSize(QSize(200, 200))
        self.gridLayout = QGridLayout(colorPicker)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_11 = QToolButton(colorPicker)
        self.toolButton_11.setObjectName(u"toolButton_11")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_11.sizePolicy().hasHeightForWidth())
        self.toolButton_11.setSizePolicy(sizePolicy)
        self.toolButton_11.setStyleSheet(u"background-color: rgb(255, 255, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_11, 2, 3, 1, 1)

        self.toolButton = QToolButton(colorPicker)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet(u"background-color: rgb(0, 0, 255)\n"
"")

        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)

        self.toolButton_4 = QToolButton(colorPicker)
        self.toolButton_4.setObjectName(u"toolButton_4")
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setStyleSheet(u"background-color: rgb(0, 191, 191)")

        self.gridLayout.addWidget(self.toolButton_4, 0, 4, 1, 1)

        self.toolButton_2 = QToolButton(colorPicker)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setStyleSheet(u"background-color:rgb(0, 128, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_2, 0, 1, 1, 1)

        self.toolButton_12 = QToolButton(colorPicker)
        self.toolButton_12.setObjectName(u"toolButton_12")
        sizePolicy.setHeightForWidth(self.toolButton_12.sizePolicy().hasHeightForWidth())
        self.toolButton_12.setSizePolicy(sizePolicy)
        self.toolButton_12.setStyleSheet(u"background-color: rgb(0, 255, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_12, 2, 4, 1, 1)

        self.toolButton_10 = QToolButton(colorPicker)
        self.toolButton_10.setObjectName(u"toolButton_10")
        sizePolicy.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy)
        self.toolButton_10.setStyleSheet(u"background-color:rgb(255, 165, 0)")

        self.gridLayout.addWidget(self.toolButton_10, 2, 1, 1, 1)

        self.toolButton_9 = QToolButton(colorPicker)
        self.toolButton_9.setObjectName(u"toolButton_9")
        sizePolicy.setHeightForWidth(self.toolButton_9.sizePolicy().hasHeightForWidth())
        self.toolButton_9.setSizePolicy(sizePolicy)
        self.toolButton_9.setStyleSheet(u"background-color: rgb(0, 255, 255)\n"
"")

        self.gridLayout.addWidget(self.toolButton_9, 2, 0, 1, 1)

        self.toolButton_7 = QToolButton(colorPicker)
        self.toolButton_7.setObjectName(u"toolButton_7")
        sizePolicy.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy)
        self.toolButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255)\n"
"")

        self.gridLayout.addWidget(self.toolButton_7, 1, 3, 1, 1)

        self.toolButton_8 = QToolButton(colorPicker)
        self.toolButton_8.setObjectName(u"toolButton_8")
        sizePolicy.setHeightForWidth(self.toolButton_8.sizePolicy().hasHeightForWidth())
        self.toolButton_8.setSizePolicy(sizePolicy)
        self.toolButton_8.setStyleSheet(u"background-color: rgb(0, 0, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_8, 1, 4, 1, 1)

        self.toolButton_3 = QToolButton(colorPicker)
        self.toolButton_3.setObjectName(u"toolButton_3")
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setStyleSheet(u"background-color: rgb(255, 0, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_3, 0, 3, 1, 1)

        self.toolButton_6 = QToolButton(colorPicker)
        self.toolButton_6.setObjectName(u"toolButton_6")
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setStyleSheet(u"background-color: rgb(191, 191, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_6, 1, 1, 1, 1)

        self.toolButton_5 = QToolButton(colorPicker)
        self.toolButton_5.setObjectName(u"toolButton_5")
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setStyleSheet(u"background-color: rgb(191, 0, 191)\n"
"")

        self.gridLayout.addWidget(self.toolButton_5, 1, 0, 1, 1)

        self.toolButton_13 = QToolButton(colorPicker)
        self.toolButton_13.setObjectName(u"toolButton_13")
        sizePolicy.setHeightForWidth(self.toolButton_13.sizePolicy().hasHeightForWidth())
        self.toolButton_13.setSizePolicy(sizePolicy)
        self.toolButton_13.setStyleSheet(u"background-color: rgb(165, 42, 42)\n"
"")

        self.gridLayout.addWidget(self.toolButton_13, 3, 0, 1, 1)

        self.toolButton_14 = QToolButton(colorPicker)
        self.toolButton_14.setObjectName(u"toolButton_14")
        sizePolicy.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy)
        self.toolButton_14.setStyleSheet(u"background-color:rgb(255, 192, 203)")

        self.gridLayout.addWidget(self.toolButton_14, 3, 1, 1, 1)

        self.toolButton_15 = QToolButton(colorPicker)
        self.toolButton_15.setObjectName(u"toolButton_15")
        sizePolicy.setHeightForWidth(self.toolButton_15.sizePolicy().hasHeightForWidth())
        self.toolButton_15.setSizePolicy(sizePolicy)
        self.toolButton_15.setStyleSheet(u"background-color: rgb(128, 128, 128)\n"
"")

        self.gridLayout.addWidget(self.toolButton_15, 3, 3, 1, 1)

        self.toolButton_16 = QToolButton(colorPicker)
        self.toolButton_16.setObjectName(u"toolButton_16")
        sizePolicy.setHeightForWidth(self.toolButton_16.sizePolicy().hasHeightForWidth())
        self.toolButton_16.setSizePolicy(sizePolicy)
        self.toolButton_16.setStyleSheet(u"background-color: rgb(128, 128, 0)\n"
"")

        self.gridLayout.addWidget(self.toolButton_16, 3, 4, 1, 1)


        self.retranslateUi(colorPicker)

        QMetaObject.connectSlotsByName(colorPicker)
    # setupUi

    def retranslateUi(self, colorPicker):
        colorPicker.setWindowTitle(QCoreApplication.translate("colorPicker", u"Form", None))
        self.toolButton_11.setText("")
        self.toolButton.setText("")
        self.toolButton_4.setText("")
        self.toolButton_2.setText("")
        self.toolButton_12.setText("")
        self.toolButton_10.setText("")
        self.toolButton_9.setText("")
        self.toolButton_7.setText("")
        self.toolButton_8.setText("")
        self.toolButton_3.setText("")
        self.toolButton_6.setText("")
        self.toolButton_5.setText("")
        self.toolButton_13.setText("")
        self.toolButton_14.setText("")
        self.toolButton_15.setText("")
        self.toolButton_16.setText("")
    # retranslateUi

