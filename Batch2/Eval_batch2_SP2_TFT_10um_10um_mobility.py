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
Mobility = [13.687, 10.12, 10.428]


plt.style.use('default')
plt.scatter(x_axis, Mobility, color='blue')
plt.ylim(8,15)
plt.xlabel('Steps',fontsize=8)
plt.ylabel('Mobility $\u03BC$ (cm$^2$/(Vs))',fontsize=8)
#plt.show()
plt.tight_layout()
plt.savefig('Plot_batch2_SP2_TFT_mobility.png')