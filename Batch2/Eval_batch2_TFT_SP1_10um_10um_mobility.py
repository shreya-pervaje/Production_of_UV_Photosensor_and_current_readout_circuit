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

x_axis = ['1', '2','3','4','5']
V_threshold = [0.617, 0.589, -0.083, -0.288, -0.387]

plt.style.use('default')
plt.scatter(x_axis, V_threshold, color='red')
plt.ylabel('Threshold voltage $V_{th}$ (V)',fontsize=8)
plt.ylim(-1,1)
plt.xlabel('Steps',fontsize=8)
#plt.xticks(rotation=30)
#plt.show()
plt.tight_layout()
#plt.savefig('bar_plot_threshold_SP1.eps',format = 'eps')