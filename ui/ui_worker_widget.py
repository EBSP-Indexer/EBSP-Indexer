# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_WorkerWidget(object):
    def setupUi(self, WorkerWidget):
        if not WorkerWidget.objectName():
            WorkerWidget.setObjectName(u"WorkerWidget")
        WorkerWidget.resize(511, 324)
        self.verticalLayout = QVBoxLayout(WorkerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelJobNumber = QLabel(WorkerWidget)
        self.labelJobNumber.setObjectName(u"labelJobNumber")

        self.horizontalLayout.addWidget(self.labelJobNumber)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.line_2 = QFrame(WorkerWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.labelTime = QLabel(WorkerWidget)
        self.labelTime.setObjectName(u"labelTime")
        self.labelTime.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.labelTime)

        self.pushButtonAbort = QPushButton(WorkerWidget)
        self.pushButtonAbort.setObjectName(u"pushButtonAbort")

        self.horizontalLayout.addWidget(self.pushButtonAbort)

        self.pushButtonRemove = QPushButton(WorkerWidget)
        self.pushButtonRemove.setObjectName(u"pushButtonRemove")
        self.pushButtonRemove.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/linea icons/resources/linea basic icons/basic_trashcan.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRemove.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButtonRemove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(WorkerWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.labelJobName = QLabel(WorkerWidget)
        self.labelJobName.setObjectName(u"labelJobName")
        self.labelJobName.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")

        self.verticalLayout.addWidget(self.labelJobName)

        self.labelOutput = QLabel(WorkerWidget)
        self.labelOutput.setObjectName(u"labelOutput")
        self.labelOutput.setStyleSheet(u"font: italic 8pt \"MS Sans Serif\";\n"
"color: rgb(120, 120, 120);")

        self.verticalLayout.addWidget(self.labelOutput)

        self.labelStatus = QLabel(WorkerWidget)
        self.labelStatus.setObjectName(u"labelStatus")
        self.labelStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.labelStatus)

        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(WorkerWidget)

        QMetaObject.connectSlotsByName(WorkerWidget)
    # setupUi

    def retranslateUi(self, WorkerWidget):
        WorkerWidget.setWindowTitle(QCoreApplication.translate("WorkerWidget", u"Form", None))
        self.labelJobNumber.setText(QCoreApplication.translate("WorkerWidget", u"job number", None))
        self.labelTime.setText(QCoreApplication.translate("WorkerWidget", u"0:00:00", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAbort.setToolTip(QCoreApplication.translate("WorkerWidget", u"Abort the worker", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonAbort.setText(QCoreApplication.translate("WorkerWidget", u"Abort", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemove.setToolTip(QCoreApplication.translate("WorkerWidget", u"Remove from list", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemove.setText("")
        self.labelJobName.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>job name</p></body></html>", None))
        self.labelOutput.setText(QCoreApplication.translate("WorkerWidget", u"<html><head/><body><p>output_directory</p></body></html>", None))
        self.labelStatus.setText(QCoreApplication.translate("WorkerWidget", u"status", None))
    # retranslateUi

