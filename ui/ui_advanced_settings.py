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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_AdvancedSettings(object):
    def setupUi(self, AdvancedSettings):
        if not AdvancedSettings.objectName():
            AdvancedSettings.setObjectName(u"AdvancedSettings")
        AdvancedSettings.resize(393, 392)
        self.gridLayout = QGridLayout(AdvancedSettings)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.indexingTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AdvancedSettings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preProcessingTab), QCoreApplication.translate("AdvancedSettings", u"Pre Prosessing", None))
        self.label.setText(QCoreApplication.translate("AdvancedSettings", u"Default settings:", None))
        self.lazyLoadingBox.setText(QCoreApplication.translate("AdvancedSettings", u"Lazy Loading (recommended)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indexingTab), QCoreApplication.translate("AdvancedSettings", u"Indexing", None))
    # retranslateUi

