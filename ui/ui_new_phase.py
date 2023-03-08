# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_phase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_NewPhaseDialog(object):
    def setupUi(self, NewPhaseDialog):
        if not NewPhaseDialog.objectName():
            NewPhaseDialog.setObjectName(u"NewPhaseDialog")
        NewPhaseDialog.resize(345, 139)
        self.gridLayout_2 = QGridLayout(NewPhaseDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelName = QLabel(NewPhaseDialog)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.labelSpaceGroup = QLabel(NewPhaseDialog)
        self.labelSpaceGroup.setObjectName(u"labelSpaceGroup")

        self.gridLayout.addWidget(self.labelSpaceGroup, 1, 0, 1, 1)

        self.labelColor = QLabel(NewPhaseDialog)
        self.labelColor.setObjectName(u"labelColor")

        self.gridLayout.addWidget(self.labelColor, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.lineName = QLineEdit(NewPhaseDialog)
        self.lineName.setObjectName(u"lineName")

        self.gridLayout.addWidget(self.lineName, 0, 2, 1, 1)

        self.lineSpaceGroup = QLineEdit(NewPhaseDialog)
        self.lineSpaceGroup.setObjectName(u"lineSpaceGroup")

        self.gridLayout.addWidget(self.lineSpaceGroup, 1, 2, 1, 1)

        self.lineColor = QLineEdit(NewPhaseDialog)
        self.lineColor.setObjectName(u"lineColor")

        self.gridLayout.addWidget(self.lineColor, 2, 2, 1, 1)

        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(NewPhaseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(NewPhaseDialog)
        self.buttonBox.accepted.connect(NewPhaseDialog.accept)
        self.buttonBox.rejected.connect(NewPhaseDialog.reject)

        QMetaObject.connectSlotsByName(NewPhaseDialog)
    # setupUi

    def retranslateUi(self, NewPhaseDialog):
        NewPhaseDialog.setWindowTitle(QCoreApplication.translate("NewPhaseDialog", u"Add New Phase", None))
        self.labelName.setText(QCoreApplication.translate("NewPhaseDialog", u"Name*", None))
        self.labelSpaceGroup.setText(QCoreApplication.translate("NewPhaseDialog", u"Space Group Number*", None))
        self.labelColor.setText(QCoreApplication.translate("NewPhaseDialog", u"Color", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. al or aluminium", None))
        self.lineSpaceGroup.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. 225 ", None))
        self.lineColor.setPlaceholderText(QCoreApplication.translate("NewPhaseDialog", u"e.g. blue", None))
    # retranslateUi

