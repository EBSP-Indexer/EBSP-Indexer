import sys
from kikuchipy import load
import matplotlib.pyplot as plt
import matplotlib as mpl
from os import path

def signalNavigation(file_path):
    mpl.use("qt5agg")
    try:
        s = load(file_path, lazy=True)
    except Exception as e:
        raise e
    s.plot()
    plt.show()

#signalNavigation(sys.argv[1])