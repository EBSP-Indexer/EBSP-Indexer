import sys
import kikuchipy as kp
import matplotlib.pyplot as plt

def open_pattern(file_path):
    s = kp.load(file_path, lazy=True)
    return s

def get_navigation_figure(pattern, nav_type="mean_intensity"):
    if nav_type == "mean_intensity":
        navigator = pattern.mean(axis=(2,3))
    if nav_type == "iq":
        print("ok")
        navigator = pattern.get_image_quality()

    return navigator