import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Rules and conventions for ETFs
# 's' is defined by convention as the distance from the center of the ETF to the center of the hot junction contact.

rule_NW_enclose_pplus = 1e-6  # Conservative convention since we don't know how accurate pplus is
rule_NW_extend_min = 1e-6   # How far the NW should extend beyond the RPO contact edge, just a guess
rule_pplus_extend_min = rule_NW_extend_min - rule_NW_enclose_pplus 

# Process-specific definitions
viawidth = 0.22e-6                  # As drawn in .gds files
contact_margin_RPO = 0.22e-6

t_STI = 0.350e-6                    # As given in MUSE document
dt_STI = 0.171*t_STI
t_ILD = 7500e-10
dt_ILD = 0.214*t_ILD
t_IMDa = 11800e-10
dt_IMDa = 0.2*t_IMDa
t_IMDb = 2000e-10
dt_IMDb = 0.03*t_IMDb
t_pass1 = 10000e-10
dt_pass1 = 0.1*t_pass1
t_pass2 = 15000e-10
dt_pass2 = 0.1*t_pass2
t_pass3 = 6000e-10
dt_pass3 = 0.1*t_pass3

t_M1 = 5300e-10         # As given in the PDK
t_M2 = t_M1
t_M3 = t_M1             # T-180-LO-DR-100_2_15.pdf page 141
t_M4 = t_M1
t_M5 = t_M1
t_M6 = 9900e-10
t_poly = 2000e-10
t_20KA_UTM = 23400e-10      # Ultra thick metal metal layer without MIM cap
t_40KA_UTM = 46000e-10      # Ultra thick metal metal layer with MIM cap

def construct_heater_geometry(type, targetfile):
    return None

def generate_geometry(s,l_tp,ext_NW,ext_pplus,heater_type,targetfile):
    construct_heater_geometry(heater_type, targetfile)

    r_hotj = s + viawidth/2 + contact_margin_RPO

    return None

def main():
    targetfile = "heater_geometry.mph"
    s = 24e-6
    l_tp = 24e-6
    ext_NW = 2e-6
    ext_pplus = 2e-6
    heater_type = "default"

    # safetynet NW
    if ext_NW < rule_NW_extend_min:
        raise ValueError(f"ext_NW must be at least {rule_NW_extend_min} m. It may not be negative.")
    # safetynet pplus
    if ext_pplus < rule_pplus_extend_min:
        raise ValueError(f"ext_pplus must be at least {rule_pplus_extend_min} m. It may not be negative.")
    if ext_pplus > ext_NW - rule_NW_enclose_pplus:
        raise ValueError(f"ext_pplus must be less than ext_NW - {rule_NW_enclose_pplus} m")

    generate_geometry(s, l_tp, ext_NW, ext_pplus, heater_type, targetfile)
    return None

if "__name__" == "__main__":
    main()