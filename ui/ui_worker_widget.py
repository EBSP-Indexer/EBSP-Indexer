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
        WorkerWidget.resize(504, 387)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WorkerWidget.sizePolicy().hasHeightForWidth())
        WorkerWidget.setSizePolicy(sizePolicy)
        WorkerWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(WorkerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.labelJobNumber = QLabel(WorkerWidget)
        self.labelJobNumber.setObjectName(u"labelJobNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelJobNumber.sizePolicy().hasHeightForWidth())
        self.labelJobNumber.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.labelJobNumber)

        self.pushButtonShow = QPushButton(WorkerWidget)
        self.pushButtonShow.setObjectName(u"pushButtonShow")
        self.pushButtonShow.setStyleSheet(u"QPushButton:focus {\n"
"	border: none;\n"
"	outline: none;\n"
"}\n"
"QPushButton:checked {\n"
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

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelTime = QLabel(WorkerWidget)
        self.labelTime.setObjectName(u"labelTime")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelTime.sizePolicy().hasHeightForWidth())
        self.labelTime.setSizePolicy(sizePolicy2)
        self.labelTime.setStyleSheet(u"color: rgb(220, 190, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.labelTime)

        self.pushButtonCancel = QPushButton(WorkerWidget)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        icon1 = QIcon()
        icon1.addFile(u":/linea_arrows/resources/linea_arrows_icons/arrows_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCancel.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/linea_basic/resources/linea_basic_icons/basic_trashcan.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRemove.setIcon(icon2)
        self.pushButtonRemove.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButtonRemove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(WorkerWidget)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelJobName = QLabel(WorkerWidget)
        self.labelJobName.setObjectName(u"labelJobName")
        sizePolicy2.setHeightForWidth(self.labelJobName.sizePolicy().hasHeightForWidth())
        self.labelJobName.setSizePolicy(sizePolicy2)
        self.labelJobName.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")

        self.verticalLayout.addWidget(self.labelJobName)

        self.labelOutput = QLabel(WorkerWidget)
        self.labelOutput.setObjectName(u"labelOutput")
        sizePolicy2.setHeightForWidth(self.labelOutput.sizePolicy().hasHeightForWidth())
        self.labelOutput.setSizePolicy(sizePolicy2)
        self.labelOutput.setStyleSheet(u"font: italic 8pt \"MS Sans Serif\";\n"
"color: rgb(120, 120, 120);")

        self.verticalLayout.addWidget(self.labelOutput)

        self.textBrowserStatus = QTextBrowser(WorkerWidget)
        self.textBrowserStatus.setObjectName(u"textBrowserStatus")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textBrowserStatus.sizePolicy().hasHeightForWidth())
        self.textBrowserStatus.setSizePolicy(sizePolicy4)
        self.textBrowserStatus.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowserStatus.setStyleSheet(u"font: 8pt \"Cascadia Code\";\n"
"color: rgb(0, 0, 255);")

        self.verticalLayout.addWidget(self.textBrowserStatus)

        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(WorkerWidget)
        self.pushButtonShow.toggled.connect(self.textBrowserStatus.setVisible)
        self.pushButtonShow.toggled.connect(self.labelJobName.setVisible)
        self.pushButtonShow.toggled.connect(self.labelOutput.setVisible)

        QMetaObject.connectSlotsByName(WorkerWidget)
    # setupUi

    def retranslateUi(self, WorkerWidget):
        WorkerWidget.setWindowTitle(QCoreApplication.translate("WorkerWidget", u"Form", None))
        self.labelJobNumber.setText(QCoreApplication.translate("WorkerWidget", u"job number", None))
        self.pushButtonShow.setText("")
        self.labelTime.setText(QCoreApplication.translate("WorkerWidget", u"In Queue", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCancel.setToolTip(QCoreApplication.translate("WorkerWidget", u"Cancel job", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCancel.setText(QCoreApplication.translate("WorkerWidget", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemove.setToolTip(QCoreApplication.translate("WorkerWidget", u"Remove job from list", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemove.setText(QCoreApplication.translate("WorkerWidget", u"Remove", None))
        self.labelJobName.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>job name</p></body></html>", None))
        self.labelOutput.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>output_directory</p></body></html>", None))
        self.textBrowserStatus.setHtml(QCoreApplication.translate("WorkerWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cascadia Code'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

