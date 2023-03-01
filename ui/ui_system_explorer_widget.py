# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_explorer_widget.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_SystemExplorerWidget(object):
    def setupUi(self, SystemExplorerWidget):
        if not SystemExplorerWidget.objectName():
            SystemExplorerWidget.setObjectName(u"SystemExplorerWidget")
        SystemExplorerWidget.resize(480, 365)
        SystemExplorerWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.verticalLayout = QVBoxLayout(SystemExplorerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.folderLabel = QLabel(SystemExplorerWidget)
        self.folderLabel.setObjectName(u"folderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderLabel.sizePolicy().hasHeightForWidth())
        self.folderLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.folderLabel)

        self.systemViewer = QTreeView(SystemExplorerWidget)
        self.systemViewer.setObjectName(u"systemViewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.systemViewer.sizePolicy().hasHeightForWidth())
        self.systemViewer.setSizePolicy(sizePolicy1)
        self.systemViewer.setMinimumSize(QSize(320, 320))
        self.systemViewer.setMouseTracking(False)
        self.systemViewer.setTabletTracking(True)
        self.systemViewer.setStyleSheet(u"")
        self.systemViewer.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)
        self.systemViewer.setTabKeyNavigation(True)
        self.systemViewer.setDragEnabled(False)
        self.systemViewer.setDragDropOverwriteMode(False)
        self.systemViewer.setAlternatingRowColors(False)
        self.systemViewer.setAnimated(True)
        self.systemViewer.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.systemViewer)


        self.retranslateUi(SystemExplorerWidget)

        QMetaObject.connectSlotsByName(SystemExplorerWidget)
    # setupUi

    def retranslateUi(self, SystemExplorerWidget):
        SystemExplorerWidget.setWindowTitle(QCoreApplication.translate("SystemExplorerWidget", u"System Explorer Widget", None))
        self.folderLabel.setText(QCoreApplication.translate("SystemExplorerWidget", u"NO FOLDER OPENED", None))
    # retranslateUi

