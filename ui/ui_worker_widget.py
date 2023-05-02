# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_WorkerWidget(object):
    def setupUi(self, WorkerWidget):
        if not WorkerWidget.objectName():
            WorkerWidget.setObjectName(u"WorkerWidget")
        WorkerWidget.resize(423, 230)
        WorkerWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(WorkerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButtonShow = QPushButton(WorkerWidget)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setStyleSheet(u"QPushButton:focus {\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"QPushButton:checked {\n"
"	selection-background-color: rgba(255, 255, 255, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"QPushButton:pressed {\n"
"	selection-background-color: rgba(255, 255, 255, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	outline: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/linea_arrows/resources/linea_arrows_icons/arrows_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/linea_arrows/resources/linea_arrows_icons/arrows_down.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButtonShow.setIcon(icon)
        self.pushButtonShow.setCheckable(True)
        self.pushButtonShow.setChecked(True)
        self.pushButtonShow.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButtonShow)

        self.labelJobNumber = QLabel(WorkerWidget)
        self.labelJobNumber.setObjectName(u"labelJobNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelJobNumber.sizePolicy().hasHeightForWidth())
        self.labelJobNumber.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.labelJobNumber)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelTime = QLabel(WorkerWidget)
        self.labelTime.setObjectName(u"labelTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelTime.sizePolicy().hasHeightForWidth())
        self.labelTime.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.labelTime.setFont(font)
        self.labelTime.setStyleSheet(u"color: rgb(220, 190, 0);")

        self.horizontalLayout.addWidget(self.labelTime)

        self.pushButtonCancel = QPushButton(WorkerWidget)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy2)
        self.pushButtonCancel.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButtonCancel)

        self.pushButtonRemove = QPushButton(WorkerWidget)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")
        self.pushButtonRemove.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButtonRemove.sizePolicy().hasHeightForWidth())
        self.pushButtonRemove.setSizePolicy(sizePolicy3)
        self.pushButtonRemove.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/linea_basic/resources/linea_basic_icons/basic_trashcan.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRemove.setIcon(icon1)
        self.pushButtonRemove.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButtonRemove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(WorkerWidget)
        self.line.setObjectName(u"line")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy4)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelJobName = QLabel(WorkerWidget)
        self.labelJobName.setObjectName(u"labelJobName")
        sizePolicy1.setHeightForWidth(self.labelJobName.sizePolicy().hasHeightForWidth())
        self.labelJobName.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.labelJobName.setFont(font1)

        self.verticalLayout.addWidget(self.labelJobName)

        self.labelOutput = QLabel(WorkerWidget)
        self.labelOutput.setObjectName(u"labelOutput")
        sizePolicy1.setHeightForWidth(self.labelOutput.sizePolicy().hasHeightForWidth())
        self.labelOutput.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setItalic(True)
        font2.setUnderline(True)
        self.labelOutput.setFont(font2)
        self.labelOutput.setStyleSheet(u"color: rgb(100, 100, 100);")

        self.verticalLayout.addWidget(self.labelOutput)

        self.textBrowserStatus = QTextBrowser(WorkerWidget)
        self.textBrowserStatus.setObjectName(u"textBrowserStatus")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowserStatus.sizePolicy().hasHeightForWidth())
        self.textBrowserStatus.setSizePolicy(sizePolicy5)
        self.textBrowserStatus.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowserStatus.setStyleSheet(u"font: 8pt \"Cascadia Code\";\n"
"color: rgb(0, 0, 255);")

        self.verticalLayout.addWidget(self.textBrowserStatus)

        self.lineBrowser = QFrame(WorkerWidget)
        self.lineBrowser.setObjectName(u"lineBrowser")
        sizePolicy4.setHeightForWidth(self.lineBrowser.sizePolicy().hasHeightForWidth())
        self.lineBrowser.setSizePolicy(sizePolicy4)
        self.lineBrowser.setFrameShape(QFrame.HLine)
        self.lineBrowser.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.lineBrowser)

        self.verticalLayout.setStretch(4, 1)
        QWidget.setTabOrder(self.pushButtonShow, self.pushButtonCancel)
        QWidget.setTabOrder(self.pushButtonCancel, self.pushButtonRemove)
        QWidget.setTabOrder(self.pushButtonRemove, self.textBrowserStatus)

        self.retranslateUi(WorkerWidget)
        self.pushButtonShow.toggled.connect(self.textBrowserStatus.setVisible)
        self.pushButtonShow.toggled.connect(self.labelJobName.setVisible)
        self.pushButtonShow.toggled.connect(self.labelOutput.setVisible)
        self.pushButtonShow.toggled.connect(self.lineBrowser.setVisible)

        QMetaObject.connectSlotsByName(WorkerWidget)
    # setupUi

    def retranslateUi(self, WorkerWidget):
        WorkerWidget.setWindowTitle(QCoreApplication.translate("WorkerWidget", u"Form", None))
        self.pushButtonShow.setText("")
        self.labelJobNumber.setText(QCoreApplication.translate("WorkerWidget", u"job number", None))
        self.labelTime.setText(QCoreApplication.translate("WorkerWidget", u"In Queue", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCancel.setToolTip(QCoreApplication.translate("WorkerWidget", u"Cancel job", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCancel.setText(QCoreApplication.translate("WorkerWidget", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemove.setToolTip(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>Visibly remove job from manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemove.setText("")
        self.labelJobName.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>job name</p></body></html>", None))
        self.labelOutput.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>output_directory</p></body></html>", None))
        self.textBrowserStatus.setHtml(QCoreApplication.translate("WorkerWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cascadia Code'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

