def pc_from_wd(microscope: str, working_distance: float, convention="TSL"):
    """
    Returns pattern center depending microscope, calculated from linear regression of PC's from different working distances.
    
    If no microsope configuration is found, return (0.5, 0.8, 0.5) TSL
    """
    if microscope == "ZEISS SUPRA55 VP":
        pc = [
        0.5605-0.0017*float(working_distance),
        1.2056-0.0225*float(working_distance),
        0.483,
        ]
    
    else:
        # TSL
        pc = [0.5000, 0.8000, 0.5000]

    if convention == "BRUKER":
        pc[1] = 1-pc[1]
    
    return pc