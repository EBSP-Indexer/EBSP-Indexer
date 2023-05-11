import sys
import os

from .threads import sendToJobManager, sendToWorker, ThreadedOutput
from .redirect import Redirect
from .setting_file import SettingFile, get_setting_file_bottom_top
from .filebrowser import FileBrowser

def resource_path(relative_path):
    """
    Fix for issues related to relative paths, from https://stackoverflow.com/a/31966932

    Use this around relative paths to resources which are not 
    part of `resources.qrc`

    Parameters
    ----------
    relative_path : str
        The relative path to the resource

    Returns
    -------
    String
        The absolute path to the resource
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

__all__ = [
    "sendToJobManager",
    "sendToWorker",
    "ThreadedOutput",
    "Redirect",
    "SettingFile",
    "get_setting_file_bottom_top",
    "FileBrowser",
    "resource_path"
]