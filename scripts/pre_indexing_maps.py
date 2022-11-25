from os import path
from kikuchipy import load, generators
from matplotlib_scalebar.scalebar import ScaleBar
import matplotlib.pyplot as plt

from utils.worker import Worker
from PySide6.QtCore import QThreadPool

save_fig_kwargs = dict(bbox_inches="tight", pad_inches = 0)

def toWorker(function, console, *args, **kwargs):
    worker = Worker(function, console, *args, **kwargs)
    QThreadPool.globalInstance().start(worker)

def generate_figure(image, pattern):
    print("Generating image...")
    scale = pattern.axes_manager["x"].scale
    fig, ax = plt.subplots()
    ax.axis("off")
    ax.imshow(image, cmap="gray")
    scalebar = ScaleBar(scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
    ax.add_artist(scalebar)
    return fig
    
def save_iq_map(pattern_path):
    s = load(pattern_path, lazy=True)
    iq_map = s.get_image_quality()
    fig = generate_figure(iq_map, s)
    plt.savefig(
        path.join(path.dirname(pattern_path), "image_quality_map.png"),
        **save_fig_kwargs,
    )
    print("Image quality map saved")

def save_adp_map(pattern_path):
    s = load(pattern_path, lazy=True)
    adp_map = s.get_average_neighbour_dot_product_map()
    fig = generate_figure(adp_map, s)
    plt.savefig(
        path.join(path.dirname(pattern_path), "average_dot_product_map.png"),
        **save_fig_kwargs
    )
    print("Average dot product map saved")

def save_mean_intensity_map(pattern_path):
    s = load(pattern_path, lazy=True)
    mim_map = s.mean(axis=(2, 3))
    fig=generate_figure(mim_map, s)
    plt.savefig(
        path.join(path.dirname(pattern_path), "mean_intensity_map.png"),
        **save_fig_kwargs
    )
    print("Mean intensity map saved")

def save_rgb_vbse(pattern_path):
    s = load(pattern_path, lazy=True)
    vbse_gen = generators.VirtualBSEGenerator(s)
    vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
    vbse_map.change_dtype("uint8")
    vbse_map = vbse_map.data
    fig = generate_figure(vbse_map, s)
    plt.savefig(
        path.join(path.dirname(pattern_path), "vbse_rgb.png"),
        **save_fig_kwargs
    )
    print("Virtual backscatter electron image saved")
