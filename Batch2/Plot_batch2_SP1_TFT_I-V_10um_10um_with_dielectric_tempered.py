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
            "font.size": 7,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)
savePlot = True

AnzahlTransistorenInSerienmessung = 4

dataname = 'SP1_10um_10um_with_dielectric_temp.xls'
U_Gate = pd.read_excel(dataname, sheet_name="Data", usecols=[0])    
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])

U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(I_Drain.T)[0]  
plt.plot(U_Gate,I_Drain)

j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1

    U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[0])
    I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[1])

    U_Gate = np.array(U_Gate.T)[0]
    I_Drain = np.array(I_Drain.T)[0]
   
    plt.plot(U_Gate,I_Drain)
   
plt.plot(U_Gate,I_Drain,'b')    
plt.xlabel('Gate voltage $V_\mathrm{GS}$ (V)')
plt.ylabel('Drain current $I_\mathrm{DS}$ (A)')

plt.yscale('log')
plt.xlim(-20.2,20.2)
plt.tight_layout()
plt.savefig('plot_batch2_TFT_I-V_SP1_10um_10um_with_dielectric_tempered.png')