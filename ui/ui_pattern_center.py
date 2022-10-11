# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattern_center.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QProgressBar, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PatternCenterDialog(object):
    def setupUi(self, PatternCenterDialog):
        if not PatternCenterDialog.objectName():
            PatternCenterDialog.setObjectName(u"PatternCenterDialog")
        PatternCenterDialog.resize(1055, 399)
        self.gridLayout = QGridLayout(PatternCenterDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.comboBox = QComboBox(PatternCenterDialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_3 = QComboBox(PatternCenterDialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMaximumSize(QSize(104, 16777215))

        self.horizontalLayout_2.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(PatternCenterDialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(PatternCenterDialog)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(120, 120))

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(PatternCenterDialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(PatternCenterDialog)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(PatternCenterDialog)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(PatternCenterDialog)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_4 = QLabel(PatternCenterDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.progressBar = QProgressBar(PatternCenterDialog)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(PatternCenterDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox_3 = QDoubleSpinBox(PatternCenterDialog)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout.addWidget(self.doubleSpinBox_3)

        self.label_2 = QLabel(PatternCenterDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(PatternCenterDialog)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout.addWidget(self.doubleSpinBox_2)

        self.label_3 = QLabel(PatternCenterDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(PatternCenterDialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.widget = QWidget(PatternCenterDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(240, 240))

        self.gridLayout_2.addWidget(self.widget, 0, 0, 4, 1)

        self.buttonBox = QDialogButtonBox(PatternCenterDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)


        self.retranslateUi(PatternCenterDialog)

        QMetaObject.connectSlotsByName(PatternCenterDialog)
    # setupUi

    def retranslateUi(self, PatternCenterDialog):
        PatternCenterDialog.setWindowTitle(QCoreApplication.translate("PatternCenterDialog", u"Dialog", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PatternCenterDialog", u"Phase 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PatternCenterDialog", u"Nickel", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PatternCenterDialog", u"Aluminium", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PatternCenterDialog", u"Austenite", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("PatternCenterDialog", u"Ferrite", None))
        self.comboBox.setItemText(5, "")

        self.comboBox_3.setItemText(0, QCoreApplication.translate("PatternCenterDialog", u"Phase 2", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("PatternCenterDialog", u"Nickel", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("PatternCenterDialog", u"Aluminium", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("PatternCenterDialog", u"Austenite", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("PatternCenterDialog", u"Ferrite", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("PatternCenterDialog", u"Phase 3", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("PatternCenterDialog", u"Nickel", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("PatternCenterDialog", u"Aluminium", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("PatternCenterDialog", u"Austenite", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("PatternCenterDialog", u"Ferrite", None))

        self.checkBox.setText(QCoreApplication.translate("PatternCenterDialog", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("PatternCenterDialog", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("PatternCenterDialog", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("PatternCenterDialog", u"CheckBox", None))
        self.label_4.setText(QCoreApplication.translate("PatternCenterDialog", u"Matching: 0.91", None))
        self.label.setText(QCoreApplication.translate("PatternCenterDialog", u"x:", None))
        self.label_2.setText(QCoreApplication.translate("PatternCenterDialog", u"y:", None))
        self.label_3.setText(QCoreApplication.translate("PatternCenterDialog", u"z:", None))
    # retranslateUi

