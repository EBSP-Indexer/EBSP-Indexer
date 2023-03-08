from utils import SettingFile

from os import path

import kikuchipy as kp
import orix
from diffsims.crystallography import ReciprocalLatticeVector

from utils.threads.thdout import ThreadedOutput

from contextlib import redirect_stdout

import numpy as np



def find_hkl(phase):
    FCC = ["ni", "al", "austenite", "cu", "si"]
    BCC = ["ferrite"]
    #TETRAGONAL = ["steel_sigma"]
    if phase.lower() in FCC:
        return [[1, 1, 1], [2, 0, 0], [2, 2, 0], [3, 1, 1]]
    elif phase.lower() in BCC:
        return [[0, 1, 1], [0, 0, 2], [1, 1, 2], [0, 2, 2]]

class crystalMap:
    """
    Loads a crystal map and generates neccesary properties
    
    """

    def __init__(
        self,
        dataset,
        crystal_map_path: str):
        self.crystal_map = dataset
        self.datatype = "crystal map"
        self.phase_id_array = self.crystal_map.get_map_data("phase_id")
        self.nav_shape = self.crystal_map.shape[::-1]
        self.ebsd = self.ebsd_signal(crystal_map_path)
        thdout = ThreadedOutput()
        with redirect_stdout(thdout):
            self.hkl = self.hkl_simulation(crystal_map_path)
            self.navigator = {"Inverse polefigure": self.inverse_pole_figure(), "Phase map": self.phase_map()}
        #self.ipf = self.inverse_pole_figure()
        #self.phase_map = self.phase_map()
    
    def ebsd_signal(self, crystal_map_path):
        try:
        # returns a dictionary with values stored in di_parameters.txt
            parameter_file = SettingFile(
            path.join(path.dirname(crystal_map_path), "indexing_parameters.txt")
            )
        except FileNotFoundError as e:
            raise e

        ebsd_signal_name = parameter_file.read("Pattern name")
        ebsd_signal = kp.load(path.join(path.dirname(path.dirname(crystal_map_path)), ebsd_signal_name))
        
        return ebsd_signal

    def hkl_simulation(self, crystal_map_path):
        hkl_simulations = []

        for i, ph in self.crystal_map.phases:
            if ph.name != "not_indexed":
                rlv = ReciprocalLatticeVector(
                    phase=ph, hkl=find_hkl(ph.name)
                )
                rlv = rlv.symmetrise()
                simulator = kp.simulations.KikuchiPatternSimulator(rlv)
                hkl_simulations.append(simulator.on_detector(self.detector(crystal_map_path), self.crystal_map.rotations.reshape(*self.crystal_map.shape)))
    
        return hkl_simulations
    
    def inverse_pole_figure(self):
        
        ckey = orix.plot.IPFColorKeyTSL(self.crystal_map.phases[0].point_group)
        
        rgb_all = np.zeros((self.crystal_map.size, 3))
        for i, phase in self.crystal_map.phases:
            if i != -1:
                rgb_i = ckey.orientation2color(self.crystal_map[phase.name].orientations)
                rgb_all[self.crystal_map.phase_id == i] = rgb_i

        rgb_all = rgb_all.reshape(self.crystal_map.shape + (3,))

        return rgb_all

    def phase_map(self):
        thdout = ThreadedOutput()
        with redirect_stdout(thdout):
            phase_id = self.crystal_map.get_map_data("phase_id")
            unique_phase_ids = np.unique(phase_id[~np.isnan(phase_id)])
            phase_map = np.ones(phase_id.shape + (3,))
            for i, color in zip(unique_phase_ids, self.crystal_map.phases_in_data.colors_rgb):
                mask = phase_id == int(i)
                phase_map[mask] = phase_map[mask] * color
            
            phase_map = np.squeeze(phase_map)
        
        return phase_map
    
    def detector(self, crystal_map_path):
        detector = kp.detectors.EBSDDetector.load(path.join(path.dirname(crystal_map_path), "detector.txt"))
        ebsd_signal = self.ebsd_signal(crystal_map_path)
        detector.shape = ebsd_signal.axes_manager.signal_shape

        return detector
    
class EBSDDataset:

    """
    Loads an EBSD dataset
    """

    def __init__(
            self,
            dataset,
            ebsd_pattern_path: str):
        
        self.ebsd = dataset
        self.datatype = "ebsd_dataset"
        self.nav_shape = self.ebsd.axes_manager.navigation_shape
        self.navigator = {"Mean intensity map": self.ebsd.mean(axis=(2,3)), "Image quality map": self.ebsd.get_image_quality().compute()}


        

    



