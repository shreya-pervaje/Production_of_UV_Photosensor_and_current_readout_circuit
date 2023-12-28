import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
import os
import sys
import matplotlib as mpl
from array import array

def linear(x, a, b):
    return a * x + b
savePlot = True

# image settings
cm = 1/2.54
plt.figure(figsize= (15*cm,10*cm),dpi=600)
settings = {"xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "font.size": 18,
            "legend.fontsize": 10,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)


AnzahlTransistorenInSerienmessung = 8

colors = ['red','lightcoral','darkgreen','olive','indigo','darkviolet']

# SP1 data extraction
dataname = 'SP1_100um_10um_PS_I-V.xls'
U_PS = pd.read_excel(dataname, sheet_name="Data", usecols=[1])     
I_PS = pd.read_excel(dataname, sheet_name='Data', usecols=[0])
U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]
plt.plot(U_PS,I_PS,color = colors[0],label='SP1: light off',linewidth=4)

appends = "Append5"
U_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[1])
I_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[0])
U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]  
plt.plot(U_PS,np.abs(I_PS),color = colors[1], label = 'SP1: light on',linewidth=4)

# SP2 data extraction
dataname = 'SP2_100um_10um_PS_I-V.xls'
U_PS = pd.read_excel(dataname, sheet_name="Data", usecols=[1])     
I_PS = pd.read_excel(dataname, sheet_name='Data', usecols=[0])
U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]
plt.plot(U_PS,I_PS,color = colors[2],label='SP2: light off',linewidth=4)

appends = "Append5"   
U_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[1])
I_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[0])
U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]
plt.plot(U_PS,np.abs(I_PS),color = colors[3], label = 'SP2: light on',linewidth=4)


plt.legend(loc='lower left',fontsize=10)

plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')

plt.yscale('log')
plt.tight_layout()
plt.savefig('plot_batch2_PS_I-V_100um_10um_compare.png')


