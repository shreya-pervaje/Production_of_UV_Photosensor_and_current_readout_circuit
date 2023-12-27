import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
import os
import sys
import matplotlib as mpl

def linear(x, a, b):
    return a * x + b
savePlot = True

# image settings
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)


AnzahlTransistorenInSerienmessung = 8

colors = ['blue','red','green','orange']

dataname = 'SP1_100um_10um.xls'

U_PS = pd.read_excel(dataname, sheet_name="Data", usecols=[1])
I_PS = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]

plt.plot(U_PS,I_PS,color = colors[0],label = 'PS_Cr-Au: light off')

# to read different columns in excel and to plot
j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1

    U_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[1])
    I_PS = pd.read_excel(dataname, sheet_name=appends, usecols=[0])

    U_PS = np.array(U_PS.T)[0]
    I_PS = np.array(np.abs(I_PS.T))[0]
    
    if j < 5:
        plt.plot(U_PS,np.abs(I_PS),color = colors[0])
    elif j >= 5:
        plt.plot(U_PS,np.abs(I_PS),color = colors[1])
        
plt.plot(U_PS,np.abs(I_PS),color = colors[1],label = 'PS_Cr-Au: light on')

   
plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')
plt.legend(fontsize=5)
plt.yscale('log')
plt.tight_layout()
plt.savefig('plot_PS_I-V_100um_10um_Au.png')

