import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
#import xlrd
import os
import sys
import matplotlib as mpl
from array import array

def linear(x, a, b):
    return a * x + b
savePlot = True
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
dataname = 'SP1_100um_10um_PS_I-V.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])     
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]
plt.plot(U_Drain,I_Drain,color = colors[0],label='SP1: light off',linewidth=4)
#plt.show()
#sys.exit()
appends = "Append5"
U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[1])
I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[0])
U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]  
#plt.plot(U_Drain,np.abs(I_Drain),color = colors[1])
plt.plot(U_Gate,np.abs(I_Drain),color = colors[1], label = 'SP1: light on',linewidth=4)
dataname = 'SP2_100um_10um_PS_I-V.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])     
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]
plt.plot(U_Drain,I_Drain,color = colors[2],label='SP2: light off',linewidth=4)
#plt.show()
#sys.exit()
appends = "Append5"   
U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[1])
I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[0])
U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]
plt.plot(U_Gate,np.abs(I_Drain),color = colors[3], label = 'SP2: light on',linewidth=4)


plt.legend(loc='lower left',fontsize=10)


plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')

#plt.legend()
plt.yscale('log')
#plt.show()
plt.tight_layout()
#plt.savefig('plot_100um_10um_batch2_PS_compare.png')
#plt.title(dataname)

