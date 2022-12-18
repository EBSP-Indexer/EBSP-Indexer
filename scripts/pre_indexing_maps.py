from os import path
import kikuchipy as kp
from matplotlib_scalebar.scalebar import ScaleBar
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

save_fig_kwargs = dict(bbox_inches="tight", pad_inches = 0)

def generate_figure(image, pattern, col_label):
    print("Generating image...")
    scale = pattern.axes_manager["x"].scale
    fig, ax = plt.subplots()
    ax.axis("off")
    plot = ax.imshow(image, cmap="gray")
    if col_label != "VBSE":
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(plot, cax=cax, label=col_label)
    scalebar = ScaleBar(scale, "um", location="lower left", box_alpha=0.5, border_pad=0.4)
    ax.add_artist(scalebar)
    return fig
    
def save_iq_map(pattern_path):
    s = kp.load(pattern_path, lazy=True)
    iq_map = s.get_image_quality()
    fig = generate_figure(iq_map, s, "IQ")
    plt.savefig(
        path.join(path.dirname(pattern_path), "image_quality_map.png"),
        **save_fig_kwargs,
    )
    print("Image quality map saved")
    plt.close(fig)


def save_adp_map(pattern_path):
    s = kp.load(pattern_path, lazy=True)
    adp_map = s.get_average_neighbour_dot_product_map()
    fig = generate_figure(adp_map, s, "ADP")
    plt.savefig(
        path.join(path.dirname(pattern_path), "average_dot_product_map.png"),
        **save_fig_kwargs
    )
    print("Average dot product map saved")
    plt.close(fig)


def save_mean_intensity_map(pattern_path):
    s = kp.load(pattern_path, lazy=True)
    mim_map = s.mean(axis=(2, 3))
    fig=generate_figure(mim_map, s, "MI")
    plt.savefig(
        path.join(path.dirname(pattern_path), "mean_intensity_map.png"),
        **save_fig_kwargs
    )
    print("Mean intensity map saved")
    plt.close(fig)


def save_rgb_vbse(pattern_path):
    s = kp.load(pattern_path, lazy=True)
    vbse_gen = kp.generators.VirtualBSEGenerator(s)
    vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
    vbse_map.change_dtype("uint8")
    vbse_map = vbse_map.data
    fig = generate_figure(vbse_map, s, "VBSE")
    plt.savefig(
        path.join(path.dirname(pattern_path), "vbse_rgb.png"),
        **save_fig_kwargs
    )
    print("Virtual backscatter electron image saved")
    plt.close(fig)
