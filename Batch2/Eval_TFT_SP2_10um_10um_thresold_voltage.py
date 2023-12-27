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

x_axis = ['1', '2','3']
V_threshold = [3.678, 2.705, 2.529]

plt.style.use('default')
plt.scatter(x_axis, V_threshold, color='red')
plt.ylabel('Threshold voltage $V_{th}$ (V)',fontsize=8)
plt.ylim(0,5)
plt.xlabel('Steps',fontsize=8)
#plt.xticks(rotation=30)
#plt.show()
plt.tight_layout()
plt.savefig('SP2_bar_plot_threshold.eps',format = 'eps')