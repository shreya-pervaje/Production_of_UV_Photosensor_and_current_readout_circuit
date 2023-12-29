# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 22:29:46 2023

@author: Shreya Pervaje
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from glob import glob
import pandas as pd
import xlrd
import os
from scipy.constants import constants
from scipy.optimize import curve_fit
import matplotlib as mpl

savePlot = True
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

x_axis = ['PS1','PS2','PS3','PS4']
Mobility = [8.75,8.861,7.393,9.9]


#plt.style.use('default')
plt.scatter(x_axis, Mobility, color='blue')
plt.ylim(5,13)
plt.xlabel('Setup')
plt.ylabel('Mobility $\u03BC$ (cm$^2$/(Vs))')
plt.tight_layout()
plt.savefig('plot_batch4_tft_mobility_compare.png')