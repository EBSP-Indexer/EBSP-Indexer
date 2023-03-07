import os
import PyInstaller.__main__

workdir = os.getcwd()

PyInstaller.__main__.run([
    '--noconfirm',
    '--windowed',
    '--onedir',
    '--uac-admin',
    '--icon', os.path.join(workdir, "resources/ebsd_gui.ico"),
    '--name', "EBSD-GUI",
    '--add-data', os.path.join(workdir, "resources;resources/"),
    '--additional-hooks-dir', os.path.join(workdir,"hooks"),
    '--hidden-import', "kikuchipy",
    '--hidden-import', "hyperspy",
    '--hidden-import', "pyebsdindex",
    'main.py',
])