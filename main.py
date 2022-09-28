from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100,100,480,480)
    win.setWindowTitle("Olav sitt vindu")

    label = QtWidgets.QLabel(win)
    label.setText("Olav var her")
    label.move(50,50)

    win.show()
    sys.exit(app.exec())

def main():
    window()

    return 0

main()