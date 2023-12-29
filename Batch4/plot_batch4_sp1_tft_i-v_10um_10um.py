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
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)



UGate, IDrain = np.genfromtxt("Batch4_SP1_TFT_Final1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'b') 

UGate, IDrain = np.genfromtxt("Batch4_SP1_TFT_Final2.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'r') 

UGate, IDrain = np.genfromtxt("Batch4_SP1_TFT_Final3.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y') 
plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)')
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)')


plt.yscale('log')
#plt.title("TFT with reduced no. of layers")
plt.xlim(-20.2,20.2)
plt.tight_layout()
plt.savefig('plot_batch4_sp1_tft_i-v_10um_10um.png')