# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roi_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_ROIDialog(object):
    def setupUi(self, ROIDialog):
        if not ROIDialog.objectName():
            ROIDialog.setObjectName(u"ROIDialog")
        ROIDialog.resize(655, 496)
        self.gridLayout = QGridLayout(ROIDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centralwidget = QFrame(ROIDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBoxNavigator = QComboBox(self.centralwidget)
        self.comboBoxNavigator.setObjectName(u"comboBoxNavigator")

        self.horizontalLayout_5.addWidget(self.comboBoxNavigator)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.mplWidget = MplWidget(self.centralwidget)
        self.mplWidget.setObjectName(u"mplWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy1)
        self.mplWidget.setMinimumSize(QSize(200, 200))
        self.mplWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout.addWidget(self.mplWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.imageShapeLabel = QLabel(self.centralwidget)
        self.imageShapeLabel.setObjectName(u"imageShapeLabel")

        self.horizontalLayout_6.addWidget(self.imageShapeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.spinBoxXstart = QSpinBox(self.centralwidget)
        self.spinBoxXstart.setObjectName(u"spinBoxXstart")

        self.horizontalLayout_3.addWidget(self.spinBoxXstart)

        self.spinBoxXend = QSpinBox(self.centralwidget)
        self.spinBoxXend.setObjectName(u"spinBoxXend")

        self.horizontalLayout_3.addWidget(self.spinBoxXend)

        self.spinBoxYstart = QSpinBox(self.centralwidget)
        self.spinBoxYstart.setObjectName(u"spinBoxYstart")

        self.horizontalLayout_3.addWidget(self.spinBoxYstart)

        self.spinBoxYend = QSpinBox(self.centralwidget)
        self.spinBoxYend.setObjectName(u"spinBoxYend")

        self.horizontalLayout_3.addWidget(self.spinBoxYend)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")

        self.horizontalLayout.addWidget(self.folderLabel)

        self.folderEdit = QLabel(self.centralwidget)
        self.folderEdit.setObjectName(u"folderEdit")

        self.horizontalLayout.addWidget(self.folderEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filenameLabel = QLabel(self.centralwidget)
        self.filenameLabel.setObjectName(u"filenameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filenameLabel.sizePolicy().hasHeightForWidth())
        self.filenameLabel.setSizePolicy(sizePolicy2)
        self.filenameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.filenameLabel)

        self.filenameEdit = QLineEdit(self.centralwidget)
        self.filenameEdit.setObjectName(u"filenameEdit")
        self.filenameEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.filenameEdit)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setMinimumSize(QSize(0, 0))
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.browseButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(ROIDialog)

        QMetaObject.connectSlotsByName(ROIDialog)
    # setupUi

    def retranslateUi(self, ROIDialog):
        ROIDialog.setWindowTitle(QCoreApplication.translate("ROIDialog", u"Region of interest", None))
        self.label_5.setText(QCoreApplication.translate("ROIDialog", u"Navigator:", None))
        self.label_6.setText(QCoreApplication.translate("ROIDialog", u"Image shape (x, y):", None))
        self.imageShapeLabel.setText(QCoreApplication.translate("ROIDialog", u"(x,y)", None))
        self.label.setText(QCoreApplication.translate("ROIDialog", u"<html><head/><body><p>Selection (x<span style=\" vertical-align:sub;\">start</span>, x<span style=\" vertical-align:sub;\">end</span>, y<span style=\" vertical-align:sub;\">start</span>, y<span style=\" vertical-align:sub;\">end</span>)</p></body></html>", None))
        self.folderLabel.setText(QCoreApplication.translate("ROIDialog", u"Working folder:", None))
        self.folderEdit.setText(QCoreApplication.translate("ROIDialog", u"TextLabel", None))
        self.filenameLabel.setText(QCoreApplication.translate("ROIDialog", u"Filename:", None))
        self.browseButton.setText(QCoreApplication.translate("ROIDialog", u"Browse", None))
    # retranslateUi

