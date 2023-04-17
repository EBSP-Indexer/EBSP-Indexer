import os
import platform
import sys

import PyInstaller.__main__

sys.setrecursionlimit(sys.getrecursionlimit() * 5) # Fix needed for some systems
workdir = os.getcwd()

target_arch = input(
    "Specify the target arcitecture [auto, x86_64, arm64, universal2]: "
    ).lower().strip()

# Different seperators between macOS and Windows
if platform.system().lower() == "darwin":
    sep = ":"
else:
    sep = ";"

args_list = [
    '--noconfirm',
    '--onedir',
    '--icon', os.path.join(workdir, "resources/ebsd_gui.ico"),
    '--name', "EBSD-GUI",
    '--add-data', os.path.join(workdir, f"resources{sep}resources/"),
    '--add-data', os.path.join(workdir, f"*G.txt{sep}."),   # Add COPYING.txt
    '--additional-hooks-dir', os.path.join(workdir,"hooks"),
    '--hidden-import', "kikuchipy",
    '--hidden-import', "hyperspy",
    '--hidden-import', "pyebsdindex",
]
# Checks target architecture for valid values
if target_arch in ['x86_64', 'arm64', 'universal2']:
    args_list.append("--target-arch") 
    args_list.append(target_arch) 

# Skips creating application on macOS as it currently do not work
if platform.system().lower() == "darwin":
    args_list.append("--console")
else:
    args_list.append("--windowed")

args_list.append('main.py')
PyInstaller.__main__.run(args_list) # Runs the command with arguments