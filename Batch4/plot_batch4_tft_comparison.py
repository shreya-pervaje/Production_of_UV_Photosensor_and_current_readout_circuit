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

UGate, IDrain = np.genfromtxt("SP1_TFT_10um_10um/Batch4_SP1_TFT_Final1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y', label = "Setup 1") 

UGate, IDrain = np.genfromtxt("SP3_TFT_10um_10um/Batch4_SP3_TFT_Final1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'b', label = "Setup 2") 

UGate, IDrain = np.genfromtxt("SP5_TFT_10um_10um/Batch4_SP5_TFT_Final1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'r', label = "Setup 3") 

UGate, IDrain = np.genfromtxt("SP8_TFT_10um_10um/Batch4_SP8_Final_TFT1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'g', label = "Setup 4") 

plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)',fontsize=9)
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)',fontsize=9)

plt.yscale('log')
plt.legend(fontsize = 6)
plt.xlim(-20.2,20.2)
plt.tight_layout()

plt.savefig('plot_batch4_SP1_different_layers.png')