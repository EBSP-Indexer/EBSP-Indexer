# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattern_processing.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_PatternProcessingDialog(object):
    def setupUi(self, PatternProcessingDialog):
        if not PatternProcessingDialog.objectName():
            PatternProcessingDialog.setObjectName(u"PatternProcessingDialog")
        PatternProcessingDialog.resize(865, 472)
        PatternProcessingDialog.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.gridLayout = QGridLayout(PatternProcessingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(PatternProcessingDialog)
        self.frame.setObjectName(u"frame")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.staticBackgroundBox = QCheckBox(self.frame)
        self.staticBackgroundBox.setObjectName(u"staticBackgroundBox")
        self.staticBackgroundBox.setChecked(False)
        self.staticBackgroundBox.setTristate(False)

        self.verticalLayout.addWidget(self.staticBackgroundBox)

        self.dynamicBackgroundBox = QCheckBox(self.frame)
        self.dynamicBackgroundBox.setObjectName(u"dynamicBackgroundBox")
        self.dynamicBackgroundBox.setChecked(False)

        self.verticalLayout.addWidget(self.dynamicBackgroundBox)

        self.averageBox = QCheckBox(self.frame)
        self.averageBox.setObjectName(u"averageBox")
        self.averageBox.setChecked(False)

        self.verticalLayout.addWidget(self.averageBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.previewWidget = MplWidget(self.frame)
        self.previewWidget.setObjectName(u"previewWidget")
        self.previewWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_4.addWidget(self.previewWidget)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.folderLabel = QLabel(self.frame)
        self.folderLabel.setObjectName(u"folderLabel")

        self.horizontalLayout_5.addWidget(self.folderLabel)

        self.folderEdit = QLabel(self.frame)
        self.folderEdit.setObjectName(u"folderEdit")

        self.horizontalLayout_5.addWidget(self.folderEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filenameLabel = QLabel(self.frame)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.horizontalLayout.addWidget(self.filenameLabel)

        self.filenameEdit = QLineEdit(self.frame)
        self.filenameEdit.setObjectName(u"filenameEdit")
        self.filenameEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.filenameEdit)

        self.browseButton = QPushButton(self.frame)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.browseButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.staticBackgroundBox, self.dynamicBackgroundBox)
        QWidget.setTabOrder(self.dynamicBackgroundBox, self.averageBox)
        QWidget.setTabOrder(self.averageBox, self.browseButton)

        self.retranslateUi(PatternProcessingDialog)
        self.buttonBox.rejected.connect(PatternProcessingDialog.reject)
        self.buttonBox.accepted.connect(PatternProcessingDialog.accept)

        QMetaObject.connectSlotsByName(PatternProcessingDialog)
    # setupUi

    def retranslateUi(self, PatternProcessingDialog):
        PatternProcessingDialog.setWindowTitle(QCoreApplication.translate("PatternProcessingDialog", u"Pattern Processing", None))
        self.label.setText(QCoreApplication.translate("PatternProcessingDialog", u"Pre-processing steps", None))
#if QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingDialog", u"Remove the static background inplace.", None))
#endif // QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setText(QCoreApplication.translate("PatternProcessingDialog", u"Remove static background noise", None))
#if QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingDialog", u"Remove the dynamic background in an EBSD pattern.", None))
#endif // QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setText(QCoreApplication.translate("PatternProcessingDialog", u"Remove dynamic background noise", None))
#if QT_CONFIG(whatsthis)
        self.averageBox.setWhatsThis(QCoreApplication.translate("PatternProcessingDialog", u"Average a chunk of patterns with its neighbours within a window.", None))
#endif // QT_CONFIG(whatsthis)
        self.averageBox.setText(QCoreApplication.translate("PatternProcessingDialog", u"Average neighbour patterns", None))
        self.label_2.setText(QCoreApplication.translate("PatternProcessingDialog", u"Preview of pattern processing", None))
        self.folderLabel.setText(QCoreApplication.translate("PatternProcessingDialog", u"Working folder:", None))
        self.folderEdit.setText(QCoreApplication.translate("PatternProcessingDialog", u"PLACEHOLDER", None))
        self.filenameLabel.setText(QCoreApplication.translate("PatternProcessingDialog", u"Filename:", None))
        self.browseButton.setText(QCoreApplication.translate("PatternProcessingDialog", u"Browse", None))
    # retranslateUi

