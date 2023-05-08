![Alt text](https://github.com/htrellin/EBSD-GUI/blob/main/resources/ebsd_gui.png?raw=true "Electron backscatter diffraction - Graphicacl User Interface")
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

EBSD-GUI is a graphical user interface that allows for processing and indexing of Electron backscatter patterns (EBSP), generated by scanning electron microscopes (SEM). It's goal is to make the rich functionality of the open source library [Kikutchipy](https://zenodo.org/record/7263012) more accessible to users, without requireing knowledge of python or the library itself.

NB! The portable version requires [Microsoft Visual C++ Redistributable packages for Visual Studio 2015, 2017, 2019, and 2022.](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)

The GUI supports:
- Dictionary and Hough indexing
- Signal improvements
    - Static background removal
    - Dynamic background removal
    - Averaging by neighbour patterns
- Pattern center calibration
- Region of interest
- Signal navigation
- Pre- and post-indexing maps
- Interactive interpreter for python
- Customizable settings

The project is developed by students at [The Department of Material Science](https://www.ntnu.edu/ima/research/emlab) at [Norwegian University of Science and Techonolgy (NTNU)](https://www.ntnu.edu/), and is open source and free to use.

WARNING: The software is still in early development and can produce unrelaible results, and should therefor be used at own risk. 

# Tutorials
## Setting up the repository
Requirements: 
- Python >= 3.10 (Tested on 3.10, but >=3.7 should work.)
- [Microsoft Visual C++ Redistributable packages for Visual Studio 2015, 2017, 2019, and 2022](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- [Visual Studio Code](https://code.visualstudio.com/) (Optional, but recommended)
- [Qt Designer](https://build-system.fman.io/qt-designer-download) (Optional for designing GUI elements)

1. Clone or fork the repository to your local computer using git. It is recommended to put the repository just under your local disk, so that the root directory is C:/EBSD-GUI. If you don't have much experience with git, we recommend [Visual Studio Code's solution for git.](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette)
Alternativly you could download the repo as a zip and upack it manually.

![Alt text](https://github.com/htrellin/EBSD-GUI/blob/dev/resources/tutorial/tutorial_clone_repo.png?raw=true "Figure for cloning the git repository, copy the link to get started")

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
This requires that you have already set up the repository and virtual environment, see previous section on how to do so.

You can get the name and version number of every package installed in the virtual environment by  executing:
```
pip list
```
To update a package, add the argument --upgrade to the pip install command, e.g. for kikutchipy like this:
```
pip install --upgrade kikutchipy 
```
If you want to update requirements.txt to use new packages or newer versions of existing packages that are now installed in your environment, execute:
```
pip freeze > requirements.txt 
```

## Bundle with pyinstaller
To bundle the program into a directory with a single executable you can use the packages pyinstaller and auto-py-to-exe. These packages should already be installed if you used pip install together with the requirements.txt. To create an executable that runs on Windows you will need to create the bundle on a Windows computer. Therefor an executable that runs on MacOS (.app file), must be made using a Mac.

An easy way to interact with pyinstaller is to run it through the auto-py-to-exe package. Running the following command will load a user interface with the configuration made for this project. 
```
auto-py-to-exe -c pyinstaller_config.json
```
In this interface you can edit the name and icon used for the executable, what image is used for the splash screen, and much more. Expand all sections and make sure that all paths are correct, corresponding with their respective locations on your computer. If your root-folder for the repository is C:/EBSD-GUI, all paths loaded from the configuration should already be correct.

Feel free to edit or add any parameters in the interface. You can also save the configuration by going to "Settings -> Configuration -> Export Config to JSON File".

When you are finished, create the bundle by clicking the bottom button CONVERT .PY TO .EXE. It might take some time for the program to create the bundle. In the end, the bundle/directory is put under your root-directory inside a folder called output. It is recommended to select the folder inside the output and package it into a .zip, so it can easily be shared. 

## Working with Qt Designer and python tutorial
The following describes a workflow for designing GUI elements and then add Python code to the elements.

![Alt text](https://github.com/htrellin/EBSD-GUI/blob/dev/resources/tutorial/tutorial_workflow.png?raw=true "Figure for cloning the git repository, copy the link to get started")

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
There are VScode extensions that automatically compiles the .ui file to a .py file every time the .ui is uptated. It is highly recommended to install [Qt for python extension.](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python)

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

### Naming convention
- Functions/ variables containing PyQt logic and pure Qt elements uses camelCase
- Functions/ variables that contain python code and other libraries uses snake_case

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/olavlet"><img src="https://avatars.githubusercontent.com/u/113110330?v=4?s=100" width="100px;" alt="olavlet"/><br /><sub><b>olavlet</b></sub></a><br /><a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=olavlet" title="Code">💻</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/issues?q=author%3Aolavlet" title="Bug reports">🐛</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=olavlet" title="Documentation">📖</a> <a href="#ideas-olavlet" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/htrellin"><img src="https://avatars.githubusercontent.com/u/80631936?v=4?s=100" width="100px;" alt="htrellin"/><br /><sub><b>htrellin</b></sub></a><br /><a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=htrellin" title="Code">💻</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/issues?q=author%3Ahtrellin" title="Bug reports">🐛</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=htrellin" title="Documentation">📖</a> <a href="#ideas-htrellin" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!