### Dictionary indexing with the possibility to look at recordings containing one or more phases

import hyperspy.api as hs
import kikuchipy as kp
import matplotlib.pyplot as plt
import numpy as np
from orix.quaternion import Rotation
from orix import io, sampling
import os
from time import time
import warnings

import gc

# ENDRE KUN DISSE PARAMETRENE:

# Mappe med Pattern.dat. Må ligge i C:/EBSD data/DI data
sample = "SDSS_070321_SR_kopi"

# Pattern Center og prøvetilt for prøve-detektor-modell
pc = (0.511, 0.750, 0.455)

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
# Faser og energi for master pattern, legg til de forventede fasene i lista

phases = ["austenite", "ferrite", "ni"]

# Binning
new_signal_shape = (60, 60)

# Gjennomsnittlig disorientering (minste misorientering) i katalogen
disori = 2  # Degrees

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
refine = 1


# Paths to EBSD simulations and orientation sampling (don't change)
dir_top = "C:\EBSD data\kikuchipy"
dir_sim = os.path.join(dir_top, "ebsd_simulations")
dir_ori_samp = os.path.join(dir_top, "orientation_sampling")

# Paths to data (change)
dir_data = "C:\EBSD data\DI data"
dir_sample = os.path.join(dir_data, sample)
dir_nordif = dir_sample

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


### Load data and inspect

file = os.path.join(dir_nordif, "Pattern.dat")
s = kp.load(
    file, lazy=False
)  # Set lazy=True if Pattern.dat is close to or greater than available memory
s

### Hent metadata fra Pattern.dat

sem_md = s.metadata.Acquisition_instrument.SEM


energy = sem_md.beam_energy
sample_tilt = sem_md.Detector.EBSD.sample_tilt

# s.plot()

# Set up settings file
settings_fname = os.path.join(dir_out, "SettingKP.txt")
f_settings = SettingFile(settings_fname)

# SEM parameters
f_settings.write("Microscope", sem_md.microscope)
f_settings.write("Acceleration voltage", f"{energy} kV")
f_settings.write("Sample tilt", f"{sample_tilt} degrees")
f_settings.write("Working distance", sem_md.working_distance)
f_settings.write("Magnification", sem_md.magnification)
f_settings.write(
    "Navigation shape (rows, columns)", s.axes_manager.navigation_shape[::-1]
)
f_settings.write("Signal shape (rows, columns)", s.axes_manager.signal_shape[::-1])
f_settings.write("Step size", f"{s.axes_manager[0].scale} um\n")

# DI parameters
f_settings.write("kikuchipy version", kp.__version__)
f_settings.write("PC (x*, y*, z*)", pc)
f_settings.write("Phases(s)", phases)
f_settings.write("Pattern resolution DI", new_signal_shape)
f_settings.write("Delta orientation", f"{disori} degrees")
f_settings.write("Circular mask", use_signal_mask)
f_settings.write(
    "Number of experimental patterns matched per iteration [None - all]",
    n_per_iteration,
)
f_settings.write(
    "Refinement [0 - None, 1 - Orientations, 2 - PC, 3 - Orientations and PC]", refine
)


### Pre-pattern processing maps

# Maps of the data before doing any processing of pattern intensities.

### Mean intensity in each pattern

mean_intensity = s.mean(axis=(2, 3))
plt.imsave(
    os.path.join(dir_out, "mean_intensity.png"), mean_intensity.data, cmap="gray"
)

### Virtual backscatter electron (VBSE) imaging
# Also called virtual diode imaging, virtual forescatter electron (VFSE) imaging, and many other things.

vbse_gen = kp.generators.VirtualBSEGenerator(s)
vbse_gen

### RGB image

red = (2, 1)
green = (2, 2)
blue = (2, 3)
p = vbse_gen.plot_grid(rgb_channels=[red, green, blue])
p._plot.signal_plot.figure.savefig(
    os.path.join(dir_out, "vbse_rgb_grid.png"), **savefig_kwargs
)


vbse_rgb_img = vbse_gen.get_rgb_image(r=red, g=green, b=blue)
vbse_rgb_img.change_dtype("uint8")
plt.imsave(os.path.join(dir_out, "vbse_rgb.png"), vbse_rgb_img.data)
s.plot(navigator=vbse_rgb_img)


### One image per VBSE grid tile

vbse_gen.grid_shape = (3, 3)
p = vbse_gen.plot_grid()
p._plot.signal_plot.figure.savefig(
    os.path.join(dir_out, "vbse_grid2.png"), **savefig_kwargs
)

vbse_imgs = vbse_gen.get_images_from_grid()
vbse_imgs.rescale_intensity(out_range=(0, 1), percentiles=(0.5, 99.5))
vbse_imgs.plot()
s.plot(navigator=vbse_imgs.inav[1, 2])

fig, ax = plt.subplots(nrows=3, ncols=3)
for idx in np.ndindex(vbse_imgs.axes_manager.navigation_shape[::-1]):
    img = vbse_imgs.data[idx]
    ax[idx].imshow(img, cmap="gray")
    ax[idx].axis("off")
    plt.imsave(
        os.path.join(dir_out, f"vbse_img_y{idx[0]}_x{idx[1]}.png"), arr=img, cmap="gray"
    )
fig.tight_layout(w_pad=0.5, h_pad=0.5)
fig.savefig(os.path.join(dir_out, "vbse_img.png"), **savefig_kwargs)

plt.close("all")


### Processing of pattern intensities
#       Improve the signal-to-noise ratio. This means enhancing the Kikuchi pattern (signal)
#       and removing the diffusly scattered backscatter electrons (noise).

s.remove_static_background()
f_settings.write("Static background corrected", True)

s.remove_dynamic_background()
f_settings.write("Dynamic background corrected", True)

s.plot(navigator=vbse_rgb_img)

window = kp.filters.Window("gaussian", std=1)
fig = window.plot(return_figure=True)
fig.savefig(os.path.join(dir_out, "averaging_window.png"), **savefig_kwargs)

s.average_neighbour_patterns(window)
f_settings.write("Averaging with neighbour patterns", True)


### Write processed patterns to file

# s.save(os.path.join(dir_nordif, "Pattern_ave.dat"))  # NORDIF
# s.save(os.path.join(dir_out, "Pattern_ave.h5"))  # HDF5


### Pre-indexing maps

# Maps after enhancing the signal-to-noise ratio, but before dictionary indexing.

iq = s.get_image_quality()
plt.imsave(os.path.join(dir_out, "iq.png"), iq, cmap="gray")
s.plot(navigator=hs.signals.Signal2D(iq))

# The average dot product map computation was implemented by Ole Natlandsmyr.

adp = s.get_average_neighbour_dot_product_map()
plt.imsave(os.path.join(dir_out, "adp.png"), adp, cmap="gray")
s.plot(navigator=hs.signals.Signal2D(adp))


### Dictionary indexing
#       Set up and perform dictionary indexing of patterns.
#       Bin experimental patterns ("advanced" functionality)

# WARNING! Calling `s.rebin()` will increase the data type from 8 bit to float 64, meaning a memory increase of about 8. We rescale down to 8 bit to free up memory again.

nav_shape = s.axes_manager.navigation_shape
s2 = s.rebin(new_shape=nav_shape + new_signal_shape)
s2.rescale_intensity(dtype_out=np.uint8)

plt.close("all")


### Set up and perform dictionary indexing of patterns.

### Define the detector-sample geometry

sig_shape = s2.axes_manager.signal_shape[
    ::-1
]  # HyperSpy: (column, row), NumPy: (row, column)
detector = kp.detectors.EBSDDetector(
    shape=sig_shape,
    sample_tilt=sample_tilt,  # Degrees
    pc=pc,
    convention="tsl",  # Default is Bruker
)

print(detector)

ref_kw = dict(detector=detector, energy=energy, compute=True)

### Create signal mask

if use_signal_mask:
    signal_mask = ~kp.filters.Window("circular", sig_shape).astype(bool)

    p = s2.inav[0, 0].data
    fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
    ax[0].imshow(p * signal_mask, cmap="gray")
    ax[0].set_title("Not used in matching")
    ax[1].imshow(p * ~signal_mask, cmap="gray")
    ax[1].set_title("Used in matching")
    fig.savefig(os.path.join(dir_out, "circular_mask_for_di.png"), **savefig_kwargs)

plt.close("all")


### Set up dictionary indexing parameters

di_kwargs = dict(metric="ncc", keep_n=20, n_per_iteration=n_per_iteration)
if use_signal_mask:
    di_kwargs["signal_mask"] = signal_mask

t1 = time()


# Master pattern dictionary
mp = {}

# Xmaps dictionary
xmaps = {}

# Refined xmaps dictionary

xmaps_ref = {}


for ph in phases:

    ### Load simulated master pattern

    file_mp = os.path.join(dir_sim, ph, f"{ph}_mc_mp_20kv.h5")
    mp[f"mp_{ph}"] = kp.load(
        file_mp,
        energy=energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
        projection="lambert",  # stereographic, lambert
        hemisphere="both",  # north, south, both
    )

    mp[f"mp_{ph}"].phase

    ### Sample orientations

    rot = sampling.get_sample_fundamental(
        method="cubochoric",
        resolution=disori,
        point_group=mp[f"mp_{ph}"].phase.point_group,
    )

    rot

    ### Simulate one pattern to check the parameters. The master pattern sampling was implemented by Lars Lervik.

    sim = mp[f"mp_{ph}"].get_patterns(
        rotations=Rotation.from_euler(np.deg2rad([0, 0, 0])),
        # rotations=rot[0],
        detector=detector,
        energy=energy,  # Defined above
        compute=True,  # if False, sim.compute() must be called at a later time
    )

    fig, _ = detector.plot(
        pattern=sim.squeeze().data,
        draw_gnomonic_circles=True,
        coordinates="gnomonic",
        return_fig_ax=True,
    )

    fig.savefig(os.path.join(dir_out, f"pc_{ph}.png"), **savefig_kwargs)

    ### Generate dictionary

    sim_dict = mp[f"mp_{ph}"].get_patterns(
        rotations=rot,
        detector=detector,
        energy=energy,
        compute=False,
    )

    sim_dict

    fname_dict = f"simulated_dictionary_{ph}_{detector.ncols}x{detector.nrows}_{int(energy)}kV_{int(sample_tilt)}deg_pcx{pc[0]}_pcy{pc[1]}_pcz{pc[2]}"

    ### Perform dictionary indexing

    xmaps[f"xmap_{ph}"] = s2.dictionary_indexing(dictionary=sim_dict, **di_kwargs)

    # Record of time after DI
    t2 = time()

    xmaps[f"xmap_{ph}"].scan_unit = "um"

    xmaps[f"xmap_{ph}"]

    ### Save results from DI for phase

    io.save(
        os.path.join(dir_out, f"di_results_{ph}.h5"), xmaps[f"xmap_{ph}"]
    )  # orix' HDF5
    io.save(os.path.join(dir_out, f"di_results_{ph}.ang"), xmaps[f"xmap_{ph}"])  # .ang

    ### Inspect dictionary indexing results for phase

    fig = xmaps[f"xmap_{ph}"].plot(
        value=xmaps[f"xmap_{ph}"].scores[:, 0],
        colorbar=True,
        colorbar_label="Normalized cross correlation score",
        return_figure=True,
        cmap="gray",
    )

    fig.savefig(os.path.join(dir_out, f"ncc_{ph}.png"), **savefig_kwargs)

    ### Calculate and save orientation similairty map

    osm = kp.indexing.orientation_similarity_map(xmaps[f"xmap_{ph}"])

    fig = xmaps[f"xmap_{ph}"].plot(
        value=osm.ravel(),
        colorbar=True,
        colorbar_label="Orientation similarity",
        return_figure=True,
        cmap="gray",
    )

    fig.savefig(os.path.join(dir_out, f"osm_{ph}.png"), **savefig_kwargs)
    if refine == 1:

        ### Refine xmaps

        xmaps_ref[f"xmap_ref_{ph}"] = s2.refine_orientation(
            xmap=xmaps[f"xmap_{ph}"],
            master_pattern=mp[f"mp_{ph}"],
            trust_region=[1, 1, 1],
            **ref_kw,
        )

        io.save(
            os.path.join(dir_out, f"di_ref_results_{ph}.ang"),
            xmaps_ref[f"xmap_ref_{ph}"],
        )  # .ang

    plt.close()
    del sim_dict
    gc.collect()


### Merge xmaps if there are more phases

if len(phases) > 1:

    cm = []
    for ph in phases:
        cm.append(xmaps[f"xmap_{ph}"])

    ### Merge xmaps from indexed phases

    xmap_merged = kp.indexing.merge_crystal_maps(
        crystal_maps=cm,
         mean_n_best=1,
         scores_prop="scores",
        # simulation_indices_prop="simulation_indices",
    )

    xmap_merged

    ### Change colors of phases

    colors = ["lime", "r", "b", "yellow"]

    for i in range(len(phases)):
        xmap_merged.phases[i].color = colors[i]

    xmap_merged

    ### Save merged xmaps to file

    io.save(os.path.join(dir_out, "di_results_merged.h5"), xmap_merged)  # orix' HDF5
    io.save(os.path.join(dir_out, "di_results_merged.ang"), xmap_merged)  # .ang

    ### Plot and save the normalized cross correlation score

    fig = xmap_merged.plot(
        value=xmap_merged.scores[:, 0],
        colorbar=True,
        colorbar_label="Normalized cross correlation score",
        return_figure=True,
        cmap="gray",
    )

    fig.savefig(os.path.join(dir_out, "ncc_merged.png"), **savefig_kwargs)

    ### Calculate, plot and save the orientation similarity map

    osm_merged = kp.indexing.orientation_similarity_map(xmap_merged)

    fig = xmap_merged.plot(
        value=osm_merged.ravel(),
        colorbar=True,
        colorbar_label="Orientation similarity",
        return_figure=True,
        cmap="gray",
    )

    fig.savefig(os.path.join(dir_out, "osm_merged.png"), **savefig_kwargs)

    ### Phase map

    fig = xmap_merged.plot(remove_padding=True, return_figure=True)
    fig.savefig(os.path.join(dir_out, "phase_map.png"), **savefig_kwargs)

    if refine == 1:

        cm_ref = []
        for ph in phases:
            cm_ref.append(xmaps_ref[f"xmap_ref_{ph}"])

        ### Merge xmaps from indexed phases

        xmap_merged_ref = kp.indexing.merge_crystal_maps(
            crystal_maps=cm_ref,
            # mean_n_best=1,
            # scores_prop="scores",
            # simulation_indices_prop="simulation_indices",
        )

        xmap_merged_ref

        ### Change colors of phases

        colors = ["lime", "r", "b", "yellow"]

        for i in range(len(phases)):
            xmap_merged_ref.phases[i].color = colors[i]

        xmap_merged_ref

        ### Save merged xmaps to file

        io.save(
            os.path.join(dir_out, "di_results_ref_merged.h5"), xmap_merged_ref
        )  # orix' HDF5
        io.save(
            os.path.join(dir_out, "di_results_ref_merged.ang"), xmap_merged_ref
        )  # .ang

        ### Plot and save the normalized cross correlation score

        fig = xmap_merged_ref.plot(
            value=xmap_merged_ref.scores[:, 0],
            colorbar=True,
            colorbar_label="Normalized cross correlation score after refinement",
            return_figure=True,
            cmap="gray",
        )

        fig.savefig(os.path.join(dir_out, "ncc_merged_ref.png"), **savefig_kwargs)

        ### Calculate, plot and save the orientation similarity map

        osm_merged_ref = kp.indexing.orientation_similarity_map(xmap_merged_ref)

        fig = xmap_merged_ref.plot(
            value=osm_merged_ref.ravel(),
            colorbar=True,
            colorbar_label="Orientation similarity after refinement",
            return_figure=True,
            cmap="gray",
        )

        fig.savefig(os.path.join(dir_out, "osm_merged_ref.png"), **savefig_kwargs)

        ### Phase map

        fig = xmap_merged_ref.plot(remove_padding=True, return_figure=True)
        fig.savefig(os.path.join(dir_out, "phase_map_ref.png"), **savefig_kwargs)
