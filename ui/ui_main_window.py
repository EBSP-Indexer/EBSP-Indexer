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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 537)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.actionOpen_Workfolder = QAction(MainWindow)
        self.actionOpen_Workfolder.setObjectName(u"actionOpen_Workfolder")
        self.actionProcessingMenu = QAction(MainWindow)
        self.actionProcessingMenu.setObjectName(u"actionProcessingMenu")
        self.actionSignalNavigation = QAction(MainWindow)
        self.actionSignalNavigation.setObjectName(u"actionSignalNavigation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 933, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcessing = QMenu(self.menubar)
        self.menuProcessing.setObjectName(u"menuProcessing")
        self.menuPlot = QMenu(self.menubar)
        self.menuPlot.setObjectName(u"menuPlot")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menuFile.addAction(self.actionOpen_Workfolder)
        self.menuProcessing.addAction(self.actionProcessingMenu)
        self.menuPlot.addAction(self.actionSignalNavigation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EBSD-GUI", None))
        self.actionOpen_Workfolder.setText(QCoreApplication.translate("MainWindow", u"Open Workfolder...", None))
#if QT_CONFIG(statustip)
        self.actionOpen_Workfolder.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.actionProcessingMenu.setText(QCoreApplication.translate("MainWindow", u"N/S improvement", None))
        self.actionSignalNavigation.setText(QCoreApplication.translate("MainWindow", u"Signal navigation", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcessing.setTitle(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.menuPlot.setTitle(QCoreApplication.translate("MainWindow", u"Plotting", None))
    # retranslateUi

