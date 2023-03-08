from utils import SettingFile

from os import path

import kikuchipy as kp
import orix
from diffsims.crystallography import ReciprocalLatticeVector

from utils.threads.thdout import ThreadedOutput

from contextlib import redirect_stdout

import numpy as np

#from scripts.signal_loader import crystalMap

def find_hkl(phase):
    FCC = ["ni", "al", "austenite", "cu", "si"]
    BCC = ["ferrite"]
    TETRAGONAL = ["steel_sigma"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]
    elif phase.lower() in TETRAGONAL:
        return [[1, 1, 0], [2, 0, 0], [1, 0, 1], [2, 1, 0], [1, 1, 1], [2, 2, 0], [2, 1, 1]]

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


def return_ebsd_pattern(ebsd_signal):

    ebsd_pattern = {}
    ebsd_pattern["type"] = "ebsd dataset"
    ebsd_pattern["ebsd_data"] = ebsd_signal
    ebsd_pattern["nav_shape"] = ebsd_signal.axes_manager.navigation_shape
    
    mean_intensity_map = ebsd_signal.mean(axis=(2, 3))
    image_quality_map = ebsd_signal.get_image_quality().compute()

    ebsd_pattern["navigator"] = {"Mean intensity map": mean_intensity_map, "Image quality map": image_quality_map}

    return ebsd_pattern


def return_crystal_map(file_path, crystal_map):
    #thdout = ThreadedOutput()
    crystal_map_dict = {}
    crystal_map_dict["type"] = "crystal map"

    #crystal_map_object = crystalMap(file_path)
    crystal_map_dict["phase_id_map"] = crystal_map.get_map_data("phase_id")
    #crystal_map_dict["phase_id_map"] = crystal_map_object.phase_id_array


    crystal_map_dict["crystal_map"] = crystal_map
    #crystal_map_dict["crystal_map"] = crystal_map_object.crystal_map
    print("hit")
    crystal_map_dict["nav_shape"] = crystal_map.shape[::-1]
    #crystal_map_dict["nav_shape"] = crystal_map_object.nav_shape

    #crystal_map_dict["ebsd_data"] = crystal_map_object.ebsd
    #crystal_map_dict["geo_sim"] = crystal_map_object.hkl

    #ipf_all = crystal_map_object.ipf
    #data = crystal_map_object.phase_map

    #crystal_map_dict["navigator"] = {"Inverse pole figure": ipf_all, "Phase map": data}
    

    
    try:
        # returns a dictionary with values stored in di_parameters.txt
        parameter_file = SettingFile(
            path.join(path.dirname(file_path), "indexing_parameters.txt")
        )
    except FileNotFoundError as e:
        raise e

    pattern_name = parameter_file.read("Pattern name")
    pattern = kp.load(path.join(path.dirname(path.dirname(file_path)), pattern_name))

    # Get detector from indexing routine
    detector = kp.detectors.EBSDDetector.load(path.join(path.dirname(file_path), "detector.txt"))
    # Ensure that detector and original EBSD pattern shares same shape
    detector.shape = pattern.axes_manager.signal_shape

    
    
    #Generate geometrical simulation based on orientations in crystal map
    #with redirect_stdout(thdout):
    sims = []

    for i, ph in crystal_map.phases:
        if ph.name != "not_indexed":
            rlv = ReciprocalLatticeVector(
                phase=ph, hkl=find_hkl(ph.name)
            )
            rlv = rlv.symmetrise()
            simulator = kp.simulations.KikuchiPatternSimulator(rlv)
            sims.append(simulator.on_detector(detector, crystal_map.rotations.reshape(*crystal_map.shape)))
    
    crystal_map_dict["ebsd_data"] = pattern
    crystal_map_dict["geo_sim"] = sims

    ckey = orix.plot.IPFColorKeyTSL(crystal_map.phases[0].point_group)
    rgb_all = np.zeros((crystal_map.size, 3))
    for i, phase in crystal_map.phases:
        if i != -1:
            rgb_i = ckey.orientation2color(crystal_map[phase.name].orientations)
            rgb_all[crystal_map.phase_id == i] = rgb_i

    ipf_all = rgb_all.reshape(crystal_map.shape + (3,))

    #Generating a phase map array, adapted from the orix method orix_map_plot with minor adjustments
    phase_id = crystal_map.get_map_data("phase_id")
    unique_phase_ids = np.unique(phase_id[~np.isnan(phase_id)])
    data = np.ones(phase_id.shape + (3,))
    for i, color in zip(unique_phase_ids, crystal_map.phases_in_data.colors_rgb):
        mask = phase_id == int(i)
        data[mask] = data[mask] * color

    # Add legend patches to plot
    #patches = []
    #for _, p in crystal_map.phases_in_data:
    #    patches.append(mpatches.Patch(color=p.color_rgb, label=p.name))

        data = np.squeeze(data)
        
        crystal_map_dict["navigator"] = {"Inverse pole figure": ipf_all, "Phase map": data}
    
    
    return crystal_map_dict