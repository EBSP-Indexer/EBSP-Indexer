# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roi_dialog.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_ROIDialog(object):
    def setupUi(self, ROIDialog):
        if not ROIDialog.objectName():
            ROIDialog.setObjectName(u"ROIDialog")
        ROIDialog.resize(812, 344)
        self.gridLayout_2 = QGridLayout(ROIDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(ROIDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.spinBoxXstart = QSpinBox(self.centralwidget)
        self.spinBoxXstart.setObjectName(u"spinBoxXstart")

        self.gridLayout_4.addWidget(self.spinBoxXstart, 1, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.spinBoxXend = QSpinBox(self.centralwidget)
        self.spinBoxXend.setObjectName(u"spinBoxXend")

        self.gridLayout_4.addWidget(self.spinBoxXend, 2, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.spinBoxYstart = QSpinBox(self.centralwidget)
        self.spinBoxYstart.setObjectName(u"spinBoxYstart")

        self.gridLayout_4.addWidget(self.spinBoxYstart, 3, 1, 1, 1)

        self.spinBoxYend = QSpinBox(self.centralwidget)
        self.spinBoxYend.setObjectName(u"spinBoxYend")

        self.gridLayout_4.addWidget(self.spinBoxYend, 4, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.gridLayout_5.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.mplWidget = MplWidget(self.centralwidget)
        self.mplWidget.setObjectName(u"mplWidget")
        self.mplWidget.setStyleSheet(u"background-color: transparent")

        self.gridLayout_5.addWidget(self.mplWidget, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_5.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.pathLineEdit = QLineEdit(self.centralwidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.pathLineEdit)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setMinimumSize(QSize(0, 0))
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.browseButton)


        self.gridLayout_5.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 4, 0, 1, 1)


        self.retranslateUi(ROIDialog)

        QMetaObject.connectSlotsByName(ROIDialog)
    # setupUi

    def retranslateUi(self, ROIDialog):
        ROIDialog.setWindowTitle(QCoreApplication.translate("ROIDialog", u"Region of interest", None))
        self.label_6.setText(QCoreApplication.translate("ROIDialog", u"Image shape:", None))
        self.label_4.setText(QCoreApplication.translate("ROIDialog", u"y-end [px]", None))
        self.label_3.setText(QCoreApplication.translate("ROIDialog", u"y-start [px]", None))
        self.label_2.setText(QCoreApplication.translate("ROIDialog", u"x-end [px]", None))
        self.label.setText(QCoreApplication.translate("ROIDialog", u"x-start [px]", None))
        self.label_5.setText(QCoreApplication.translate("ROIDialog", u"Savepath", None))
        self.browseButton.setText(QCoreApplication.translate("ROIDialog", u"Browse", None))
    # retranslateUi

