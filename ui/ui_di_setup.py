# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'di_setup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QSizePolicy, QWidget)

class Ui_DiSetupWindow(object):
    def setupUi(self, DiSetupWindow):
        if not DiSetupWindow.objectName():
            DiSetupWindow.setObjectName(u"DiSetupWindow")
        DiSetupWindow.resize(702, 355)
        self.gridLayout_2 = QGridLayout(DiSetupWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(DiSetupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setScaledContents(False)
        self.pathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pathLabel, 5, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 2, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)


        self.retranslateUi(DiSetupWindow)

        QMetaObject.connectSlotsByName(DiSetupWindow)
    # setupUi

    def retranslateUi(self, DiSetupWindow):
        DiSetupWindow.setWindowTitle(QCoreApplication.translate("DiSetupWindow", u"Pattern Processing", None))
        self.pathLabel.setText(QCoreApplication.translate("DiSetupWindow", u"Phase", None))
        self.label_3.setText(QCoreApplication.translate("DiSetupWindow", u"PC - y", None))
        self.label_4.setText(QCoreApplication.translate("DiSetupWindow", u"PC - z", None))
        self.label_2.setText(QCoreApplication.translate("DiSetupWindow", u"PC - x", None))
    # retranslateUi

