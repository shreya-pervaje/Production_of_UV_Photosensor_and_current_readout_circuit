import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import constants
from scipy.signal import savgol_filter
import pandas as pd
import xlrd
import os
import sys
import matplotlib as mpl


def linear(x, a, b):
    return a * x + b
# Einstellungen
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

Mobility_Array = []
U_TH_Array = []

AnzahlTransistorenInSerienmessung = 1
# Konstanten angeben
e0 = constants.epsilon_0
er = 4
d = 130 * 10 ** (-9)
W = 10 * 10 ** (-6)
L = 10 * 10 ** (-6)
C = e0 * er / d



U_Gate, I_Drain = np.genfromtxt("Batch4_SP3_TFT_Final3.txt", delimiter= '\t', unpack = True) 

I_Drain = savgol_filter(I_Drain,11,1)

difx = np.diff(U_Gate)
dify = np.diff(np.sqrt(np.abs(I_Drain)))



steigung = dify/difx
steigung = np.append(steigung,steigung[-1])



maxV = np.max(steigung)

maxvalue = np.argmax(steigung)
a = [U_Gate[maxvalue-1], U_Gate[maxvalue + 1]]
b = [np.sqrt(np.abs(I_Drain[maxvalue-1])), np.sqrt(np.abs(I_Drain[maxvalue + 1]))]


popt, _ = curve_fit(linear, a, b)

U_TH = -popt[1] / popt[0]

Mobility = 2 * I_Drain[maxvalue] / (U_Gate[maxvalue] - U_TH) ** 2 * L / (C * W) * 10000

plt.plot(U_Gate,np.abs(I_Drain),'b-',label='$V_\mathrm{DS} = 10 \, \mathrm{V}$')

print(Mobility)
print(U_TH)

plt.xlabel('Voltage $V_\mathrm{GS}$ (V)')
plt.ylabel('Current $I_\mathrm{DS}$ (A)')
plt.yscale('log')
plt.xlim(-20.2,20.2)
plt.tight_layout()
plt.legend()
plt.savefig('eval_batch4_sp3_tft_threshold_voltage_mobility.png')
