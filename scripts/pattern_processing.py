import os
import kikuchipy as kp
from PyQt6 import uic

uiForm, baseClass = uic.loadUiType("")

class background_processor(baseClass):
    def __init__(self, working_dir, save_path = "Pattern_avg.h5"):
        self.working_dir = working_dir
        self.save_path = save_path
        self.s = kp.load(os.path.join(working_dir, "Pattern.dat"), lazy=True)
        self.ui = uiForm
        self.ui.setupUi(self)
        self.show()

    def remove_static(self):
        self.s.remove_static_background()

    def remove_dynamic(self):
        self.s.remove_dynamic_background()

    def averaging(self):
        window = kp.filters.Window("gaussian", std=1)
        self.s.average_neighbour_patterns(window)

    def save_to_file(self, *save_path):
        if (save_path):
            self.save_path = save_path
        self.s.save(self.save_path)
