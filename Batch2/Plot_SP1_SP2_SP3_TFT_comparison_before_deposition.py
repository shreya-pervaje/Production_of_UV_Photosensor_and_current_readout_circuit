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

dataname = 'SP1\TFT_Measurements\SP1_10um_10um\WithDi_Au_IGZO\SP1_Batch2_WithDi_Au_IGZO.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'r', label = 'SP1')


dataname = 'SP2\TFT_Measurements\SP2_10um_10um\WithAu_IGZO\SP2_Batch2_WithoutDi_WithAu_IGZO.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'b', label = 'SP2')

UGate, IDrain = np.genfromtxt("SP3\TFT_Measurement\SP3_10um_10um\SP3_Batch2_10u_10u_TFT_Measurement1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'y', label = 'SP3') 
plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)')
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)')

plt.yscale('log')
plt.legend(loc='upper left',fontsize=6)
#plt.ylim(-2.2e-10,5.2e-10)
plt.xlim(-20.2,20.2)
#.title(dataname)
#plt.title('Effect of photosensor production on TFT')
plt.tight_layout()

plt.savefig('plot_TFT_SP1_SP2_SP3.png')