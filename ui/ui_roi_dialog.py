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
        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.browseButton, 8, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 9, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pathLabel, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.pathLineEdit = QLineEdit(self.centralwidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setMinimumSize(QSize(400, 0))

        self.gridLayout.addWidget(self.pathLineEdit, 8, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 4, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.label_4 = QLabel(ROIDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEditYend = QLineEdit(ROIDialog)
        self.lineEditYend.setObjectName(u"lineEditYend")

        self.gridLayout_4.addWidget(self.lineEditYend, 3, 1, 1, 1)

        self.label_3 = QLabel(ROIDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEditXstart = QLineEdit(ROIDialog)
        self.lineEditXstart.setObjectName(u"lineEditXstart")
        self.lineEditXstart.setMaxLength(3)
        self.lineEditXstart.setCursorPosition(3)
        self.lineEditXstart.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditXstart, 0, 1, 1, 1)

        self.lineEditXend = QLineEdit(ROIDialog)
        self.lineEditXend.setObjectName(u"lineEditXend")

        self.gridLayout_4.addWidget(self.lineEditXend, 1, 1, 1, 1)

        self.label = QLabel(ROIDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(ROIDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEditYstart = QLineEdit(ROIDialog)
        self.lineEditYstart.setObjectName(u"lineEditYstart")

        self.gridLayout_4.addWidget(self.lineEditYstart, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 2, 1)

        QWidget.setTabOrder(self.lineEditXstart, self.lineEditXend)
        QWidget.setTabOrder(self.lineEditXend, self.lineEditYstart)
        QWidget.setTabOrder(self.lineEditYstart, self.lineEditYend)
        QWidget.setTabOrder(self.lineEditYend, self.pathLineEdit)
        QWidget.setTabOrder(self.pathLineEdit, self.browseButton)

        self.retranslateUi(ROIDialog)

        QMetaObject.connectSlotsByName(ROIDialog)
    # setupUi

    def retranslateUi(self, ROIDialog):
        ROIDialog.setWindowTitle(QCoreApplication.translate("ROIDialog", u"Region of interest", None))
        self.browseButton.setText(QCoreApplication.translate("ROIDialog", u"Browse", None))
        self.pathLabel.setText(QCoreApplication.translate("ROIDialog", u"Savepath", None))
        self.label_4.setText(QCoreApplication.translate("ROIDialog", u"y-end", None))
        self.lineEditYend.setInputMask(QCoreApplication.translate("ROIDialog", u"999", None))
        self.lineEditYend.setText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.lineEditYend.setPlaceholderText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.label_3.setText(QCoreApplication.translate("ROIDialog", u"y-start", None))
        self.lineEditXstart.setInputMask(QCoreApplication.translate("ROIDialog", u"999", None))
        self.lineEditXstart.setText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.lineEditXstart.setPlaceholderText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.lineEditXend.setInputMask(QCoreApplication.translate("ROIDialog", u"999", None))
        self.lineEditXend.setText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.lineEditXend.setPlaceholderText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.label.setText(QCoreApplication.translate("ROIDialog", u"x-start", None))
        self.label_2.setText(QCoreApplication.translate("ROIDialog", u"x-end", None))
        self.lineEditYstart.setInputMask(QCoreApplication.translate("ROIDialog", u"999", None))
        self.lineEditYstart.setText(QCoreApplication.translate("ROIDialog", u"0", None))
        self.lineEditYstart.setPlaceholderText(QCoreApplication.translate("ROIDialog", u"0", None))
    # retranslateUi

