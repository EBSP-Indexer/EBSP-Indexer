from utils import SettingFile
from utils.setting_file import get_setting_file_bottom_top

from os import path

import functools

import kikuchipy as kp
import orix
from diffsims.crystallography import ReciprocalLatticeVector

from utils.threads.thdout import ThreadedOutput

from contextlib import redirect_stdout

import numpy as np


def mean_intensity_map(ebsd):
    return ebsd.mean(axis=(2, 3))


class crystalMap:
    """
    crystal map for signal navigation


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
                if len(self.crystal_map.phases.ids) > 1:
                    self.navigator = {
                        "Inverse pole figure": 0,
                        "Phase map": 1,
                    }
                else:
                    self.navigator = {
                        "Inverse pole figure": 0,
                    }
                if "scores" in self.crystal_map.prop:
                    self.navigator["Normalized cross-correlation"] = 2
                if self.crystal_map.rotations_per_point > 1:
                    self.navigator["Orientation similarity metric"] = 3
                
                self.hkl = self.hkl_simulation()

            self.ebsd_detector = self.detector(crystal_map_path)

    def ebsd_signal(self, crystal_map_path):
        try:
            parameter_file, parameter_file_path = get_setting_file_bottom_top(
                crystal_map_path, "indexing_parameters.txt", return_dir_path=True
            )
        except FileNotFoundError as e:
            raise e

        ebsd_signal_name = parameter_file.read("Pattern name")
        ebsd_signal = kp.load(
            path.join(path.dirname(parameter_file_path), ebsd_signal_name)
        )

        return ebsd_signal

    def hkl_simulation(self):
        hkl_simulations = []

        for i, ph in self.crystal_map.phases:
            phase_lattice = ph.structure.lattice
            phase_lattice.setLatPar(
                phase_lattice.a * 10, phase_lattice.b * 10, phase_lattice.c * 10
            )  # diffsim uses ångstrøm and not nm for lattice parameters

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

    def detector(self, crystal_map_path):
        detector = kp.detectors.EBSDDetector.load(
            path.join(
                get_setting_file_bottom_top(
                    crystal_map_path, "detector.txt", return_dir_path=True
                )[-1],
                "detector.txt",
            )
        )
        ebsd_signal = self.ebsd_signal(crystal_map_path)
        detector.shape = ebsd_signal.axes_manager.signal_shape

        return detector
    
    def compute_navigator(self, nav_num: int = 0):
        """
        0 = inverse pole figure
        1 = phase map
        2 = ncc_map
        3 = osm_map
        """

        if nav_num == 0:
            navigator = self.inverse_pole_figure
            return navigator

        if nav_num == 1:
            navigator = self.phase_map
            return navigator
        
        if nav_num == 2:
            navigator =  self.normalized_corss_correlation_map
            return navigator
        
        if nav_num == 3:
            navigator = self.orientation_simliarity_metric
            return navigator

    @functools.cached_property
    def inverse_pole_figure(self):
        if self.crystal_map.phases.ids[0] == -1:
            phase_id = self.crystal_map.phases.ids[1]
        else:
            phase_id = self.crystal_map.phases.ids[0]
        
        ckey = orix.plot.IPFColorKeyTSL(self.crystal_map.phases[phase_id].point_group)
        rgb_all = np.zeros((self.crystal_map.size, 3))
        for i, phase in self.crystal_map.phases:
            if i != -1:
                rgb_i = ckey.orientation2color(
                    self.crystal_map[phase.name].orientations
                )
                rgb_all[self.crystal_map.phase_id == i] = rgb_i

        rgb_all = rgb_all.reshape(self.crystal_map.shape + (3,))

        return rgb_all

    @functools.cached_property
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
    
    @functools.cached_property
    def normalized_corss_correlation_map(self):
        if self.crystal_map.rotations_per_point > 1:
            ncc_map = self.crystal_map.scores[:, 0].reshape(*self.crystal_map.shape)
        else:
            ncc_map = self.crystal_map.get_map_data("scores")

        return ncc_map

    @functools.cached_property
    def orientation_simliarity_metric(self):
        osm_map = kp.indexing.orientation_similarity_map(self.crystal_map)

        return osm_map


class EBSDDataset:

    """
    Loads an EBSD dataset

    """

    def __init__(self, dataset):
        self.ebsd = dataset
        self.datatype = "ebsd_dataset"
        self.nav_shape = self.ebsd.axes_manager.navigation_shape
        self.navigator = {
            "Mean intensity map": 0,
            "Image quality map": 1,
            "VBSE map": 2,
        }

    def compute_navigator(self, nav_num: int = 0):
        """
        Computes navigator

        0 = mean intensity map
        1 = image quality
        2 = virtual bse image
        """

        if nav_num == 0:
            navigator = self.mean_intensity
            return navigator
        if nav_num == 1:
            navigator = self.image_quality
            return navigator
        if nav_num == 2:
            navigator = self.virtual_bse
            return navigator

    @functools.cached_property
    def mean_intensity(self):
        mean_intensity_map = self.ebsd.mean(axis=(2, 3))
        return mean_intensity_map

    @functools.cached_property
    def image_quality(self):
        return self.ebsd.get_image_quality().compute()

    @functools.cached_property
    def virtual_bse(self):
        vbse_gen = kp.generators.VirtualBSEGenerator(self.ebsd)
        vbse_map = vbse_gen.get_rgb_image(r=(3, 1), b=(3, 2), g=(3, 3))
        vbse_map.change_dtype("uint8")
        vbse_map = vbse_map.data
        return vbse_map
