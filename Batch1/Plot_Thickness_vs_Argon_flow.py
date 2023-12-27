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

meanT = [130.4,106.3,95.75,87.7]
oxygen = [9,18,24,30]    
argon = [75, 67.5, 62.5, 57.5]    
plt.plot(argon,meanT,'o')
   
plt.xlabel('Argon flow (ml/min)')
plt.ylabel('Thickness a-IGZO $h$ (nm)')

#plt.legend()
#plt.yscale('log')
#plt.show()
plt.savefig('Thickness vs Argon Flow.png')
#plt.title(dataname)

