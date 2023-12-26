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

# ax1 = plt.subplot()
# ax2 = ax1.twinx()

# ax1.tick_params(axis='y', colors='b')
# ax2.tick_params(axis='y', colors='r')

# ax1.yaxis.label.set_color('b')
# ax2.yaxis.label.set_color('r')

AnzahlTransistorenInSerienmessung = 4


dataname = 'SP1_10um_10um_withDi_Temp_withAu.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])

        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
#print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain)

j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1



    U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[0])

    I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[1])

    U_Gate = np.array(U_Gate.T)[0]
    I_Drain = np.array(I_Drain.T)[0]
   # print(np.max(I_Drain))  
    plt.plot(U_Drain,I_Drain)
    print(j)


#print(np.max(I_Drain))    
plt.plot(U_Drain,I_Drain,'b')    
plt.xlabel('Gate voltage $V_\mathrm{Gate}$ (V)')
plt.ylabel('Drain current $I_\mathrm{Drain}$ (A)')

plt.yscale('log')
#plt.legend()
#plt.ylim(-2.2e-10,5.2e-10)
plt.xlim(-20.2,20.2)
#.title(dataname)
plt.tight_layout()

plt.savefig('plot.png')