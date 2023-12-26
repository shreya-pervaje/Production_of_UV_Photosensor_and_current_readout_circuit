import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
#import xlrd
import os
import sys

def linear(x, a, b):
    return a * x + b

AnzahlTransistorenInSerienmessung = 4

colors = ['blue','red','yellow','green']
dataname = 'DarkCurrent_vs_OxygenConc.xlsx'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1],engine='openpyxl')

        
I_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0],engine='openpyxl')

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]

plt.plot(U_Drain,np.abs(I_Drain),color = colors[0],label = '9% Oxygen')
#plt.show()
#sys.exit()
j = 1
while j < AnzahlTransistorenInSerienmessung:
    appends = "Append" + str(j)
    j = j + 1

    U_Gate = pd.read_excel(dataname, sheet_name=appends, usecols=[1],engine='openpyxl')

    I_Drain = pd.read_excel(dataname, sheet_name=appends, usecols=[0],engine='openpyxl')

    U_Gate = np.array(U_Gate.T)[0]
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
#plt.show()
#plt.savefig('plot.png')
#plt.title(dataname)

