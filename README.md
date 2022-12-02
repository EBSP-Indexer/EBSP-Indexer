![Alt text](resources\ebsd_gui.png?raw=true "Electron backscatter diffraction - Graphicacl User Interface")

Student project, work in progress, not suitable for use

Developing an EBSD GUI based on the kikuchipy package

## Setting up the repository
Requirements: 
- Python >= 3.10 (Tested on 3.10, but >=3.7 should work.)
- [Visual Studio Code](https://code.visualstudio.com/) (Optional, but recommended)
- [Qt Designer](https://build-system.fman.io/qt-designer-download) (Optional for designing GUI elements)

1. Clone or fork the repository to your local computer using git. If you don't have much experience with git, we recommend [Visual Studio Code's solution for git.](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette)
Alternativly you could download the repo as a zip and upack it manually.
![Alt text](resources\tutorial\tutorial_clone_repo.png?raw=true "Figure for cloning the git repository, copy the link to get started")
2. Open the repository in any terminal. The next step is to create a virtual evironment for the repository. This can be done by executing the following command in the root directory (same directory that includes requirements.txt):
    ```
    python3 -m venv env
    ```
    Then activte the enviroment in your current running terminal, e.g. for windows by executing:
    ```
    & env/Scripts/Activate.ps1
    ```
    Make sure that the enviroment has been activated by executing:
    ```
    pip -V
    ```
    The path returned should include ...\env\lib\site-packages\pip. 
    NOTE: Make sure that the environment is ALWAYS activated when executing commands related to the project. 
3. Once the environment is active, install the necessary packages by executing: 
    ```
    pip install -r requirements.txt
    ```
4. The program should now be able to run by executing the following in the root directory:
    ```
    python main.py
    ```

## Update Modules 
You can get the name and version number of every package installed in the virtual environment by  executing
```
pip list
```

## Bundle with pyinstaller
auto-py-to-exe -c pyinstaller_config.json

## Working with Qt Designer and python tutorial
The following describes a workflow for designing GUI elements and then add Python code to the elements.
![Alt text](resources\tutorial\tutorial_workflow.png?raw=true "Figure for cloning the git repository, copy the link to get started")

### Qt Designer
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
There are VScode extensions that automatically compiles the .ui file to a .py file every time the .ui is uptated. It is highly recommended to install the extension ["Qt for python".](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python)

### Python logic
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

### Naming
- Functions/ variables containing PyQt logic and pure Qt elements uses camelCase
- Functions/ variables that contain python code and other libraries uses snake_case