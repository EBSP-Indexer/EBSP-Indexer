from utils import SettingFile

from os import path

import kikuchipy as kp

import orix
from diffsims.crystallography import ReciprocalLatticeVector


from numpy import array

import matplotlib.pyplot as plt

def open_file(file_path):
    """
    File check, checks if the file header is an EBSD pattern or a crystal map

    """

    try:
        s = kp.load(file_path, lazy=True)
    except:
        s = orix.io.load(file_path)

    if isinstance(s, kp.signals.ebsd.EBSD):
        return return_ebsd_pattern(s)

    if isinstance(s, orix.crystal_map.crystal_map.CrystalMap):
        return return_crystal_map(file_path, s)


def return_ebsd_pattern(s):

    ebsd_pattern = {}
    ebsd_pattern["type"] = "ebsd dataset"
    ebsd_pattern["ebsd_data"] = s
    ebsd_pattern["nav_shape"] = s.axes_manager.navigation_shape
    
    mean_intensity_map = s.mean(axis=(2, 3))
    image_quality_map = s.get_image_quality().compute()

    ebsd_pattern["navigator"] = {"Mean intensity map": mean_intensity_map, "Image quality map": image_quality_map}

    return ebsd_pattern


def return_crystal_map(file_path, s):

    crystal_map = {}
    crystal_map["type"] = "crystal map"
    crystal_map["nav_shape"] = s.shape[::-1]

    try:
        # returns a dictionary with values stored in di_parameters.txt
        print(path.join(path.dirname(file_path), "di_parameters.txt"))
        # param_directory = path.dirname(file_path)
        parameter_file = SettingFile(
            path.join(path.dirname(file_path), "di_parameters.txt")
        )
    except FileNotFoundError as e:
        raise e

    pattern_path = parameter_file.read("Dataset path")
    pattern = kp.load(pattern_path)

    # Get detector from indexing routine
    detector = kp.detectors.EBSDDetector.load(path.join(path.dirname(file_path), "detector.txt"))
    detector.shape = pattern.axes_manager.signal_shape
    print(detector)
    # Generate geometrical simulation based on orientations in crystal map
    rlv = ReciprocalLatticeVector(
        phase=s.phases[0], hkl=[[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    )
    rlv = rlv.symmetrise()
    simulator = kp.simulations.KikuchiPatternSimulator(rlv)
    sim = simulator.on_detector(detector, s.rotations.reshape(*s.shape))

    crystal_map["ebsd_data"] = pattern
    crystal_map["geo_sim"] = sim

    # Generate IPF for navigation of crystal map
    ckey = orix.plot.IPFColorKeyTSL(s.phases.point_groups[0])

    ipf = ckey.orientation2color(s["ni"].orientations)
    ipf = ipf.reshape(s.shape + (3,))

    #Generate NCC map


    crystal_map["navigator"] = {"Inverse pole figure": ipf}

    return crystal_map

def export_image(navigator, signal, ):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(navigator)
    ax[1].imshow(signal)

    fig.imsave()
