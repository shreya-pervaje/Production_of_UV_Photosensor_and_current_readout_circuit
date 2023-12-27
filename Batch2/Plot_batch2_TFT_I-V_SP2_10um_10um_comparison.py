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
plt.figure(figsize= (14*cm,10*cm),dpi=600)
settings = {"xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "font.size": 18,
            "legend.fontsize": 12,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

UGate, IDrain = np.genfromtxt("WithoutDielectric/SP2_Batch2_10u_10u_TFT_Measurement1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'g', label = "Only TFT") 
plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)',fontsize=18)
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)',fontsize=18)


dataname = 'SP2_10um_10um_withAu\SP2_10um_10um_withAu.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Append3", usecols=[0])      
I_Drain = pd.read_excel(dataname, sheet_name='Append3', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'r',label = 'After gold deposition')


dataname = 'WithAu_IGZO\SP2_Batch2_WithoutDi_WithAu_IGZO.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'b', label = 'After a-IGZO deposition')


plt.yscale('log')
plt.legend(fontsize=10)
#plt.ylim(-2.2e-10,5.2e-10)
plt.xlim(-20.2,20.2)
#.title(dataname)
plt.tight_layout()

plt.savefig('plot_SP2_different_layers.eps',format = 'eps')