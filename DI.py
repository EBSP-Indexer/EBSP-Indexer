# Mappe med Pattern.dat. Må ligge i C:/EBSD data/Data set
sample = "Al 60x60"

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
dir_data = "C:\EBSD data\DI dataset"
dir_sample = os.path.join(dir_data, sample)
dir_nordif = dir_sample

#Create new directory for storing results

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


# ## Load data and inspect

file = os.path.join(dir_nordif, "Pattern.dat")
s = kp.load(
    file, lazy=False
)  # Set lazy=True if Pattern.dat is close to or greater than available memory
s

sem_md = s.metadata.Acquisition_instrument.SEM

energy = sem_md.beam_energy
# energy = 15  # kV

sample_tilt = sem_md.Detector.EBSD.sample_tilt
# sample_tilt = 70  # Degrees

# s.plot()


# ## Set up setting file


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
f_settings.write("Phases(s)", phase)
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


# ## Pre-pattern processing maps
#
# Maps of the data before doing any processing of pattern intensities.
#
# ### Mean intensity in each pattern

mean_intensity = s.mean(axis=(2, 3))
plt.imsave(
    os.path.join(dir_out, "mean_intensity.png"), mean_intensity.data, cmap="gray"
)


# ### Virtual backscatter electron (VBSE) imaging
#
# Also called virtual diode imaging, virtual forescatter electron (VFSE) imaging, and many other things.

vbse_gen = kp.generators.VirtualBSEGenerator(s)
vbse_gen


# #### RGB image

red = (2, 1)
green = (2, 2)
blue = (2, 3)
# p = vbse_gen.plot_grid(rgb_channels=[red, green, blue])
# p._plot.signal_plot.figure.savefig(os.path.join(dir_out, "vbse_rgb_grid.png"), **savefig_kwargs)

vbse_rgb_img = vbse_gen.get_rgb_image(r=red, g=green, b=blue)
vbse_rgb_img.change_dtype("uint8")
plt.imsave(os.path.join(dir_out, "vbse_rgb.png"), vbse_rgb_img.data)
# s.plot(navigator=vbse_rgb_img)


# #### One image per VBSE grid tile

vbse_gen.grid_shape = (3, 3)
# p = vbse_gen.plot_grid()
# p._plot.signal_plot.figure.savefig(os.path.join(dir_out, "vbse_grid2.png"), **savefig_kwargs)


vbse_imgs = vbse_gen.get_images_from_grid()
vbse_imgs.rescale_intensity(out_range=(0, 1), percentiles=(0.5, 99.5))
# vbse_imgs.plot()
# s.plot(navigator=vbse_imgs.inav[1, 2])

fig, ax = plt.subplots(nrows=3, ncols=3)
for idx in np.ndindex(vbse_imgs.axes_manager.navigation_shape[::-1]):
    img = vbse_imgs.data[idx]
    ax[idx].imshow(img, cmap="gray")
    ax[idx].axis("off")
#    plt.imsave(os.path.join(dir_out, f"vbse_img_y{idx[0]}_x{idx[1]}.png"), arr=img, cmap="gray")
fig.tight_layout(w_pad=0.5, h_pad=0.5)
fig.savefig(os.path.join(dir_out, "vbse_img.png"), **savefig_kwargs)

plt.close("all")


# ## Processing of pattern intensities
#
# Improve the signal-to-noise ratio. This means enhancing the Kikuchi pattern (signal)
# and removing the diffusly scattered backscatter electrons (noise).

s.remove_static_background()
f_settings.write("Static background corrected", True)

s.remove_dynamic_background()
f_settings.write("Dynamic background corrected", True)

# s.plot(navigator=vbse_rgb_img)

window = kp.filters.Window("gaussian", std=1)
# fig = window.plot(return_figure=True)
# fig.savefig(os.path.join(dir_out, "averaging_window.png"), **savefig_kwargs)


# s.average_neighbour_patterns(window)
# f_settings.write("Averaging with neighbour patterns", True)


# Write processed patterns to file

# s.save(os.path.join(dir_nordif, "Pattern_ave.dat"))  # NORDIF
# s.save(os.path.join(dir_out, "Pattern_ave.h5"))  # HDF5


# ## Pre-indexing maps

# Maps after enhancing the signal-to-noise ratio, but before dictionary indexing.


iq = s.get_image_quality()
plt.imsave(os.path.join(dir_out, "iq.png"), iq, cmap="gray")
# s.plot(navigator=hs.signals.Signal2D(iq))


# The average dot product map computation was implemented by Ole Natlandsmyr.


adp = s.get_average_neighbour_dot_product_map()
plt.imsave(os.path.join(dir_out, "adp.png"), adp, cmap="gray")
# s.plot(navigator=hs.signals.Signal2D(adp))


# ## Dictionary indexing
#
# Set up and perform dictionary indexing of patterns.

# ### Bin experimental patterns ("advanced" functionality)
# WARNING! Calling `s.rebin()` will increase the data type from 8 bit to float 64, meaning a memory increase of about 8. We rescale down to 8 bit to free up memory again.

nav_shape = s.axes_manager.navigation_shape
s2 = s.rebin(new_shape=nav_shape + new_signal_shape)
s2.rescale_intensity(dtype_out=np.uint8)


# ### Load simulated master pattern


file_mp = os.path.join(dir_sim, phase, f"{phase}_mc_mp_20kv.h5")
mp = kp.load(
    file_mp,
    energy=energy,  # single energies like 10, 11, 12 etc. or a range like (10, 20)
    projection="lambert",  # stereographic, lambert
    hemisphere="north",  # north, south, both
)
mp.phase


# mp.plot()


# ### Sample orientations


rot = sampling.get_sample_fundamental(
    method="cubochoric", resolution=disori, point_group=mp.phase.point_group
)
rot


# Alternative to using orientations sampled with orix is to import orientations
# sampled with EMsoft's `EMsampleRFZ` (Rodrigues Fundamental Zone) program. The
# sampling in orix is based on EMsoft's sampling, so the results should be
# identical, but you never know for sure...


# euler = np.load(os.path.join(dir_ori_samp, f"pg_{pg}_n100_eu.npz"))["arr_0"]
# rot = Rotation.from_euler(np.deg2rad(euler1))
# rot  # Displayed as quaternions (q0, q1, q2, q3)


# ### Define the detector-sample geometry

sig_shape = s2.axes_manager.signal_shape[
    ::-1
]  # HyperSpy: (column, row), NumPy: (row, column)
detector = kp.detectors.EBSDDetector(
    shape=sig_shape,
    sample_tilt=sample_tilt,  # Degrees
    pc=pc,
    convention="tsl",  # Default is Bruker
)
detector


# ### Create signal mask

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


# Simulate one pattern to check the parameters. The master pattern sampling was implemented by Lars Lervik.


# sim1 = mp.get_patterns(
#    rotations=Rotation.from_euler(np.deg2rad([0, 0, 0])),
##    rotations=rot[0],
#    detector=detector,
#    energy=energy,  # Defined above
#    compute=True,  # if False, sim.compute() must be called at a later time
# )

# fig, _ = detector.plot(
#    pattern=sim1.squeeze().data,
#    draw_gnomonic_circles=True,
#    coordinates="gnomonic",
#    return_fig_ax=True
# )
# fig.savefig(os.path.join(dir_out, "pc.png"), **savefig_kwargs)

# sim1


# ### Generate dictionary
#
# The master pattern sampling was implemented by Lars Lervik.

sim_dict = mp.get_patterns(
    rotations=rot,
    detector=detector,
    energy=energy,
    compute=False,
)
sim_dict

fname_dict = f"simulated_dictionary_{phase}_{detector.ncols}x{detector.nrows}_{int(energy)}kV_{int(sample_tilt)}deg_pcx{pc[0]}_pcy{pc[1]}_pcz{pc[2]}"


# Remove "#" before the following lines to save the dictionary of simulated patterns to file


# sim_dict.save(os.path.join(dir_sim, phase, fname_dict + ".h5"))
# io.save(os.path.join(dir_sim, phase, fname_dict + "_xmap.h5"), sim_dict.xmap)


# Remove "#" before the following lines to load the saved dictionary of simualted patterns into memory

# sim_dict = kp.load(os.path.join(dir_sim, phase, fname_dict + ".h5"))
# sim_dict._xmap = io.load(os.path.join(dir_sim, phase, fname_dict + "_xmap.h5"))


# ### Perform dictionary indexing
#
# Dictionary indexing is implemented by Ole Natlandsmyr.


di_kwargs = dict(metric="ncc", keep_n=20, n_per_iteration=n_per_iteration)
if use_signal_mask:
    di_kwargs["signal_mask"] = signal_mask
t1 = time()
xmap = s2.dictionary_indexing(dictionary=sim_dict, **di_kwargs)
t2 = time()
xmap.scan_unit = "um"
xmap

io.save(os.path.join(dir_out, "di_results.h5"), xmap)  # orix' HDF5
io.save(os.path.join(dir_out, "di_results.ang"), xmap)  # .ang


# ## Inspect dictionary indexing results
#
# Plot and save the normalized cross correlation score $r$


fig = xmap.plot(
    value=xmap.scores[:, 0],
    colorbar=True,
    colorbar_label="Normalized cross correlation score",
    return_figure=True,
    cmap="gray",
)
fig.savefig(os.path.join(dir_out, "ncc.png"), **savefig_kwargs)


# Calculate, plot and save the orientation similarity map, which shows how similar the best matching simulated patterns in each map point are to their neighbours

osm = kp.indexing.orientation_similarity_map(xmap)


fig = xmap.plot(
    value=osm.ravel(),
    colorbar=True,
    colorbar_label="Orientation similarity",
    return_figure=True,
    cmap="gray",
)
fig.savefig(os.path.join(dir_out, "osm.png"), **savefig_kwargs)


# ## Refine orientations (not projection centers)

if refine == 1:
    fname_ref = "ori"
elif refine == 2:
    fname_ref = "pc"
elif refine == 3:
    fname_ref = "ori_pcs"

# Perform refinement
refine_kwargs = dict(
    xmap=xmap,
    detector=detector,
    master_pattern=mp,
    energy=energy,
    compute=True,
)
if refine == 1:
    xmap_refined = s2.refine_orientation(**refine_kwargs)
elif refine == 2:
    ncc_after_refinement, detector_refined = s2.refine_projection_center(
        **refine_kwargs
    )
elif refine == 3:
    xmap_refined, detector_refined = s2.refine_orientation_projection_center(
        **refine_kwargs
    )

# Save orientation maps
if refine in [1, 3]:
    io.save(
        os.path.join(dir_out, f"di_ref_{fname_ref}_results.h5"), xmap_refined
    )  # orix' HDF5
    io.save(
        os.path.join(dir_out, f"di_ref_{fname_ref}_results.ang"), xmap_refined
    )  # .ang


# Get NCC map min/max
if refine != 0:
    ncc_map = xmap.get_map_data(xmap.scores[:, 0])
    if refine != 2:
        ncc_after_refinement = xmap_refined.get_map_data("scores")

    ncc_di_min = np.min(ncc_map)
    ncc_di_max = np.max(ncc_map)
    ncc_ref_min = np.min(ncc_after_refinement)
    ncc_ref_max = np.max(ncc_after_refinement)

    vmin = min([ncc_di_min, ncc_ref_min])
    vmax = max([ncc_di_max, ncc_ref_max])


# NCC maps
if refine != 0:
    fig, ax = plt.subplots(ncols=2, figsize=(9, 3))
    im0 = ax[0].imshow(ncc_map, vmin=vmin, vmax=vmax)
    ax[0].axis("off")
    fig.colorbar(im0, ax=ax[0], label="NCC from DI")
    im1 = ax[1].imshow(ncc_after_refinement, vmin=vmin, vmax=vmax)
    ax[1].axis("off")
    ncc_after_label = f"NCC after {fname_ref} ref."
    fig.colorbar(im1, ax=ax[1], label=ncc_after_label)
    fig.tight_layout()
    fig.savefig(
        os.path.join(dir_out, f"ncc_scores_di_ref_{fname_ref}.png"), **savefig_kwargs
    )


# NCC histograms
if refine != 0:
    bins = np.linspace(vmin, vmax, 100)
    fig, ax = plt.subplots(figsize=(9, 5))
    _ = ax.hist(ncc_map.ravel(), bins, alpha=0.5, label="NCC from DI")
    _ = ax.hist(
        ncc_after_refinement.ravel(),
        bins,
        alpha=0.5,
        label=ncc_after_label,
    )
    ax.set_xlabel("Normalized cross correlation (NCC) scores")
    ax.set_ylabel("Frequency")
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        os.path.join(dir_out, f"ncc_scores_di_ref_{fname_ref}_histogram.png"),
        **savefig_kwargs,
    )


# Plot PC
if refine in [2, 3]:
    fig, ax = plt.subplots(ncols=3, figsize=(15, 3))
    im0 = ax[0].imshow(detector_refined.pcx)
    fig.colorbar(im0, ax=ax[0], label="Projection center x")
    ax[0].axis("off")
    im1 = ax[1].imshow(detector_refined.pcy)
    fig.colorbar(im1, ax=ax[1], label="Projection center y")
    ax[1].axis("off")
    im2 = ax[2].imshow(detector_refined.pcz)
    fig.colorbar(im2, ax=ax[2], label="Projection center z")
    ax[2].axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(dir_out, f"pc_ref_{fname_ref}.png"), **savefig_kwargs)


# Save PC values to file
if refine in [2, 3]:
    nav_size = np.prod(detector_refined.navigation_shape)
    pc = detector_refined.pc_tsl().reshape((nav_size, 3))
    idx_map_center = pc.shape[0] // 2
    pc_map_center = pc[idx_map_center]
    np.savetxt(
        os.path.join(dir_out, f"pc_values_ref_{fname_ref}.txt"),
        pc,
        fmt="%.6f",
        header="PC map center: {:.6f} {:.6f} {:.6f}".format(*pc_map_center),
    )
    print(f"PC in map center: {pc_map_center}")

plt.close("all")

t3 = time()

n_experimental_patterns = s.axes_manager.navigation_size
time_total = t3 - t0
time_di = t2 - t1

f_settings.write(
    "Indexed patterns per second (n / total processing)",
    n_experimental_patterns / time_total,
)
f_settings.write(
    "Indexed patterns per second (n / dictionary indexing)",
    n_experimental_patterns / time_di,
)
f_settings.write("Time (total processing)", f"{time_total} s")
f_settings.write("Time (dictionary indexing)", f"{time_di} s")

f_settings.close()
