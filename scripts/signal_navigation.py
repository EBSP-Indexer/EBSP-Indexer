from msilib.schema import Error
from os import path
import kikuchipy as kp
import matplotlib.pyplot as plt

class SignalNavigation():

    def __init__(self, working_dir):
        super().__init__()
        self.working_dir = working_dir
        try:
            self.s = kp.load(path.join(working_dir, "Pattern_avg.h5"), lazy=True)
        except Exception as e:
            raise e

        self.s.plot()
        plt.show()
        