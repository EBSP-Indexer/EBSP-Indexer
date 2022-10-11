from kikuchipy import load
import matplotlib.pyplot as plt

class SignalNavigation():

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        try:
            self.s = load(file_path, lazy=True)
        except Exception as e:
            raise e
        self.s.plot()
        plt.show()
        