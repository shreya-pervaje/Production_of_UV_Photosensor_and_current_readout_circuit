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

#image settings
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

AnzahlTransistorenInSerienmessung = 4

colors = ['blue','red','yellow','green']
dataname = 'DarkCurrent_vs_OxygenConc.xlsx'

# to read the data from excel sheet
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1],engine='openpyxl')
I_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0],engine='openpyxl')

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]

plt.plot(U_Drain,np.abs(I_Drain),color = colors[0],label = '9% Oxygen')

# to read different columns of excel file and plot
j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1

    U_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[1],engine='openpyxl')
    I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[0],engine='openpyxl')

    U_Drain = np.array(U_Drain.T)[0]
    I_Drain = np.array(I_Drain.T)[0]
    
    if j == 2:
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[1])
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[1],label = '18% Oxygen')
    elif j == 3:
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[2])
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[2],label = '24% Oxygen')
    elif j == 4:
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[3])
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[3],label = '30% Oxygen')
        

   
plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')
plt.legend()
plt.yscale('log')

plt.savefig('plot_dark_current_vs_oxygen_concentration.png')


