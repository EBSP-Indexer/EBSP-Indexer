import sys
import os

from utils.threads.worker_widget import sendToJobManager
from utils.threads.worker import sendToWorker
from utils.threads.thdout import ThreadedOutput
from utils.redirect import Redirect
from utils.setting_file import SettingFile, get_setting_file_bottom_top
from utils.filebrowser import FileBrowser

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)