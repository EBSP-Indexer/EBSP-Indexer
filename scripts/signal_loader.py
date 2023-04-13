from utils import SettingFile

from os import path

import kikuchipy as kp
import orix
from diffsims.crystallography import ReciprocalLatticeVector

from utils.threads.thdout import ThreadedOutput

from contextlib import redirect_stdout

import numpy as np

def mean_intensity_map(ebsd):
    return ebsd.mean(axis=(2, 3))


def virtual_bse_map(ebsd):
    vbse_gen = kp.generators.VirtualBSEGenerator(ebsd)
    vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
    vbse_map.change_dtype("uint8")
    vbse_map = vbse_map.data
    return vbse_map

def check_directory(file_path):
    folder_names = ["unrefined_crystal_maps", "refined_crystal_maps"]
    if path.basename(path.dirname(file_path)) in folder_names:
        pattern_dir = path.dirname(path.dirname(file_path))
    else:
        pattern_dir = path.dirname(file_path)
    
    return pattern_dir

class crystalMap:
    """
    Loads a crystal map

    """

    def __init__(self, dataset, crystal_map_path: str, compute_all: bool = False):

        self.crystal_map = dataset
        self.datatype = "crystal map"
        if compute_all:
            self.phase_id_array = self.crystal_map.get_map_data("phase_id")
            self.nav_shape = self.crystal_map.shape[::-1]
            self.ebsd = self.ebsd_signal(crystal_map_path)
            thdout = ThreadedOutput()
            with redirect_stdout(thdout):            
                self.navigator = {
                    "Inverse polefigure": self.inverse_pole_figure(),
                    "Phase map": self.phase_map(),
                    "Mean intensity map": mean_intensity_map(self.ebsd),
                    "Virtual BSE map": virtual_bse_map(self.ebsd),
                    # "NCC": self.property_map("scores"),
                    # "Orientation similarity map": self.orientation_similarity_map(),

                }

                self.hkl = self.hkl_simulation(crystal_map_path)

            self.ebsd_detector = self.detector(crystal_map_path)

    def ebsd_signal(self, crystal_map_path):
        try:
            # returns a dictionary with values stored in di_parameters.txt
            parameter_file = SettingFile(
                path.join(check_directory(crystal_map_path), "indexing_parameters.txt")
            )
        except FileNotFoundError as e:
            raise e

        ebsd_signal_name = parameter_file.read("Pattern name")
        ebsd_signal = kp.load(
            path.join(path.dirname(check_directory(crystal_map_path)), ebsd_signal_name)
        )

        return ebsd_signal

    def hkl_simulation(self, crystal_map_path):
        hkl_simulations = []

        for i, ph in self.crystal_map.phases:
            phase_lattice = ph.structure.lattice
            phase_lattice.setLatPar(phase_lattice.a*10, phase_lattice.b*10, phase_lattice.c*10) #diffsim uses ångstrøm and not nm for lattice parameters

            if i != -1:
                rlv = ReciprocalLatticeVector.from_min_dspacing(ph, 0.7)

                rlv.sanitise_phase()
                rlv = rlv.unique(use_symmetry=True)
                rlv.calculate_structure_factor("lobato")

                structure_factor = abs(rlv.structure_factor)
                order = np.argsort(structure_factor)[::-1]
                rlv = rlv[order[0:4]]
                rlv = rlv.symmetrise()
                hkl_simulations.append(rlv)

        return hkl_simulations

    def inverse_pole_figure(self):

        ckey = orix.plot.IPFColorKeyTSL(self.crystal_map.phases[0].point_group)

        rgb_all = np.zeros((self.crystal_map.size, 3))
        for i, phase in self.crystal_map.phases:
            if i != -1:
                rgb_i = ckey.orientation2color(
                    self.crystal_map[phase.name].orientations
                )
                rgb_all[self.crystal_map.phase_id == i] = rgb_i
        
        rgb_all = rgb_all.reshape(self.crystal_map.shape + (3,))
        
        return rgb_all

    def phase_map(self):
        thdout = ThreadedOutput()
        with redirect_stdout(thdout):
            phase_id = self.crystal_map.get_map_data("phase_id")
            unique_phase_ids = np.unique(phase_id[~np.isnan(phase_id)])
            phase_map = np.ones(phase_id.shape + (3,))
            for i, color in zip(
                unique_phase_ids, self.crystal_map.phases_in_data.colors_rgb
            ):
                mask = phase_id == int(i)
                phase_map[mask] = phase_map[mask] * color

            phase_map = np.squeeze(phase_map)

        return phase_map

    def detector(self, crystal_map_path):
        detector = kp.detectors.EBSDDetector.load(
            path.join(check_directory(crystal_map_path), "detector.txt")
        )
        ebsd_signal = self.ebsd_signal(crystal_map_path)
        detector.shape = ebsd_signal.axes_manager.signal_shape

        return detector


    # def property_map(self, property: str):
    #     if self.crystal_map.rotations_per_point > 1:
    #         property_map = self.crystal_map.scores[:, 0].reshape(*self.crystal_map.shape)
    #     else:
    #         property_map = self.crystal_map.get_map_data(property)

    #     return property_map
    
    # def orientation_similarity_map(self):
    #     try:
    #         osm = kp.indexing.orientation_similarity_map(self.crystal_map)
    #     except:
    #         osm = None

    #     return osm
    
class EBSDDataset:

    """
    Loads an EBSD dataset
    """

    def __init__(self, dataset, ebsd_pattern_path: str):

        self.ebsd = dataset
        self.datatype = "ebsd_dataset"
        self.nav_shape = self.ebsd.axes_manager.navigation_shape
        self.navigator = {
            "Mean intensity map": mean_intensity_map(self.ebsd),
            "Image quality map": self.ebsd.get_image_quality().compute(),
            "VBSE map": virtual_bse_map(self.ebsd),
        }


