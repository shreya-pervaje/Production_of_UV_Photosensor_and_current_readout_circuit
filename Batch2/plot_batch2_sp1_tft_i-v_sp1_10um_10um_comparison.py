import numpy as np
import matplotlib.pyplot as plt
#import sys
#from glob import glob
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
            "legend.fontsize": 10,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

plt.style.use('default')
UGate, IDrain = np.genfromtxt("SP1_10um_10um_without_dielectric/SP1_Batch2_10u_10u_TFT_Measurement1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'green', label = "Only TFT",linewidth=4) 
plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)',fontsize=18)
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)',fontsize=18)


UGate, IDrain = np.genfromtxt("SP1_10um_10um_with_dielectric/SP1_Batch2_10u_10u_WithDielectric_TFT_Measurement1.txt", delimiter= '\t', unpack = True)    
plt.plot(UGate,np.absolute(IDrain),'orange', label = "After dielectric depo.",linewidth=4) 


dataname = 'SP1_10um_10um_with_dielectric_tempered/SP1_10um_10um_with_dielectric_temp.xls'
U_Gate = pd.read_excel(dataname, sheet_name="Data", usecols=[0])      
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Gate,I_Drain,'cyan',label = 'After tempering',linewidth=4)


dataname = 'SP1_10um_10um_with_dielectric_tempered_Au/SP1_10um_10um_withDi_Temp_withAu.xls'
U_Gate = pd.read_excel(dataname, sheet_name="Data", usecols=[0])       
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Gate,I_Drain,'red',label = 'After Cr-Au depo.',linewidth=4)


dataname = 'SP1_10um_10um_with_dielectric_tempered_Au_IGZO/SP1_Batch2_WithDi_Au_IGZO.xls'
U_Gate = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Gate,I_Drain,'blue', label = 'After a-IGZO depo.',linewidth=3)


plt.yscale('log')
plt.legend(loc='upper left', fontsize=10)
plt.xlim(-20.2,20.2)
plt.tight_layout()

plt.savefig('plot_batch2_SP1_different_layers.png')