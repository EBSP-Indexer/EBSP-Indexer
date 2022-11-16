# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pre_indexing_maps.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(591, 421)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget = MplWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 300))

        self.verticalLayout_2.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBoxMIM = QCheckBox(Dialog)
        self.checkBoxMIM.setObjectName(u"checkBoxMIM")

        self.verticalLayout.addWidget(self.checkBoxMIM)

        self.checkBoxIQM = QCheckBox(Dialog)
        self.checkBoxIQM.setObjectName(u"checkBoxIQM")

        self.verticalLayout.addWidget(self.checkBoxIQM)

        self.checkBoxADP = QCheckBox(Dialog)
        self.checkBoxADP.setObjectName(u"checkBoxADP")

        self.verticalLayout.addWidget(self.checkBoxADP)

        self.checkBoxVBSE = QCheckBox(Dialog)
        self.checkBoxVBSE.setObjectName(u"checkBoxVBSE")

        self.verticalLayout.addWidget(self.checkBoxVBSE)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Preview:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose maps to generate", None))
        self.checkBoxMIM.setText(QCoreApplication.translate("Dialog", u"Mean intensity map", None))
        self.checkBoxIQM.setText(QCoreApplication.translate("Dialog", u"Image quality map", None))
        self.checkBoxADP.setText(QCoreApplication.translate("Dialog", u"Average dot product map", None))
        self.checkBoxVBSE.setText(QCoreApplication.translate("Dialog", u"Virtual backscatter image - RGB", None))
    # retranslateUi

