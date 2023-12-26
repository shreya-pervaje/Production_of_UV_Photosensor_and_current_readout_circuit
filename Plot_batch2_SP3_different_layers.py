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
settings = {"xtick.labelsize": 5,
            "ytick.labelsize": 5,
            "font.size": 6,
            "legend.fontsize": 3,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

UGate, IDrain = np.genfromtxt("SP3_Batch2_10u_10u_TFT_Measurement1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y') 
plt.xlabel('Gate voltage $V_\mathrm{Gate}$ (V)')
plt.ylabel('Drain current $I_\mathrm{Drain}$ (A)')

UGate, IDrain = np.genfromtxt("SP3_Batch2_10u_10u_TFT_Measurement2.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y') 
plt.xlabel('Gate voltage $V_\mathrm{Gate}$ (V)')
plt.ylabel('Drain current $I_\mathrm{Drain}$ (A)')

UGate, IDrain = np.genfromtxt("SP3_Batch2_10u_10u_TFT_Measurement3.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y') 
plt.xlabel('Gate voltage $V_\mathrm{Gate}$ (V)')
plt.ylabel('Drain current $I_\mathrm{Drain}$ (A)')

UGate, IDrain = np.genfromtxt("SP3_Batch2_10u_10u_TFT_Measurement4.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y') 
plt.xlabel('Gate voltage $V_\mathrm{Gate}$ (V)')
plt.ylabel('Drain current $I_\mathrm{Drain}$ (A)')

plt.title("Only TFTs on the substrate",loc='center')
plt.yscale('log')
plt.legend()
#plt.ylim(-2.2e-10,5.2e-10)
plt.xlim(-20.2,20.2)
#.title(dataname)
plt.tight_layout()
plt.savefig('plot_SP3_different_layers.png')
plt.savefig('plot_SP3_different_layers.eps', format='eps')