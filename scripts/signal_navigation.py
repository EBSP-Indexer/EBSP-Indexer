from kikuchipy import load
import matplotlib.pyplot as plt
import matplotlib as mpl
from os import path


class SignalNavigation:
    def __init__(self, file_path):
        mpl.use("qt5agg")
        print(mpl.get_backend())
        self.file_path = file_path
        try:
            self.s = load(self.file_path, lazy=True)
        except Exception as e:
            raise e
        self.s.plot()
        plt.show()
