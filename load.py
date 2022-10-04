# Mappe med Pattern.dat. Må ligge i C:/EBSD data/Data set
sample = "C:\EBSD data\DI data\Al 60x60"

# Pattern Center og prøvetilt for prøve-detektor-modell
pc = (0.489, 0.800, 0.497)

# Punktgruppeidentifikatorer. LA STÅ!
pg_dict = {
    "al": "m-3m",
    "austenite": "m-3m",
    "ferrite": "m-3m",
    "ni": "m-3m",
    "si": "m-3m",
    "ti_alpha": "6_mmm",  # 6/mmm
    "ti_beta": "m-3m",
}

# Fase og energi for master pattern
phase = "al"  # al, austenite, ferrite, ni, si, ti_alpha, ti_beta
pg = pg_dict[phase]

# Binning
new_signal_shape = (60, 60)

# Gjennomsnittlig disorientering (minste misorientering) i katalogen
disori = 1.8  # Degrees

# Sirkulær maske kan anvendes under indisering (ikke refinement enda)
use_signal_mask = False  # True or False

# Antall mønstre å matche under hver iterasjon av DI (tidligere n_slices).
# Tryggest å ikke sette denne (None). Høyere antall bruker generelt mer minne,
# men kan øke hastigheten.
n_per_iteration = None

# Refinement?
# 0 - Ingen
# 1 - Orientation
# 2 - Projection center
# 3 - Orientation and projection center
refine = 0


import hyperspy.api as hs
import kikuchipy as kp
import matplotlib.pyplot as plt
import numpy as np
from orix.quaternion import Rotation
from orix import io, sampling
import os
from time import time
import warnings


# Paths to EBSD simulations and orientation sampling (don't change)
dir_top = "C:\EBSD data\kikuchipy"
dir_sim = os.path.join(dir_top, "ebsd_simulations")
dir_ori_samp = os.path.join(dir_top, "orientation_sampling")

# Paths to data (change)
dir_data = "C:\EBSD data\DI data"
dir_sample = os.path.join(dir_data, sample)
dir_nordif = dir_sample

#Create new directory for storing results
"""
for i in range(1, 100):
    try:
        dir_out = os.path.join(dir_sample, "di_results" + str(i))
        os.mkdir(dir_out)
        break
    except FileExistsError:
        print(
            f"Directory '{dir_out}' exists, will try to create directory '{dir_out[:-1] + str(i + 1)}'"
        )
savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)
"""
t0 = time()

class SettingFile:
    def __init__(self, file_path):
        self.file = open(file_path, mode="w")

    def write(self, key, value):
        try:
            self.file.write(f"{key}: {value}\n")
        except:
            warnings.warn(f"Could not write '{key}: {value}' to settings file.")

    def close(self):
        self.file.close()


kp.__version__


# ## Load data and inspect

file = os.path.join(dir_nordif, "Pattern.dat")
s = kp.load(
    file, lazy=False
)  # Set lazy=True if Pattern.dat is close to or greater than available memory

sem_md = s.metadata.Acquisition_instrument.SEM

energy = sem_md.beam_energy
# energy = 15  # kV

sample_tilt = sem_md.Detector.EBSD.sample_tilt
# sample_tilt = 70  # Degrees

# s.plot()