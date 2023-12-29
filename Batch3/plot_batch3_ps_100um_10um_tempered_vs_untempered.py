import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
import pandas as pd
import os
import sys
import matplotlib as mpl

savePlot = True
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

colors = ['blue','red','yellow','green']


dataname = 'Before_tempering\Photosensors_100um_10um.xls'

U_PS = pd.read_excel(dataname, sheet_name="Data", usecols=[1])     
I_PS = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]

plt.plot(U_PS,I_PS,color = colors[0],label = 'MoTa Photosensor Untempered: light off')


U_PS = pd.read_excel(dataname, sheet_name="Append5", usecols=[1])
I_PS = pd.read_excel(dataname, sheet_name="Append5", usecols=[0])

U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]
        
plt.plot(U_PS,np.abs(I_PS),color = colors[1],label = 'MoTa Photosensor Untempered: light on')


dataname = 'After_tempering\Photosensors_100um_10um_Tempered.xls'


U_PS = pd.read_excel(dataname, sheet_name="Data", usecols=[1])        
I_PS = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]


plt.plot(U_PS,I_PS,color = colors[2],label = 'MoTa Photosensor tempered: light off')
   
U_PS = pd.read_excel(dataname, sheet_name="Append5", usecols=[1])
I_PS = pd.read_excel(dataname, sheet_name="Append5", usecols=[0])

U_PS = np.array(U_PS.T)[0]
I_PS = np.array(np.abs(I_PS.T))[0]
    
      
plt.plot(U_PS,np.abs(I_PS),color = colors[3],label = 'MoTa Photosensor tempered: light on')

   
plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')

plt.legend(fontsize='4')
plt.yscale('log')
plt.tight_layout()
plt.savefig('plot_batch3_PS_100um_10um_tempered_untempered_comparison.png')

