import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
#import xlrd
import os
import sys
import matplotlib as mpl

def linear(x, a, b):
    return a * x + b

cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

meanT = [130.4,106.3,95.75,87.7]
oxygen = [9,18,24,30]    
argon = [75, 67.5, 62.5, 57.5]    
plt.plot(argon,meanT,'o')
   
plt.xlabel('Argon flow (ml/min)')
plt.ylabel('Thickness of a-IGZO $h$ (nm)')
plt.tight_layout()

plt.savefig('Thickness vs Argon Flow.png')
