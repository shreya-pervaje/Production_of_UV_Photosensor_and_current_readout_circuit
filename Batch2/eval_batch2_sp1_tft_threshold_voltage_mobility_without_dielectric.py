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


U_Gate, I_Drain = np.genfromtxt("SP1_Batch2_10u_10u_TFT_Measurement1.txt", delimiter= '\t', unpack = True) 


difx = np.diff(U_Gate)
dify = np.diff(np.sqrt(np.abs(I_Drain)))
steigung = np.divide(dify, difx)

maxV = np.max(steigung)
maxvalue = np.argmax(steigung)

a = [U_Gate[maxvalue], U_Gate[maxvalue + 1]]
b = [np.sqrt(np.abs(I_Drain[maxvalue])), np.sqrt(np.abs(I_Drain[maxvalue + 1]))]

popt, _ = curve_fit(linear, a, b)

U_TH = -popt[1] / popt[0]
Mobility = 2 * I_Drain[maxvalue] / (U_Gate[maxvalue] - U_TH) ** 2 * L / (C * W) * 10000

Mobility_Array = np.append(Mobility_Array,Mobility)
U_TH_Array = np.append(U_TH_Array, U_TH)

plt.plot(U_Gate,np.abs(I_Drain),'b-',label='$V_\mathrm{DS} = 10 \, \mathrm{V}$')

# print(I_Drain[0])

print(Mobility_Array)
print(U_TH_Array)

plt.xlabel('Voltage $V_\mathrm{GS}$ (V)')
plt.ylabel('Current $I_\mathrm{D}$ (A)')
plt.yscale('log')
plt.xlim(-20.2,20.2)
plt.tight_layout()
plt.legend()
plt.savefig('Eval_batch2_SP1_TFT_threshold_voltage_mobility_without_dielectric.png')