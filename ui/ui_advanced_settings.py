# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QCheckBox, QDialog, QDialogButtonBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AdvancedSettings(object):
    def setupUi(self, AdvancedSettings):
        if not AdvancedSettings.objectName():
            AdvancedSettings.setObjectName(u"AdvancedSettings")
        AdvancedSettings.resize(427, 402)
        self.gridLayout = QGridLayout(AdvancedSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(AdvancedSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(AdvancedSettings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.fileExplorerTab = QWidget()
        self.fileExplorerTab.setObjectName(u"fileExplorerTab")
        self.verticalLayout_5 = QVBoxLayout(self.fileExplorerTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.fileExplorerTab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.fileTypeList = QListWidget(self.fileExplorerTab)
        self.fileTypeList.setObjectName(u"fileTypeList")

        self.verticalLayout.addWidget(self.fileTypeList)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.fileExplorerTab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.fileTypeLineEdit = QLineEdit(self.fileExplorerTab)
        self.fileTypeLineEdit.setObjectName(u"fileTypeLineEdit")
        self.fileTypeLineEdit.setMinimumSize(QSize(50, 0))
        self.fileTypeLineEdit.setToolTipDuration(1)

        self.horizontalLayout_2.addWidget(self.fileTypeLineEdit, 0, Qt.AlignTop)

        self.addFileTypeButton = QPushButton(self.fileExplorerTab)
        self.addFileTypeButton.setObjectName(u"addFileTypeButton")

        self.horizontalLayout_2.addWidget(self.addFileTypeButton, 0, Qt.AlignTop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.fileExplorerTab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.removeFileTypeButton = QPushButton(self.fileExplorerTab)
        self.removeFileTypeButton.setObjectName(u"removeFileTypeButton")

        self.verticalLayout_2.addWidget(self.removeFileTypeButton)

        self.resetFileTypeButton = QPushButton(self.fileExplorerTab)
        self.resetFileTypeButton.setObjectName(u"resetFileTypeButton")

        self.verticalLayout_2.addWidget(self.resetFileTypeButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.fileExplorerTab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.directoryBox = QCheckBox(self.fileExplorerTab)
        self.directoryBox.setObjectName(u"directoryBox")
        self.directoryBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_5.addWidget(self.directoryBox)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.directoryEdit = QLineEdit(self.fileExplorerTab)
        self.directoryEdit.setObjectName(u"directoryEdit")

        self.horizontalLayout_6.addWidget(self.directoryEdit)

        self.browseDirectoryButton = QPushButton(self.fileExplorerTab)
        self.browseDirectoryButton.setObjectName(u"browseDirectoryButton")

        self.horizontalLayout_6.addWidget(self.browseDirectoryButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.fileExplorerTab, "")
        self.preProcessingTab = QWidget()
        self.preProcessingTab.setObjectName(u"preProcessingTab")
        self.verticalLayout_3 = QVBoxLayout(self.preProcessingTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.preProcessingTab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.brukerButton = QRadioButton(self.preProcessingTab)
        self.brukerButton.setObjectName(u"brukerButton")
        self.brukerButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.brukerButton)

        self.tslButton = QRadioButton(self.preProcessingTab)
        self.tslButton.setObjectName(u"tslButton")
        self.tslButton.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.tslButton)

        self.label_3 = QLabel(self.preProcessingTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.savePcsBox = QCheckBox(self.preProcessingTab)
        self.savePcsBox.setObjectName(u"savePcsBox")
        self.savePcsBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_3.addWidget(self.savePcsBox)

        self.line_2 = QFrame(self.preProcessingTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_9 = QLabel(self.preProcessingTab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.listWidgetMicroscopes = QListWidget(self.preProcessingTab)
        self.listWidgetMicroscopes.setObjectName(u"listWidgetMicroscopes")

        self.verticalLayout_3.addWidget(self.listWidgetMicroscopes)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonAddNewMicroscope = QPushButton(self.preProcessingTab)
        self.pushButtonAddNewMicroscope.setObjectName(u"pushButtonAddNewMicroscope")

        self.horizontalLayout_5.addWidget(self.pushButtonAddNewMicroscope)

        self.pushButtonRemoveMicroscope = QPushButton(self.preProcessingTab)
        self.pushButtonRemoveMicroscope.setObjectName(u"pushButtonRemoveMicroscope")

        self.horizontalLayout_5.addWidget(self.pushButtonRemoveMicroscope)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.preProcessingTab, "")
        self.indexingTab = QWidget()
        self.indexingTab.setObjectName(u"indexingTab")
        self.verticalLayout_4 = QVBoxLayout(self.indexingTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.indexingTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.lazyLoadingBox = QCheckBox(self.indexingTab)
        self.lazyLoadingBox.setObjectName(u"lazyLoadingBox")
        self.lazyLoadingBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.lazyLoadingBox)

        self.checkBoxRefine = QCheckBox(self.indexingTab)
        self.checkBoxRefine.setObjectName(u"checkBoxRefine")

        self.verticalLayout_4.addWidget(self.checkBoxRefine)

        self.label_7 = QLabel(self.indexingTab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.colorTreeWidget = QTreeWidget(self.indexingTab)
        font = QFont()
        font.setPointSize(13)
        font.setKerning(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(0, font);
        self.colorTreeWidget.setHeaderItem(__qtreewidgetitem)
        brush = QBrush(QColor(33, 33, 33, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        brush2 = QBrush(QColor(255, 38, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        __qtreewidgetitem1 = QTreeWidgetItem(self.colorTreeWidget)
        __qtreewidgetitem1.setFlags(Qt.ItemIsEnabled);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem2.setBackground(0, brush);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        __qtreewidgetitem5.setFont(0, font1);
        __qtreewidgetitem5.setBackground(0, brush2);
        __qtreewidgetitem5.setForeground(0, brush1);
        self.colorTreeWidget.setObjectName(u"colorTreeWidget")
        self.colorTreeWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorTreeWidget.sizePolicy().hasHeightForWidth())
        self.colorTreeWidget.setSizePolicy(sizePolicy)
        self.colorTreeWidget.setMinimumSize(QSize(0, 0))
        self.colorTreeWidget.setMaximumSize(QSize(320, 16777215))
        self.colorTreeWidget.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setBold(False)
        self.colorTreeWidget.setFont(font2)
        self.colorTreeWidget.setLayoutDirection(Qt.LeftToRight)
        self.colorTreeWidget.setAutoFillBackground(False)
        self.colorTreeWidget.setStyleSheet(u"background-color: transparent")
        self.colorTreeWidget.setFrameShape(QFrame.NoFrame)
        self.colorTreeWidget.setFrameShadow(QFrame.Plain)
        self.colorTreeWidget.setLineWidth(1)
        self.colorTreeWidget.setMidLineWidth(0)
        self.colorTreeWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.colorTreeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.colorTreeWidget.setProperty("showDropIndicator", False)
        self.colorTreeWidget.setAlternatingRowColors(False)
        self.colorTreeWidget.setRootIsDecorated(True)
        self.colorTreeWidget.setUniformRowHeights(False)
        self.colorTreeWidget.setItemsExpandable(True)
        self.colorTreeWidget.setSortingEnabled(False)
        self.colorTreeWidget.setAnimated(False)
        self.colorTreeWidget.setAllColumnsShowFocus(False)
        self.colorTreeWidget.setWordWrap(False)
        self.colorTreeWidget.setExpandsOnDoubleClick(True)
        self.colorTreeWidget.setColumnCount(2)
        self.colorTreeWidget.header().setVisible(False)
        self.colorTreeWidget.header().setMinimumSectionSize(19)

        self.verticalLayout_4.addWidget(self.colorTreeWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.indexingTab, "")
        self.apperanceTab = QWidget()
        self.apperanceTab.setObjectName(u"apperanceTab")
        self.verticalLayout_6 = QVBoxLayout(self.apperanceTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.apperanceTab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lightRadioButton = QRadioButton(self.apperanceTab)
        self.lightRadioButton.setObjectName(u"lightRadioButton")
        self.lightRadioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.lightRadioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.darkRadioButton = QRadioButton(self.apperanceTab)
        self.darkRadioButton.setObjectName(u"darkRadioButton")

        self.horizontalLayout_4.addWidget(self.darkRadioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.tabWidget.addTab(self.apperanceTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(AdvancedSettings)
        self.buttonBox.accepted.connect(AdvancedSettings.accept)
        self.buttonBox.rejected.connect(AdvancedSettings.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdvancedSettings)
    # setupUi

    def retranslateUi(self, AdvancedSettings):
        AdvancedSettings.setWindowTitle(QCoreApplication.translate("AdvancedSettings", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("AdvancedSettings", u"File types shown in file explorer:", None))
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.fileTypeLineEdit.setToolTip(QCoreApplication.translate("AdvancedSettings", u"Write desired file type here", None))
#endif // QT_CONFIG(tooltip)
        self.addFileTypeButton.setText(QCoreApplication.translate("AdvancedSettings", u"Add", None))
        self.removeFileTypeButton.setText(QCoreApplication.translate("AdvancedSettings", u"Remove", None))
        self.resetFileTypeButton.setText(QCoreApplication.translate("AdvancedSettings", u"Reset", None))
        self.label_6.setText(QCoreApplication.translate("AdvancedSettings", u"Default directory:", None))
        self.directoryBox.setText(QCoreApplication.translate("AdvancedSettings", u"Enable default directory", None))
        self.browseDirectoryButton.setText(QCoreApplication.translate("AdvancedSettings", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fileExplorerTab), QCoreApplication.translate("AdvancedSettings", u"File Explorer", None))
        self.label_2.setText(QCoreApplication.translate("AdvancedSettings", u"Default Convention:", None))
        self.brukerButton.setText(QCoreApplication.translate("AdvancedSettings", u"Bruker", None))
        self.tslButton.setText(QCoreApplication.translate("AdvancedSettings", u"TSL", None))
        self.label_3.setText(QCoreApplication.translate("AdvancedSettings", u"Pattern Center Refinement:", None))
        self.savePcsBox.setText(QCoreApplication.translate("AdvancedSettings", u"Save individual pattern data to project settings file ", None))
        self.label_9.setText(QCoreApplication.translate("AdvancedSettings", u"Calibrated microscopes", None))
        self.pushButtonAddNewMicroscope.setText(QCoreApplication.translate("AdvancedSettings", u"Add new microscope", None))
        self.pushButtonRemoveMicroscope.setText(QCoreApplication.translate("AdvancedSettings", u"Remove microscope", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preProcessingTab), QCoreApplication.translate("AdvancedSettings", u"Pre Prosessing", None))
        self.label.setText(QCoreApplication.translate("AdvancedSettings", u"Default settings:", None))
        self.lazyLoadingBox.setText(QCoreApplication.translate("AdvancedSettings", u"Lazy Loading (recommended)", None))
        self.checkBoxRefine.setText(QCoreApplication.translate("AdvancedSettings", u"Refine orientations", None))
        self.label_7.setText(QCoreApplication.translate("AdvancedSettings", u"Colors:", None))
        ___qtreewidgetitem = self.colorTreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("AdvancedSettings", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AdvancedSettings", u"1", None));

        __sortingEnabled = self.colorTreeWidget.isSortingEnabled()
        self.colorTreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.colorTreeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("AdvancedSettings", u"Default phase map colors", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("AdvancedSettings", u"\u25a0", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("AdvancedSettings", u"Phase 1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("AdvancedSettings", u"\u25a0", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("AdvancedSettings", u"Phase 2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("AdvancedSettings", u"\u25a0", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("AdvancedSettings", u"Phase 3", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("AdvancedSettings", u"\u25a0", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("AdvancedSettings", u"Phase 4", None));
        self.colorTreeWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indexingTab), QCoreApplication.translate("AdvancedSettings", u"Indexing", None))
#if QT_CONFIG(accessibility)
        self.apperanceTab.setAccessibleName(QCoreApplication.translate("AdvancedSettings", u"Apperance", None))
#endif // QT_CONFIG(accessibility)
        self.label_8.setText(QCoreApplication.translate("AdvancedSettings", u"Theme", None))
        self.lightRadioButton.setText(QCoreApplication.translate("AdvancedSettings", u"Light", None))
        self.darkRadioButton.setText(QCoreApplication.translate("AdvancedSettings", u"Dark", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.apperanceTab), QCoreApplication.translate("AdvancedSettings", u"Apperance", None))
    # retranslateUi

