# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_PatternProcessingWindow(object):
    def setupUi(self, PatternProcessingWindow):
        if not PatternProcessingWindow.objectName():
            PatternProcessingWindow.setObjectName(u"PatternProcessingWindow")
        PatternProcessingWindow.resize(803, 228)
        self.gridLayout_2 = QGridLayout(PatternProcessingWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(PatternProcessingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.dynamicBackgroundBox = QCheckBox(self.centralwidget)
        self.dynamicBackgroundBox.setObjectName(u"dynamicBackgroundBox")
        self.dynamicBackgroundBox.setChecked(True)

        self.gridLayout.addWidget(self.dynamicBackgroundBox, 2, 0, 1, 1)

        self.pathLineEdit = QLineEdit(self.centralwidget)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.pathLineEdit, 5, 1, 1, 1)

        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pathLabel, 5, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 2, 1, 1)

        self.averageBox = QCheckBox(self.centralwidget)
        self.averageBox.setObjectName(u"averageBox")
        self.averageBox.setChecked(True)

        self.gridLayout.addWidget(self.averageBox, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(40, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setEnabled(True)
        self.browseButton.setLayoutDirection(Qt.LeftToRight)
        self.browseButton.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.browseButton, 5, 2, 1, 1)

        self.staticBackgroundBox = QCheckBox(self.centralwidget)
        self.staticBackgroundBox.setObjectName(u"staticBackgroundBox")
        self.staticBackgroundBox.setChecked(True)
        self.staticBackgroundBox.setTristate(False)

        self.gridLayout.addWidget(self.staticBackgroundBox, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(PatternProcessingWindow)

        QMetaObject.connectSlotsByName(PatternProcessingWindow)
    # setupUi

    def retranslateUi(self, PatternProcessingWindow):
        PatternProcessingWindow.setWindowTitle(QCoreApplication.translate("PatternProcessingWindow", u"Pattern Processing", None))
#if QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Remove the dynamic background in an EBSD pattern.", None))
#endif // QT_CONFIG(whatsthis)
        self.dynamicBackgroundBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Remove dynamic background noise", None))
        self.pathLabel.setText(QCoreApplication.translate("PatternProcessingWindow", u"Filepath of processed pattern:", None))
#if QT_CONFIG(whatsthis)
        self.averageBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Average a chunk of patterns with its neighbours within a window.", None))
#endif // QT_CONFIG(whatsthis)
        self.averageBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Average neighbour patterns", None))
        self.browseButton.setText(QCoreApplication.translate("PatternProcessingWindow", u"Browse", None))
#if QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setWhatsThis(QCoreApplication.translate("PatternProcessingWindow", u"Remove the static background inplace.", None))
#endif // QT_CONFIG(whatsthis)
        self.staticBackgroundBox.setText(QCoreApplication.translate("PatternProcessingWindow", u"Remove static background noise", None))
    # retranslateUi
