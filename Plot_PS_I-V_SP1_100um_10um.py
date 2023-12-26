import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
#import xlrd
import os
import sys
import matplotlib as mpl

def linear(x, a, b):
    return a * x + b
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


AnzahlTransistorenInSerienmessung = 8

colors = ['blue','red']
dataname = 'SP2_100um_10um_PS_I-V.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])

        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]

plt.plot(U_Drain,I_Drain,color = colors[0],label = 'light off')
#plt.show()
#sys.exit()
j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1



    U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[1])

    I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[0])

    U_Gate = np.array(U_Gate.T)[0]
    I_Drain = np.array(np.abs(I_Drain.T))[0]
    
    if j < 5:
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[0])
    elif j >= 5:
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[1])
        
plt.plot(U_Drain,np.abs(I_Drain),color = colors[1],label = 'light on')
   
plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')

plt.legend(fontsize=6)
plt.yscale('log')
#plt.show()
plt.tight_layout()
plt.savefig('plot_100um_10um_batch2_SP1.png')
#plt.title(dataname)

