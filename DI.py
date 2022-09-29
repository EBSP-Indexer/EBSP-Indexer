import hyperspy.api as hs
import kikuchipy as kp
import matplotlib.pyplot as plt
import numpy as np
from orix.quaternion import Rotation
from orix import io, sampling
import os
from time import time
import warnings

# Mappe med Pattern.dat. Må ligge i C:/EBSD data/Data set
sample = "C:/EBSD data/DI data/Al 60x60"

# Pattern Center og prøvetilt for prøve-detektor-modell
pc = (0.489, 0.800, 0.497)

# Punktgruppeidentifikatorer. LA STÅ!
pg_dict = {
    "al":        "m-3m",
    "austenite": "m-3m",
    "ferrite":   "m-3m",
    "ni":        "m-3m",
    "si":        "m-3m",
    "ti_alpha":  "6_mmm",  # 6/mmm
    "ti_beta":   "m-3m",
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

# Paths to EBSD simulations and orientation sampling (don't change)
dir_top = "C:/EBSD data/kikuchipy"
dir_sim = os.path.join(dir_top, "ebsd_simulations")
dir_ori_samp = os.path.join(dir_top, "orientation_sampling")

# Paths to data (change)
dir_data = "C:/EBSD data/DI dataset"
dir_sample = os.path.join(dir_data, sample)
dir_nordif = dir_sample

for i in range(1, 100):
    try:
        dir_out = os.path.join(dir_sample, "di_results" + str(i))
        os.mkdir(dir_out)
        break
    except FileExistsError:
        print(f"Directory '{dir_out}' exists, will try to create directory '{dir_out[:-1] + str(i + 1)}'")
savefig_kwargs = dict(bbox_inches="tight", pad_inches=0, dpi=150)

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

file = os.path.join(dir_nordif, "Pattern.dat")
s = kp.load(file, lazy=False)  # Set lazy=True if Pattern.dat is close to or greater than available memory
#s

sem_md = s.metadata.Acquisition_instrument.SEM

energy = sem_md.beam_energy
#energy = 15  # kV

sample_tilt = sem_md.Detector.EBSD.sample_tilt
#sample_tilt = 70  # Degrees

# Set up settings file
settings_fname = os.path.join(dir_out, "SettingKP.txt")
f_settings = SettingFile(settings_fname)

# SEM parameters
f_settings.write("Microscope", sem_md.microscope)
f_settings.write("Acceleration voltage", f"{energy} kV")
f_settings.write("Sample tilt", f"{sample_tilt} degrees")
f_settings.write("Working distance", sem_md.working_distance)
f_settings.write("Magnification", sem_md.magnification)
f_settings.write("Navigation shape (rows, columns)", s.axes_manager.navigation_shape[::-1])
f_settings.write("Signal shape (rows, columns)", s.axes_manager.signal_shape[::-1])
f_settings.write("Step size", f"{s.axes_manager[0].scale} um\n")

# DI parameters
f_settings.write("kikuchipy version", kp.__version__)
f_settings.write("PC (x*, y*, z*)", pc)
f_settings.write("Phases(s)", phase)
f_settings.write("Pattern resolution DI", new_signal_shape)
f_settings.write("Delta orientation", f"{disori} degrees")
f_settings.write("Circular mask", use_signal_mask)
f_settings.write("Number of experimental patterns matched per iteration [None - all]", n_per_iteration)
f_settings.write("Refinement [0 - None, 1 - Orientations, 2 - PC, 3 - Orientations and PC]", refine)

mean_intensity = s.mean(axis=(2, 3))
plt.imsave(os.path.join(dir_out, "mean_intensity.png"), mean_intensity.data, cmap="gray")

vbse_gen = kp.generators.VirtualBSEGenerator(s)
#vbse_gen

red = (2, 1)
green = (2, 2)
blue = (2, 3)
#p = vbse_gen.plot_grid(rgb_channels=[red, green, blue])
#p._plot.signal_plot.figure.savefig(os.path.join(dir_out, "vbse_rgb_grid.png"), **savefig_kwargs)

vbse_rgb_img = vbse_gen.get_rgb_image(r=red, g=green, b=blue)
vbse_rgb_img.change_dtype("uint8")
plt.imsave(os.path.join(dir_out, "vbse_rgb.png"), vbse_rgb_img.data)
#s.plot(navigator=vbse_rgb_img)

vbse_imgs = vbse_gen.get_images_from_grid()
vbse_imgs.rescale_intensity(out_range=(0, 1), percentiles=(0.5, 99.5))
#vbse_imgs.plot()
#s.plot(navigator=vbse_imgs.inav[1, 2])

fig, ax = plt.subplots(nrows=3, ncols=3)
for idx in np.ndindex(vbse_imgs.axes_manager.navigation_shape[::-1]):
    print(idx)
    img = vbse_imgs.data[idx]
    ax[idx].imshow(img, cmap="gray")
    ax[idx].axis("off")
#    plt.imsave(os.path.join(dir_out, f"vbse_img_y{idx[0]}_x{idx[1]}.png"), arr=img, cmap="gray")
fig.tight_layout(w_pad=0.5, h_pad=0.5)
fig.savefig(os.path.join(dir_out, "vbse_img.png"), **savefig_kwargs)

plt.close("all")