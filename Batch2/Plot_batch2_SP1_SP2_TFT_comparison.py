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
settings = {"xtick.labelsize": 5,
            "ytick.labelsize": 5,
            "font.size": 6,
            "legend.fontsize": 3,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)



dataname = 'SP1_10um_10um\SP1_10um_10um_with_dielectric_tempered_Au_IGZO\SP1_Batch2_WithDi_Au_IGZO.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
#print(U_Drain)
#print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'r', label = 'With Dielectric, Tempered, Gold and IGZO deposited')

dataname = 'SP2_10um_10um\SP2_10um_10um_with_Au_IGZO\SP2_Batch2_WithoutDi_WithAu_IGZO.xls'
U_Drain = pd.read_excel(dataname, sheet_name="Data", usecols=[0])        
I_Drain = pd.read_excel(dataname, sheet_name='Data', usecols=[1])
U_Drain = np.array(U_Drain.T)[0]
I_Drain = np.array(I_Drain.T)[0]
# #print(np.max(I_Drain))  
plt.plot(U_Drain,I_Drain,'b', label = 'Without Dielectric, With Gold and IGZO deposited')


plt.yscale('log')
plt.legend()
#plt.ylim(-2.2e-10,5.2e-10)
plt.xlim(-20.2,20.2)
#.title(dataname)
plt.tight_layout()
plt.savefig('plot_batch2_SP1_SP2_TFT_comparison.png')