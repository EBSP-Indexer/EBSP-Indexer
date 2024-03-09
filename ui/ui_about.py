# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(449, 314)
        self.formLayout_2 = QFormLayout(AboutDialog)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabWidget = QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.softwareVersionLabel = QLabel(self.tab)
        self.softwareVersionLabel.setObjectName(u"softwareVersionLabel")

        self.horizontalLayout.addWidget(self.softwareVersionLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.authorListWidget = QListWidget(self.tab)
        QListWidgetItem(self.authorListWidget)
        QListWidgetItem(self.authorListWidget)
        QListWidgetItem(self.authorListWidget)
        self.authorListWidget.setObjectName(u"authorListWidget")

        self.verticalLayout.addWidget(self.authorListWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dependenciesTableWidget = QTableWidget(self.tab_2)
        if (self.dependenciesTableWidget.columnCount() < 2):
            self.dependenciesTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dependenciesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dependenciesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.dependenciesTableWidget.setObjectName(u"dependenciesTableWidget")
        self.dependenciesTableWidget.setMinimumSize(QSize(0, 220))
        self.dependenciesTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dependenciesTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.dependenciesTableWidget.setRowCount(0)
        self.dependenciesTableWidget.setColumnCount(2)
        self.dependenciesTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.dependenciesTableWidget.horizontalHeader().setStretchLastSection(True)
        self.dependenciesTableWidget.verticalHeader().setVisible(False)
        self.dependenciesTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.dependenciesTableWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tabWidget)


        self.retranslateUi(AboutDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.softwareVersionLabel.setText(QCoreApplication.translate("AboutDialog", u"EBSP Indexer - v0.0.0", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Authors", None))

        __sortingEnabled = self.authorListWidget.isSortingEnabled()
        self.authorListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.authorListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("AboutDialog", u"Erlend Mikkelsen \u00d8stvold", None));
        ___qlistwidgetitem1 = self.authorListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("AboutDialog", u"Hallvard Tangvik Tellefsen Relling", None));
        ___qlistwidgetitem2 = self.authorListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("AboutDialog", u"Olav Leth-Olsen", None));
        self.authorListWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AboutDialog", u"General", None))
        ___qtablewidgetitem = self.dependenciesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AboutDialog", u"Name", None));
        ___qtablewidgetitem1 = self.dependenciesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AboutDialog", u"Version", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AboutDialog", u"Dependencies", None))
    # retranslateUi

