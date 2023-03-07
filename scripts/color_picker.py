from PySide6.QtWidgets import QDialog
from os.path import exists

from ui.ui_color_picker import Ui_color_picker

class ColorPicker(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_color_picker()
        self.ui.setupUi(self)
        self.setupConnections()
    
    def setupConnections(self):
        self.ui.pushButton.clicked.connect(lambda: self.buttonPushed(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.buttonPushed(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.buttonPushed(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.buttonPushed(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.buttonPushed(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.buttonPushed(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.buttonPushed(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.buttonPushed(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.buttonPushed(9))
        self.ui.pushButton_10.clicked.connect(lambda: self.buttonPushed(10))
        self.ui.pushButton_11.clicked.connect(lambda: self.buttonPushed(11))
        self.ui.pushButton_12.clicked.connect(lambda: self.buttonPushed(12))
        self.ui.pushButton_13.clicked.connect(lambda: self.buttonPushed(13))
        self.ui.pushButton_14.clicked.connect(lambda: self.buttonPushed(14))
        self.ui.pushButton_15.clicked.connect(lambda: self.buttonPushed(15))
        self.ui.pushButton_16.clicked.connect(lambda: self.buttonPushed(16))
    
    def buttonPushed(self, button):
        colors = [
            'blue', 'green', 'red', 'darkcyan', 'magenta', 'y', 'white', 'black',
            'cyan', 'orange', 'yellow', 'lime',
            'brown', 'pink', 'gray', 'olive'
        ]
        self.color = colors[button-1]
        self.accept()
        
        