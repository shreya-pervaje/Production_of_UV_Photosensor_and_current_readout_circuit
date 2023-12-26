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
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 5,
            "ytick.labelsize": 5,
            "font.size": 3,
            "legend.fontsize": 3,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

colors = ['blue','red','yellow','green']

#path = '/scratch/spervaje/Third_Batch/Photosensors_Measurements/100um_10um/'
dataname = 'Photosensors_100um_10um.xls'
#os.chdir(path)
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])
     
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]

plt.plot(U_Drain,I_Drain,color = colors[0],label = 'MoTa Photosensor Untempered: light off')


U_Gate = pd.read_excel(dataname, sheet_name="Append5", usecols=[1])

I_Drain = pd.read_excel(dataname, sheet_name="Append5", usecols=[0])

U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]
        
plt.plot(U_Drain,np.abs(I_Drain),color = colors[1],label = 'MoTa Photosensor Untempered: light on')


#path = '/scratch/spervaje/First_Batch_Photosensors/Measurements/spervaje/Characteristics/SP1/'
dataname = 'Photosensors_100um_10um_Tempered.xls'
#os.chdir(path)

U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[1])

        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[0])

U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]


plt.plot(U_Drain,I_Drain,color = colors[2],label = 'MoTa Photosensor tempered: light off')
   
U_Gate = pd.read_excel(dataname, sheet_name="Append5", usecols=[1])

I_Drain = pd.read_excel(dataname, sheet_name="Append5", usecols=[0])

U_Gate = np.array(U_Gate.T)[0]
I_Drain = np.array(np.abs(I_Drain.T))[0]
    
      
plt.plot(U_Drain,np.abs(I_Drain),color = colors[3],label = 'MoTa Photosensor tempered: light on')

#path = '/scratch/spervaje/Comparison/'
#os.chdir(path)
   
plt.xlabel('Voltage $U$ (V)')
plt.ylabel('Current $I$ (A)')

plt.legend()
plt.yscale('log')
plt.tight_layout()
#plt.show()
plt.savefig('plot_TemperedvsUntempered.png')
#plt.title(dataname)

