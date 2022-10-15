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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1087, 769)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.actionOpen_Workfolder = QAction(MainWindow)
        self.actionOpen_Workfolder.setObjectName(u"actionOpen_Workfolder")
        self.actionProcessingMenu = QAction(MainWindow)
        self.actionProcessingMenu.setObjectName(u"actionProcessingMenu")
        self.actionSignalNavigation = QAction(MainWindow)
        self.actionSignalNavigation.setObjectName(u"actionSignalNavigation")
        self.actionDictinary_indexing_setup = QAction(MainWindow)
        self.actionDictinary_indexing_setup.setObjectName(u"actionDictinary_indexing_setup")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bottomLayout = QVBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.consoleLog = QPlainTextEdit(self.centralwidget)
        self.consoleLog.setObjectName(u"consoleLog")

        self.bottomLayout.addWidget(self.consoleLog)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.consolePrompt = QLabel(self.centralwidget)
        self.consolePrompt.setObjectName(u"consolePrompt")

        self.inputLayout.addWidget(self.consolePrompt)

        self.consoleInput = QLineEdit(self.centralwidget)
        self.consoleInput.setObjectName(u"consoleInput")

        self.inputLayout.addWidget(self.consoleInput)


        self.bottomLayout.addLayout(self.inputLayout)

        self.bottomLayout.setStretch(0, 2)

        self.gridLayout.addLayout(self.bottomLayout, 2, 0, 1, 1)

        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.systemViewerLayout = QVBoxLayout()
        self.systemViewerLayout.setObjectName(u"systemViewerLayout")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")

        self.systemViewerLayout.addWidget(self.folderLabel)

        self.systemViewer = QTreeView(self.centralwidget)
        self.systemViewer.setObjectName(u"systemViewer")
        self.systemViewer.setMinimumSize(QSize(500, 0))
        self.systemViewer.setStyleSheet(u"")
        self.systemViewer.setAnimated(True)
        self.systemViewer.header().setStretchLastSection(True)

        self.systemViewerLayout.addWidget(self.systemViewer)


        self.topLayout.addLayout(self.systemViewerLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.topLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.topLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1087, 26))
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
        self.menuPlot.addAction(self.actionSignalNavigation)
        self.menuDictionary_indexing.addAction(self.actionDictinary_indexing_setup)

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
        self.actionDictinary_indexing_setup.setText(QCoreApplication.translate("MainWindow", u"Dictinary indexing setup", None))
        self.consolePrompt.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.folderLabel.setText(QCoreApplication.translate("MainWindow", u"NO FOLDER OPENED", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcessing.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.menuPlot.setTitle(QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.menuDictionary_indexing.setTitle(QCoreApplication.translate("MainWindow", u"Dictionary indexing", None))
    # retranslateUi

