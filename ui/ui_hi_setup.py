# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hi_setup.ui'
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
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_HISetupDialog(object):
    def setupUi(self, HISetupDialog):
        if not HISetupDialog.objectName():
            HISetupDialog.setObjectName(u"HISetupDialog")
        HISetupDialog.resize(424, 346)
        self.gridLayout = QGridLayout(HISetupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(HISetupDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.checkBoxLazy = QCheckBox(self.frame)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxLazy.setChecked(True)
        self.checkBoxLazy.setTristate(False)

        self.verticalLayout_3.addWidget(self.checkBoxLazy)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.patternCenterY = QDoubleSpinBox(self.frame)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(4)
        self.patternCenterY.setMaximum(0.999900000000000)
        self.patternCenterY.setSingleStep(0.000100000000000)

        self.horizontalLayout_2.addWidget(self.patternCenterY)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.patternCenterX = QDoubleSpinBox(self.frame)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(4)
        self.patternCenterX.setMaximum(0.999900000000000)
        self.patternCenterX.setSingleStep(0.000100000000000)

        self.horizontalLayout_2.addWidget(self.patternCenterX)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.patternCenterZ = QDoubleSpinBox(self.frame)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setDecimals(4)
        self.patternCenterZ.setMaximum(0.999900000000000)
        self.patternCenterZ.setSingleStep(0.000100000000000)

        self.horizontalLayout_2.addWidget(self.patternCenterZ)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.listWidgetPhase = QListWidget(self.frame)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        QListWidgetItem(self.listWidgetPhase)
        self.listWidgetPhase.setObjectName(u"listWidgetPhase")
        self.listWidgetPhase.setAlternatingRowColors(False)
        self.listWidgetPhase.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_2.addWidget(self.listWidgetPhase)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxLazy, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterZ)

        self.retranslateUi(HISetupDialog)
        self.buttonBox.rejected.connect(HISetupDialog.reject)
        self.buttonBox.accepted.connect(HISetupDialog.accept)

        QMetaObject.connectSlotsByName(HISetupDialog)
    # setupUi

    def retranslateUi(self, HISetupDialog):
        HISetupDialog.setWindowTitle(QCoreApplication.translate("HISetupDialog", u"Hough Indexing setup", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("HISetupDialog", u"Lazy loading", None))
        self.label_2.setText(QCoreApplication.translate("HISetupDialog", u"Pattern center:", None))
        self.label_3.setText(QCoreApplication.translate("HISetupDialog", u"X:", None))
        self.label_4.setText(QCoreApplication.translate("HISetupDialog", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("HISetupDialog", u"Z:", None))
        self.patternCenterZ.setPrefix("")
        self.label.setText(QCoreApplication.translate("HISetupDialog", u"Phases:", None))

        __sortingEnabled = self.listWidgetPhase.isSortingEnabled()
        self.listWidgetPhase.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidgetPhase.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("HISetupDialog", u"al", None));
        ___qlistwidgetitem1 = self.listWidgetPhase.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("HISetupDialog", u"austenite", None));
        ___qlistwidgetitem2 = self.listWidgetPhase.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("HISetupDialog", u"ferrite", None));
        ___qlistwidgetitem3 = self.listWidgetPhase.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("HISetupDialog", u"ni", None));
        ___qlistwidgetitem4 = self.listWidgetPhase.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("HISetupDialog", u"si", None));
        ___qlistwidgetitem5 = self.listWidgetPhase.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("HISetupDialog", u"ti_beta", None));
        self.listWidgetPhase.setSortingEnabled(__sortingEnabled)

    # retranslateUi

