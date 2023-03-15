import os
import PyInstaller.__main__
import platform
import sys

sys.setrecursionlimit(sys.getrecursionlimit() * 5)
workdir = os.getcwd()

if platform.system().lower() == "darwin":
    sep = ":"
else:
    sep = ";"

args_list = [
    '--noconfirm',
    '--onedir',
    #'--uac-admin',
    '--icon', os.path.join(workdir, "resources/ebsd_gui.ico"),
    '--name', "EBSD-GUI",
    '--add-data', os.path.join(workdir, f"resources{sep}resources/"),
    '--add-data', os.path.join(workdir, f"*G.txt{sep}."),
    '--additional-hooks-dir', os.path.join(workdir,"hooks"),
    '--hidden-import', "kikuchipy",
    '--hidden-import', "hyperspy",
    '--hidden-import', "pyebsdindex",
]

if platform.system().lower() == "darwin":
    args_list.append("--console")
    #args_list.append("--target-arch") 
    #args_list.append("x86_64") # Valid values are x86_64, arm64, and universal2.
else:
    args_list.append("--windowed")

args_list.append('main.py')
PyInstaller.__main__.run(args_list)