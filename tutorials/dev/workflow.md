# Working with Qt Designer and python
The following describes a workflow for designing GUI elements and then add Python code to the elements.

![Alt text](https://github.com/EBSP-Indexer/EBSP-Indexer/blob/dev/resources/tutorial/tutorial_workflow.png?raw=true "Figure for cloning the git repository, copy the link to get started")

## Qt Designer
Design the gui component using Qt designer and save the file with an .ui extension. 
Note that when creating a new Qt form the template/ forms you are presented with decides the base class of that ui.
This is important, as the future python class (containing python logic) should inherit this ui and in doing so its base class.
This decides what Qt methods are available to the python class itself.
There are 3 classes of importance:
- QMainWindow: A standalone window with no parent window/ widget. The main application uses this type of window.
- QDialog: A popup window that originates from another window, usually the main window.
- QWidget: Basic GUI element that can be part of a window or create custom elements

After the ui file is created, the file can be compiled to python code using: 
```
pyuic4 input.ui -o output.py
```
There are VScode extensions that automatically compiles the .ui file to a .py file every time the .ui is uptated. It is highly recommended to install [Qt for python extension.](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python)

## Python logic
Create a python class in its own .py file that will contain the logic for the GUI element.
The class should have the UI baseclass as its super. 
Import the Ui class that was generated in the .py file from the .ui file.
This class will be the Ui class of our python logic class.
After initializing the Ui class in our Python class to the variable self.ui, call self.ui.setupUi(self) to set up the designed GUI.
Then another help method can be defined (e.g. setupConnections()) to connect self.ui and its elements to python functions/ logic. 

Example template
```
from ui.ui_python_widget import Ui_PythonWidget()

class PythonWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PythonWidget()
        self.ui.setupUi(self)
        self.setupConnections()
        ...

    def setupConnections(self):
        *Connect GUI elements that exists in Ui_QtForm() to python functions here
        ...
```

## Naming convention
- Functions/ variables containing PyQt logic and pure Qt elements uses camelCase
- Functions/ variables that contain python code and other libraries uses snake_case
