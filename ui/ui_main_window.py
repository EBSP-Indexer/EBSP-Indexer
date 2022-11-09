# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(695, 662)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.actionOpen_Workfolder = QAction(MainWindow)
        self.actionOpen_Workfolder.setObjectName(u"actionOpen_Workfolder")
        self.actionProcessingMenu = QAction(MainWindow)
        self.actionProcessingMenu.setObjectName(u"actionProcessingMenu")
        self.actionSignalNavigation = QAction(MainWindow)
        self.actionSignalNavigation.setObjectName(u"actionSignalNavigation")
        self.actionDictionary_indexing = QAction(MainWindow)
        self.actionDictionary_indexing.setObjectName(u"actionDictionary_indexing")
        self.actionPattern_Center = QAction(MainWindow)
        self.actionPattern_Center.setObjectName(u"actionPattern_Center")
        self.actionROI = QAction(MainWindow)
        self.actionROI.setObjectName(u"actionROI")
        self.actionHough_indexing = QAction(MainWindow)
        self.actionHough_indexing.setObjectName(u"actionHough_indexing")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.systemViewerLayout = QVBoxLayout()
        self.systemViewerLayout.setObjectName(u"systemViewerLayout")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderLabel.sizePolicy().hasHeightForWidth())
        self.folderLabel.setSizePolicy(sizePolicy)

        self.systemViewerLayout.addWidget(self.folderLabel)

        self.systemViewer = QTreeView(self.centralwidget)
        self.systemViewer.setObjectName(u"systemViewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.systemViewer.sizePolicy().hasHeightForWidth())
        self.systemViewer.setSizePolicy(sizePolicy1)
        self.systemViewer.setMinimumSize(QSize(320, 320))
        self.systemViewer.setStyleSheet(u"")
        self.systemViewer.setAnimated(True)
        self.systemViewer.header().setStretchLastSection(True)

        self.systemViewerLayout.addWidget(self.systemViewer)

        self.consoleLog = QPlainTextEdit(self.centralwidget)
        self.consoleLog.setObjectName(u"consoleLog")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.consoleLog.sizePolicy().hasHeightForWidth())
        self.consoleLog.setSizePolicy(sizePolicy2)

        self.systemViewerLayout.addWidget(self.consoleLog)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.consolePrompt = QLabel(self.centralwidget)
        self.consolePrompt.setObjectName(u"consolePrompt")

        self.inputLayout.addWidget(self.consolePrompt)


        self.systemViewerLayout.addLayout(self.inputLayout)

        self.systemViewerLayout.setStretch(1, 1)

        self.topLayout.addLayout(self.systemViewerLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.topLayout.addWidget(self.line_2)

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName(u"MplWidget")
        sizePolicy1.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy1)
        self.MplWidget.setMinimumSize(QSize(320, 320))
        self.MplWidget.setStyleSheet(u"background-color: transparent")

        self.topLayout.addWidget(self.MplWidget)

        self.topLayout.setStretch(0, 1)
        self.topLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.topLayout)

        self.verticalLayout.setStretch(0, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 695, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcessing = QMenu(self.menubar)
        self.menuProcessing.setObjectName(u"menuProcessing")
        self.menuPlot = QMenu(self.menubar)
        self.menuPlot.setObjectName(u"menuPlot")
        self.menuDictionary_indexing = QMenu(self.menubar)
        self.menuDictionary_indexing.setObjectName(u"menuDictionary_indexing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuDictionary_indexing.menuAction())
        self.menuFile.addAction(self.actionOpen_Workfolder)
        self.menuProcessing.addAction(self.actionProcessingMenu)
        self.menuProcessing.addAction(self.actionROI)
        self.menuProcessing.addAction(self.actionPattern_Center)
        self.menuPlot.addAction(self.actionSignalNavigation)
        self.menuDictionary_indexing.addAction(self.actionDictionary_indexing)
        self.menuDictionary_indexing.addAction(self.actionHough_indexing)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EBSD-GUI", None))
        self.actionOpen_Workfolder.setText(QCoreApplication.translate("MainWindow", u"Open Workfolder...", None))
#if QT_CONFIG(statustip)
        self.actionOpen_Workfolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Select a folder containing patterns", u"LOL"))
#endif // QT_CONFIG(statustip)
        self.actionProcessingMenu.setText(QCoreApplication.translate("MainWindow", u"N/S improvement", None))
#if QT_CONFIG(statustip)
        self.actionProcessingMenu.setStatusTip(QCoreApplication.translate("MainWindow", u"Perform processing on a pattern", None))
#endif // QT_CONFIG(statustip)
        self.actionSignalNavigation.setText(QCoreApplication.translate("MainWindow", u"Signal navigation", None))
        self.actionDictionary_indexing.setText(QCoreApplication.translate("MainWindow", u"Dictionary indexing", None))
        self.actionPattern_Center.setText(QCoreApplication.translate("MainWindow", u"Pattern center", None))
        self.actionROI.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.actionHough_indexing.setText(QCoreApplication.translate("MainWindow", u"Hough indexing", None))
        self.folderLabel.setText(QCoreApplication.translate("MainWindow", u"NO FOLDER OPENED", None))
        self.consolePrompt.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcessing.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.menuPlot.setTitle(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.menuDictionary_indexing.setTitle(QCoreApplication.translate("MainWindow", u"Indexing", None))
    # retranslateUi

