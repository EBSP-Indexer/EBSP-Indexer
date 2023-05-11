# Distribute new versions

## Update Modules 
This requires that you have already set up the repository and virtual environment, see previous section on how to do so.

You can get the name and version number of every package installed in the virtual environment by  executing:
```
pip list
```
To update a package, add the argument --upgrade to the pip install command, e.g. for kikuchipy like this:
```
pip install --upgrade kikuchipy 
```
If you want to update requirements.txt to use new packages or newer versions of existing packages that are now installed in your environment, freeze the list and write it to the appropriate text file. For example, on Windows execute:
```
pip freeze > requirements.txt 
```

## Bundle with pyinstaller
To bundle the program into a directory with a single executable you can use the package pyinstaller. The package should already be installed if you used pip install together with the requirements_*.txt. To create an executable that runs on Windows you will need to create the bundle on a Windows computer. Therefor an executable that runs on MacOS (.app file), must be made using a Mac.

The bundle can be created by executing the `export.py` script from the root directory, e.g. on Windows:
```
python export.py
```
Inside the script, one can edit the name and icon used for the executable, among other things. All paths should automatically be correct, as long as the script is run in the root directory (the one containing `main.py`).


In the end, the bundle/package is put under the root-directory inside a folder called dist.

## Inno Setup Compiler (Windows)
To bundle the package into an installer which can easily be distributed, it is recommended to use Inno Setup on Windows. 

In Inno Setup, load the `setup_script.iss`, and edit any path which is not correct for your system. Make sure to update both the installer version and app version if creating a new release!

Make sure the unique "AppId" has the correct value: 
```
38A0E626-43E8-4E4A-8AE6-62FA6C9932D5
``` 
Use this so Windows recognizes the app and updates to the new version instead of installing a seperate new version.

## Platypus (macOS)
There is a problem with PyInstaller bundling GUI applications on the .app format. 
The most viable option is a workaround, which is to use Platypus to bundle the app distribution from PyInstaller into a second app. 

Platypus is a software tool which can create macOS application bundles from command line scripts or programs in a number of programming languages.
It can be installed via Homebrew.

Make sure that the following is correct for the app bundle made with Platypus:
![Alt text](https://github.com/EBSP-Indexer/EBSP-Indexer/blob/dev/resources/tutorial/tutorial_platypus.png?raw=true "Configuration used for bundling with Platypus")
- Script path pointing to `ebsp_platypus.sh` in the root directory.
- Script type is `sh`. 
- Interface type is `None`
- The app bundled with PyInstaller must be added to the Bundlded Files list.
- Make sure that `"Run in background"` is checked
- The identifier used should be:
    ```
    org.EBSPIndexerDevelopers.EBSPIndexer
    ``` 
- Author should be `EBSP Indexer Developers`
- Remember to update the version