# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hi_setup.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_HISetupDialog(object):
    def setupUi(self, HISetupDialog):
        if not HISetupDialog.objectName():
            HISetupDialog.setObjectName(u"HISetupDialog")
        HISetupDialog.resize(848, 469)
        self.gridLayout = QGridLayout(HISetupDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(HISetupDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBoxBinning = QComboBox(self.frame)
        self.comboBoxBinning.setObjectName(u"comboBoxBinning")
        self.comboBoxBinning.setMaximumSize(QSize(80, 16777215))
        self.comboBoxBinning.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.comboBoxBinning)

        self.labelSignalShape = QLabel(self.frame)
        self.labelSignalShape.setObjectName(u"labelSignalShape")

        self.horizontalLayout_2.addWidget(self.labelSignalShape)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.spinBoxBands = QSpinBox(self.frame)
        self.spinBoxBands.setObjectName(u"spinBoxBands")
        self.spinBoxBands.setMaximumSize(QSize(60, 16777215))
        self.spinBoxBands.setMinimum(3)
        self.spinBoxBands.setMaximum(20)
        self.spinBoxBands.setValue(9)

        self.verticalLayout_5.addWidget(self.spinBoxBands)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSliderRho = QSlider(self.frame)
        self.horizontalSliderRho.setObjectName(u"horizontalSliderRho")
        self.horizontalSliderRho.setMinimum(40)
        self.horizontalSliderRho.setMaximum(100)
        self.horizontalSliderRho.setValue(85)
        self.horizontalSliderRho.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSliderRho)

        self.labelRho = QLabel(self.frame)
        self.labelRho.setObjectName(u"labelRho")

        self.horizontalLayout_5.addWidget(self.labelRho)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.checkBoxLazy = QCheckBox(self.frame)
        self.checkBoxLazy.setObjectName(u"checkBoxLazy")
        self.checkBoxLazy.setEnabled(True)
        self.checkBoxLazy.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxLazy.setCheckable(True)
        self.checkBoxLazy.setChecked(True)
        self.checkBoxLazy.setTristate(False)

        self.verticalLayout.addWidget(self.checkBoxLazy)

        self.checkBoxOrientation = QCheckBox(self.frame)
        self.checkBoxOrientation.setObjectName(u"checkBoxOrientation")
        self.checkBoxOrientation.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxOrientation)

        self.checkBoxPhase = QCheckBox(self.frame)
        self.checkBoxPhase.setObjectName(u"checkBoxPhase")

        self.verticalLayout.addWidget(self.checkBoxPhase)

        self.checkBoxQuality = QCheckBox(self.frame)
        self.checkBoxQuality.setObjectName(u"checkBoxQuality")

        self.verticalLayout.addWidget(self.checkBoxQuality)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tableWidgetPhase = QTableWidget(self.frame)
        if (self.tableWidgetPhase.columnCount() < 5):
            self.tableWidgetPhase.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidgetPhase.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidgetPhase.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setPointSize(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidgetPhase.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        font2 = QFont()
        font2.setPointSize(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidgetPhase.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font3 = QFont()
        font3.setPointSize(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidgetPhase.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidgetPhase.setObjectName(u"tableWidgetPhase")
        self.tableWidgetPhase.setMinimumSize(QSize(470, 50))
        self.tableWidgetPhase.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetPhase.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidgetPhase.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetPhase.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tableWidgetPhase)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButtonAddPhase = QPushButton(self.frame)
        self.pushButtonAddPhase.setObjectName(u"pushButtonAddPhase")
        self.pushButtonAddPhase.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.pushButtonAddPhase)

        self.pushButtonLoadPhase = QPushButton(self.frame)
        self.pushButtonLoadPhase.setObjectName(u"pushButtonLoadPhase")

        self.horizontalLayout_3.addWidget(self.pushButtonLoadPhase)

        self.pushButtonRemovePhase = QPushButton(self.frame)
        self.pushButtonRemovePhase.setObjectName(u"pushButtonRemovePhase")

        self.horizontalLayout_3.addWidget(self.pushButtonRemovePhase)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.patternCenterY = QDoubleSpinBox(self.frame)
        self.patternCenterY.setObjectName(u"patternCenterY")
        self.patternCenterY.setDecimals(3)
        self.patternCenterY.setMaximum(1.000000000000000)
        self.patternCenterY.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterY, 1, 2, 1, 1)

        self.patternCenterX = QDoubleSpinBox(self.frame)
        self.patternCenterX.setObjectName(u"patternCenterX")
        self.patternCenterX.setDecimals(3)
        self.patternCenterX.setMaximum(1.000000000000000)
        self.patternCenterX.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterX, 0, 2, 1, 1)

        self.patternCenterZ = QDoubleSpinBox(self.frame)
        self.patternCenterZ.setObjectName(u"patternCenterZ")
        self.patternCenterZ.setDecimals(3)
        self.patternCenterZ.setMaximum(3.000000000000000)
        self.patternCenterZ.setSingleStep(0.001000000000000)

        self.gridLayout_2.addWidget(self.patternCenterZ, 2, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBoxConvention = QComboBox(self.frame)
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.addItem("")
        self.comboBoxConvention.setObjectName(u"comboBoxConvention")

        self.horizontalLayout.addWidget(self.comboBoxConvention)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(9, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(134, 388, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxLazy, self.checkBoxPhase)
        QWidget.setTabOrder(self.checkBoxPhase, self.checkBoxQuality)
        QWidget.setTabOrder(self.checkBoxQuality, self.pushButtonLoadPhase)
        QWidget.setTabOrder(self.pushButtonLoadPhase, self.pushButtonRemovePhase)
        QWidget.setTabOrder(self.pushButtonRemovePhase, self.patternCenterX)
        QWidget.setTabOrder(self.patternCenterX, self.patternCenterY)
        QWidget.setTabOrder(self.patternCenterY, self.patternCenterZ)

        self.retranslateUi(HISetupDialog)
        self.buttonBox.rejected.connect(HISetupDialog.reject)
        self.buttonBox.accepted.connect(HISetupDialog.accept)

        QMetaObject.connectSlotsByName(HISetupDialog)
    # setupUi

    def retranslateUi(self, HISetupDialog):
        HISetupDialog.setWindowTitle(QCoreApplication.translate("HISetupDialog", u"Hough Indexing", None))
        self.label_7.setText(QCoreApplication.translate("HISetupDialog", u"Binning", None))
#if QT_CONFIG(tooltip)
        self.comboBoxBinning.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Detector binning, i.e. how many pixels are binned into one, default is no binning</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSignalShape.setText(QCoreApplication.translate("HISetupDialog", u"Signal shape: ", None))
        self.label_9.setText(QCoreApplication.translate("HISetupDialog", u"Number of bands", None))
#if QT_CONFIG(tooltip)
        self.spinBoxBands.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Number of detected bands to use in triplet voting, default is 9</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("HISetupDialog", u"Rho fraction (\u03c1) ", None))
#if QT_CONFIG(tooltip)
        self.horizontalSliderRho.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>The fraction of the pattern to be considered when detecting bands, default is 85%. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelRho.setText(QCoreApplication.translate("HISetupDialog", u"85%", None))
        self.checkBoxLazy.setText(QCoreApplication.translate("HISetupDialog", u"Lazy loading of patterns", None))
        self.checkBoxOrientation.setText(QCoreApplication.translate("HISetupDialog", u"Generate orientation maps", None))
        self.checkBoxPhase.setText(QCoreApplication.translate("HISetupDialog", u"Generate phase maps", None))
        self.checkBoxQuality.setText(QCoreApplication.translate("HISetupDialog", u"Generate quality metrics for combined maps", None))
        self.label.setText(QCoreApplication.translate("HISetupDialog", u"Phases", None))
        ___qtablewidgetitem = self.tableWidgetPhase.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HISetupDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidgetPhase.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HISetupDialog", u"Number", None));
        ___qtablewidgetitem2 = self.tableWidgetPhase.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HISetupDialog", u"ISS", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("HISetupDialog", u"International short symbol", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tableWidgetPhase.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HISetupDialog", u"Crystal System", None));
        ___qtablewidgetitem4 = self.tableWidgetPhase.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("HISetupDialog", u"Color", None));
#if QT_CONFIG(tooltip)
        self.pushButtonAddPhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Create and add a custom phase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonAddPhase.setText(QCoreApplication.translate("HISetupDialog", u"Add", None))
#if QT_CONFIG(tooltip)
        self.pushButtonLoadPhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Add phase from master pattern (*.h5)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLoadPhase.setText(QCoreApplication.translate("HISetupDialog", u"Load", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemovePhase.setToolTip(QCoreApplication.translate("HISetupDialog", u"<html><head/><body><p>Remove the selected phase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemovePhase.setText(QCoreApplication.translate("HISetupDialog", u"Remove", None))
        self.label_2.setText(QCoreApplication.translate("HISetupDialog", u"Pattern center", None))
        self.patternCenterZ.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("HISetupDialog", u"X:", None))
        self.label_4.setText(QCoreApplication.translate("HISetupDialog", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("HISetupDialog", u"Z:", None))
        self.label_6.setText(QCoreApplication.translate("HISetupDialog", u"PC convention", None))
        self.comboBoxConvention.setItemText(0, QCoreApplication.translate("HISetupDialog", u"BRUKER", None))
        self.comboBoxConvention.setItemText(1, QCoreApplication.translate("HISetupDialog", u"TSL", None))

    # retranslateUi

