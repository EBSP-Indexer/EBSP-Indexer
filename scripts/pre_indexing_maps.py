import gc
from os import mkdir, path

import kikuchipy as kp
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from mpl_toolkits.axes_grid1 import make_axes_locatable

save_fig_kwargs = dict(bbox_inches="tight", pad_inches=0)

def generate_figure(image, pattern, col_label, pattern_path, image_type):
    scale = pattern.axes_manager["x"].scale
    fig, ax = plt.subplots()
    ax.axis("off")
    plot = ax.imshow(image, cmap="gray")
    if col_label != "VBSE":
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(plot, cax=cax, label=col_label)
    scalebar = ScaleBar(
        scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4
    )
    ax.add_artist(scalebar)
    basename, extension = path.basename(pattern_path).split(".")
    working_dir = path.dirname(pattern_path)
    image_dir = path.join(working_dir, f"{basename}_images")
    try:
        mkdir(image_dir)
    except FileExistsError:
        pass

    plt.savefig(
        path.join(image_dir, f"{image_type}.png"),
        **save_fig_kwargs,
    )
    plt.close(fig)


def save_iq_map(pattern_path):
    s_iq = kp.load(pattern_path, lazy=True)
    iq_map = s_iq.get_image_quality()
    generate_figure(iq_map, s_iq, "IQ", pattern_path, "image_quality_map")

    del s_iq
    gc.collect()


def save_adp_map(pattern_path):
    s_adp = kp.load(pattern_path, lazy=True)
    adp_map = s_adp.get_average_neighbour_dot_product_map()
    generate_figure(adp_map, s_adp, "ADP", pattern_path, "average_dot_product_map")

    del s_adp
    gc.collect()


def save_mean_intensity_map(pattern_path):
    s_mi = kp.load(pattern_path, lazy=True)
    mim_map = s_mi.mean(axis=(2, 3))
    generate_figure(mim_map, s_mi, "MI", pattern_path, "mean_intensity_map")

    del s_mi
    gc.collect()


def save_rgb_vbse(pattern_path):
    s_vbse = kp.load(pattern_path, lazy=True)
    vbse_gen = kp.imaging.VirtualBSEImager(s_vbse)
    vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
    vbse_map.change_dtype("uint8")
    vbse_map = vbse_map.data
    generate_figure(vbse_map, s_vbse, "VBSE", pattern_path, "vbse_rgb")

    del s_vbse
    gc.collect()
