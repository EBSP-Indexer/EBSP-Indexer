# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'di_setup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_DiSetupDialog(object):
    def setupUi(self, DiSetupDialog):
        if not DiSetupDialog.objectName():
            DiSetupDialog.setObjectName(u"DiSetupDialog")
        DiSetupDialog.resize(702, 355)
        self.gridLayout_2 = QGridLayout(DiSetupDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(DiSetupDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.patternCenterY = QLineEdit(self.centralwidget)
        self.patternCenterY.setObjectName(u"patternCenterY")

        self.gridLayout.addWidget(self.patternCenterY, 3, 1, 1, 1)

        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setScaledContents(False)
        self.pathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.pathLabel, 6, 0, 1, 1)

        self.patternCenterX = QLineEdit(self.centralwidget)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setCursorPosition(2)

        self.gridLayout.addWidget(self.patternCenterX, 2, 1, 1, 1)

        self.patternCenterZ = QLineEdit(self.centralwidget)
        self.patternCenterZ.setObjectName(u"patternCenterZ")

        self.gridLayout.addWidget(self.patternCenterZ, 4, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.listWidgetPhase = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        self.listWidgetPhase.setObjectName(u"listWidgetPhase")
        self.listWidgetPhase.setMinimumSize(QSize(0, 50))
        self.listWidgetPhase.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.listWidgetPhase, 6, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.checkBoxRefine = QCheckBox(self.centralwidget)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")

        self.gridLayout.addWidget(self.checkBoxRefine, 5, 1, 1, 1)

        self.pushButtonBrowse = QPushButton(self.centralwidget)
        self.pushButtonBrowse.setObjectName(u"pushButtonBrowse")

        self.gridLayout.addWidget(self.pushButtonBrowse, 7, 2, 1, 1)

        self.lineEditPath = QLineEdit(self.centralwidget)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 7, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(DiSetupDialog)

        QMetaObject.connectSlotsByName(DiSetupDialog)
    # setupUi

    def retranslateUi(self, DiSetupDialog):
        DiSetupDialog.setWindowTitle(QCoreApplication.translate("DiSetupDialog", u"Pattern Processing", None))
        self.patternCenterY.setInputMask(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterY.setText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterY.setPlaceholderText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.pathLabel.setText(QCoreApplication.translate("DiSetupDialog", u"Phase", None))
        self.patternCenterX.setInputMask(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterX.setText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterX.setPlaceholderText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterZ.setInputMask(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterZ.setText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.patternCenterZ.setPlaceholderText(QCoreApplication.translate("DiSetupDialog", u".000", None))
        self.label_4.setText(QCoreApplication.translate("DiSetupDialog", u"PC - z", None))
        self.label_3.setText(QCoreApplication.translate("DiSetupDialog", u"PC - y", None))
        self.label.setText(QCoreApplication.translate("DiSetupDialog", u"Refine", None))

        __sortingEnabled = self.listWidgetPhase.isSortingEnabled()
        self.listWidgetPhase.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetPhase.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DiSetupDialog", u"al", None));
        ___qlistwidgetitem1 = self.listWidgetPhase.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("DiSetupDialog", u"si", None));
        ___qlistwidgetitem2 = self.listWidgetPhase.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("DiSetupDialog", u"ni", None));
        ___qlistwidgetitem3 = self.listWidgetPhase.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("DiSetupDialog", u"ferrite", None));
        ___qlistwidgetitem4 = self.listWidgetPhase.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("DiSetupDialog", u"austenite", None));
        self.listWidgetPhase.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("DiSetupDialog", u"PC - x", None))
        self.checkBoxRefine.setText("")
        self.pushButtonBrowse.setText(QCoreApplication.translate("DiSetupDialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("DiSetupDialog", u"Master patterns", None))
    # retranslateUi

