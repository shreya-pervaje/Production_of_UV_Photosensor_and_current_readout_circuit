import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
import xlrd
import os
import sys
import matplotlib as mpl

def linear(x, a, b):
    return a * x + b

savePlot = True
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 7,
            "ytick.labelsize": 7,
            "font.size": 6,
            "legend.fontsize": 3,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

AnzahlTransistorenInSerienmessung = 8
colors = ['blue','red']
PSx = 4
SPy = 8
y = 5

while y <= SPy:
    x = 1
    while x <= PSx:
        plt.figure()
        dataname = 'Batch4_SP' + str(y) +'_PS' + str(x) + '_I-V.xls'
        U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])
        
        I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])
        
        U_Drain = np.array(U_Drain.T)[0]
        I_Drain = np.array(np.abs(I_Drain.T))[0]
        
        plt.plot(U_Drain,np.abs(I_Drain),color = colors[0],label = 'light off')
    
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
        plt.legend(fontsize='6')
        plt.yscale('log')
        #plt.title('Batch4_SP' + str(y) +'_PS' + str(x))
        #plt.show()
        plt.tight_layout()
        plt.savefig('Batch4_SP' + str(y) + '_PS' + str(x) +'_I-V_plot.png')
        plt.savefig('Batch4_SP' + str(y) + '_PS' + str(x) +'_I-V_plot.eps',format='eps')
        x = x + 1
    y = y + 1 




