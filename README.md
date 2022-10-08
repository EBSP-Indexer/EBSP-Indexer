# EBSD-GUI

Student project, work in progress, not suitable for use

Developing an EBSD GUI based on the kikuchipy package

testing git

## Naming
- Functions/ variables containing PyQt logic and pure Qt elements uses camelCase
- Functions/ variables that contain python code and other libraries uses snake_case

## Working with Qt Designer and python tutorial
The following describes a workflow for designing GUI elements and then add Python code to the element

### In .\ui\ui_QtForm

### In python_object.py:
from ui.ui_QtForm import Ui_QtForm

class PythonWidget(QWidget):
    def __init__(self, working_dir, save_path = "Pattern_avg.h5"):
        self.ui = Ui_QtForm()
        self.ui.setupUi(self)