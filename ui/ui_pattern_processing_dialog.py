# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pattern_processing_dialog.ui'
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
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from mplwidget import MplWidget

class Ui_PatternProcessingWindow(object):
    def setupUi(self, PatternProcessingWindow):
        if not PatternProcessingWindow.objectName():
            PatternProcessingWindow.setObjectName(u"PatternProcessingWindow")
        PatternProcessingWindow.resize(926, 566)
        self.gridLayout_2 = QGridLayout(PatternProcessingWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(PatternProcessingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.staticBackgroundBox = QCheckBox(self.centralwidget)
        self.staticBackgroundBox.setObjectName(u"staticBackgroundBox")
        self.staticBackgroundBox.setChecked(False)
        self.staticBackgroundBox.setTristate(False)

        self.verticalLayout.addWidget(self.staticBackgroundBox)

        self.dynamicBackgroundBox = QCheckBox(self.centralwidget)
        self.dynamicBackgroundBox.setObjectName(u"dynamicBackgroundBox")
        self.dynamicBackgroundBox.setChecked(False)

        self.verticalLayout.addWidget(self.dynamicBackgroundBox)

        self.averageBox = QCheckBox(self.centralwidget)
        self.averageBox.setObjectName(u"averageBox")
        self.averageBox.setChecked(False)

        self.verticalLayout.addWidget(self.averageBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.label_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.previewWidget = MplWidget(self.centralwidget)
        self.previewWidget.setObjectName(u"previewWidget")
        self.previewWidget.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_4.addWidget(self.previewWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_4.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.folderLabel = QLabel(self.centralwidget)
        self.folderLabel.setObjectName(u"folderLabel")

        self.horizontalLayout_5.addWidget(self.folderLabel)

        self.folderEdit = QLabel(self.centralwidget)
        self.folderEdit.setObjectName(u"folderEdit")

        self.horizontalLayout_5.addWidget(self.folderEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filenameLabel = QLabel(self.centralwidget)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.horizontalLayout.addWidget(self.filenameLabel)

        self.filenameEdit = QLineEdit(self.centralwidget)
        self.filenameEdit.setObjectName(u"filenameEdit")
        self.filenameEdit.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.filenameEdit)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.browseButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 4, 1, 1, 1)

        QWidget.setTabOrder(self.staticBackgroundBox, self.dynamicBackgroundBox)
        QWidget.setTabOrder(self.dynamicBackgroundBox, self.averageBox)
        QWidget.setTabOrder(self.averageBox, self.browseButton)

        self.retranslateUi(PatternProcessingWindow)

        QMetaObject.connectSlotsByName(PatternProcessingWindow)
    # setupUi

    def retranslateUi(self, PatternProcessingWindow):
        PatternProcessingWindow.setWindowTitle(QCoreApplication.translate("PatternProcessingWindow", u"Pattern Processing", None))
        self.label.setText(QCoreApplication.translate("PatternProcessingWindow", u"Pre-processing steps", None))
#if QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Remove the static background inplace.", None))
#endif // QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Remove static background noise", None))
#if QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Remove the dynamic background in an EBSD pattern.", None))
#endif // QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Remove dynamic background noise", None))
#if QT_CONFIG(whatsthis)
        self.averageBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Average a chunk of patterns with its neighbours within a window.", None))
#endif // QT_CONFIG(whatsthis)
        self.averageBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Average neighbour patterns", None))
        self.label_2.setText(QCoreApplication.translate("PatternProcessingWindow", u"Preview of pattern processing", None))
        self.folderLabel.setText(QCoreApplication.translate("PatternProcessingWindow", u"Working folder:", None))
        self.folderEdit.setText(QCoreApplication.translate("PatternProcessingWindow", u"TextLabel", None))
        self.filenameLabel.setText(QCoreApplication.translate("PatternProcessingWindow", u"Filename:", None))
        self.browseButton.setText(QCoreApplication.translate("PatternProcessingWindow", u"Browse", None))
    # retranslateUi

