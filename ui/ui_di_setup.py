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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_DiSetupDialog(object):
    def setupUi(self, DiSetupDialog):
        if not DiSetupDialog.objectName():
            DiSetupDialog.setObjectName(u"DiSetupDialog")
        DiSetupDialog.resize(778, 430)
        self.gridLayout_2 = QGridLayout(DiSetupDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralwidget = QFrame(DiSetupDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.lineEditPath = QLineEdit(self.centralwidget)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 11, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 12, 3, 1, 1)

        self.checkBoxRefine = QCheckBox(self.centralwidget)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")
        self.checkBoxRefine.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxRefine.setChecked(True)
        self.checkBoxRefine.setTristate(False)

        self.gridLayout.addWidget(self.checkBoxRefine, 5, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.checkBoxLazy = QCheckBox(self.centralwidget)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setChecked(True)

        self.gridLayout.addWidget(self.checkBoxLazy, 6, 1, 1, 1)

        self.patternCenterX = QDoubleSpinBox(self.centralwidget)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(4)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.000100000000000)

        self.gridLayout.addWidget(self.patternCenterX, 2, 1, 1, 1)

        self.patternCenterY = QDoubleSpinBox(self.centralwidget)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(4)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.000100000000000)

        self.gridLayout.addWidget(self.patternCenterY, 3, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.patternCenterZ = QDoubleSpinBox(self.centralwidget)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.patternCenterZ.setDecimals(4)
        self.patternCenterZ.setMaximum(1.000000000000000)
        self.patternCenterZ.setSingleStep(0.000100000000000)

        self.gridLayout.addWidget(self.patternCenterZ, 4, 1, 1, 1)

        self.listWidgetPhase = QListWidget(self.centralwidget)
        self.listWidgetPhase.setObjectName(u"listWidgetPhase")
        self.listWidgetPhase.setMinimumSize(QSize(0, 50))
        self.listWidgetPhase.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.listWidgetPhase, 9, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setLayoutDirection(Qt.LeftToRight)
        self.pathLabel.setScaledContents(False)
        self.pathLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.pathLabel, 9, 0, 1, 1)

        self.checkBoxMask = QCheckBox(self.centralwidget)
        self.checkBoxMask.setObjectName(u"checkBoxMask")

        self.gridLayout.addWidget(self.checkBoxMask, 7, 1, 1, 1)

        self.pushButtonBrowse = QPushButton(self.centralwidget)
        self.pushButtonBrowse.setObjectName(u"pushButtonBrowse")

        self.gridLayout.addWidget(self.pushButtonBrowse, 11, 3, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.comboBoxBinning = QComboBox(self.centralwidget)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")

        self.gridLayout.addWidget(self.comboBoxBinning, 2, 3, 1, 1)

        self.doubleSpinBoxStepSize = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxStepSize.setObjectName(u"doubleSpinBoxStepSize")
        self.doubleSpinBoxStepSize.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBoxStepSize, 3, 3, 1, 1)

        self.spinBoxNumIter = QSpinBox(self.centralwidget)
        self.spinBoxNumIter.setObjectName(u"spinBoxNumIter")
        self.spinBoxNumIter.setMaximum(99)

        self.gridLayout.addWidget(self.spinBoxNumIter, 4, 3, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddPhase = QPushButton(self.centralwidget)
        self.pushButtonAddPhase.setObjectName(u"pushButtonAddPhase")

        self.horizontalLayout.addWidget(self.pushButtonAddPhase)

        self.pushButtonRemovePhase = QPushButton(self.centralwidget)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout.addWidget(self.pushButtonRemovePhase)


        self.gridLayout.addLayout(self.horizontalLayout, 10, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralwidget, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxRefine, self.checkBoxLazy)
        QWidget.setTabOrder(self.checkBoxLazy, self.listWidgetPhase)
        QWidget.setTabOrder(self.listWidgetPhase, self.lineEditPath)

        self.retranslateUi(DiSetupDialog)

        QMetaObject.connectSlotsByName(DiSetupDialog)
    # setupUi

    def retranslateUi(self, DiSetupDialog):
        DiSetupDialog.setWindowTitle(QCoreApplication.translate("DiSetupDialog", u"Pattern Processing", None))
        self.lineEditPath.setText(QCoreApplication.translate("DiSetupDialog", u"C:\\EBSD data\\kikuchipy\\ebsd_simulations", None))
        self.label_4.setText(QCoreApplication.translate("DiSetupDialog", u"PC - z", None))
        self.checkBoxRefine.setText("")
        self.label_5.setText(QCoreApplication.translate("DiSetupDialog", u"Master patterns", None))
        self.label.setText(QCoreApplication.translate("DiSetupDialog", u"Refine", None))
        self.checkBoxLazy.setText("")
        self.label_3.setText(QCoreApplication.translate("DiSetupDialog", u"PC - y", None))
        self.label_6.setText(QCoreApplication.translate("DiSetupDialog", u"Lazy", None))
        self.label_2.setText(QCoreApplication.translate("DiSetupDialog", u"PC - x", None))
        self.label_7.setText(QCoreApplication.translate("DiSetupDialog", u"Binning shape", None))
        self.label_8.setText(QCoreApplication.translate("DiSetupDialog", u"Step-size (\u00b0)", None))
        self.pathLabel.setText(QCoreApplication.translate("DiSetupDialog", u"Phase", None))
        self.checkBoxMask.setText("")
        self.pushButtonBrowse.setText(QCoreApplication.translate("DiSetupDialog", u"Browse", None))
        self.label_9.setText(QCoreApplication.translate("DiSetupDialog", u"Use circular mask", None))
        self.label_10.setText(QCoreApplication.translate("DiSetupDialog", u"Matching per iteration", None))
        self.pushButtonAddPhase.setText(QCoreApplication.translate("DiSetupDialog", u"Add Phase", None))
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("DiSetupDialog", u"Remove Phase", None))
    # retranslateUi

