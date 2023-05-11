# Setup of development installation
## Devlopment Requirements: 
- Python >= 3.10 (Tested on 3.10, but >=3.7 should work.)
- [Microsoft Visual C++ Redistributable packages for Visual Studio 2015, 2017, 2019, and 2022](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- [Visual Studio Code](https://code.visualstudio.com/) (Optional, but recommended)
- [Qt Designer](https://build-system.fman.io/qt-designer-download) (Optional for designing GUI elements)

In addition, it is recommended for users on MacOS with Apple Silicon to use a conda environment. See [pyebsdindex's additional installation for macOS with Apple Silicon.](https://pyebsdindex.readthedocs.io/en/stable/installation.html)

## Setting up the repository
1. Clone or fork the repository to your local computer using git. It is recommended to put the repository just under your local disk, so that the root directory is C:/EBSP-Indexer. If you don't have much experience with git, we recommend [Visual Studio Code's solution for git.](https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette)
Alternativly you could download the repo as a zip and upack it manually.

![Alt text](https://github.com/EBSP-Indexer/EBSP-Indexer/blob/dev/resources/tutorial/tutorial_clone_repo.png?raw=true "Figure for cloning the git repository, copy the link to get started")

2. Open the repository in any terminal. The next step is to create a virtual evironment for the repository. This can be done by executing the following command in the root directory (same directory that includes requirements.txt):
    ```
    python3 -m venv env
    ```
    Then activte the enviroment in your current running terminal, e.g. for windows powershell by executing:
    ```
    & env/Scripts/Activate.ps1
    ```
    Make sure that the enviroment has been activated by executing:
    ```
    pip -V
    ```
    The path returned should include ...\env\lib\site-packages\pip. 
    NOTE: Make sure that the environment is ALWAYS activated when executing commands related to the project. 
3. Once the environment is active, install the necessary packages from the appropriate requirements_*.txt for your system, e.g. for Windows: 
    ```
    pip install -r requirements_WINDOWS.txt
    ```
4. The program should now be able to run by executing the following in the root directory:
    ```
    python main.py
    ```