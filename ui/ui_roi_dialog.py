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
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_ROIDialog(object):
    def setupUi(self, ROIDialog):
        if not ROIDialog.objectName():
            ROIDialog.setObjectName(u"ROIDialog")
        ROIDialog.resize(803, 240)
        self.gridLayout_2 = QGridLayout(ROIDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(ROIDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pathLineEdit = QLineEdit(self.centralwidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.pathLineEdit, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(40, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.browseButton, 5, 2, 1, 1)

        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pathLabel, 5, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEditXstart = QLineEdit(self.centralwidget)
        self.lineEditXstart.setObjectName(u"lineEditXstart")

        self.gridLayout.addWidget(self.lineEditXstart, 0, 1, 1, 1)

        self.lineEditXend = QLineEdit(self.centralwidget)
        self.lineEditXend.setObjectName(u"lineEditXend")

        self.gridLayout.addWidget(self.lineEditXend, 1, 1, 1, 1)

        self.lineEditYstart = QLineEdit(self.centralwidget)
        self.lineEditYstart.setObjectName(u"lineEditYstart")

        self.gridLayout.addWidget(self.lineEditYstart, 2, 1, 1, 1)

        self.lineEditYend = QLineEdit(self.centralwidget)
        self.lineEditYend.setObjectName(u"lineEditYend")

        self.gridLayout.addWidget(self.lineEditYend, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(ROIDialog)

        QMetaObject.connectSlotsByName(ROIDialog)
    # setupUi

    def retranslateUi(self, ROIDialog):
        ROIDialog.setWindowTitle(QCoreApplication.translate("ROIDialog", u"Pattern Processing", None))
        self.label_2.setText(QCoreApplication.translate("ROIDialog", u"x-end", None))
        self.label_3.setText(QCoreApplication.translate("ROIDialog", u"y-start", None))
        self.browseButton.setText(QCoreApplication.translate("ROIDialog", u"Browse", None))
        self.pathLabel.setText(QCoreApplication.translate("ROIDialog", u"Filepath of processed pattern:", None))
        self.label.setText(QCoreApplication.translate("ROIDialog", u"x-start", None))
        self.label_4.setText(QCoreApplication.translate("ROIDialog", u"y-end", None))
        self.lineEditXstart.setInputMask("")
    # retranslateUi

