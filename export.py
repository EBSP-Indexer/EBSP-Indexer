# Copyright (c) 2022 EBSP Indexer developers
#
# This file is part of EBSP Indexer.

# EBSP Indexer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# EBSP Indexer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

import os
import platform
import sys

import PyInstaller.__main__

sys.setrecursionlimit(sys.getrecursionlimit() * 5) # Fix needed for some systems
workdir = os.getcwd()

target_arch = input(
    "Specify the target architecture [auto, x86_64, arm64, universal2]: "
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
    '--name', "EBSP Indexer",
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

args_list.append('main.py')
PyInstaller.__main__.run(args_list) # Runs the command with arguments