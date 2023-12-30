import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.optimize import curve_fit
from scipy import interpolate
from scipy.signal import savgol_filter
import sys
import matplotlib as mpl
sys.path.append('/Production_of_UV_Photosensor_and_current_readout_circuit')
from filter import fft_filter

#image settings
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

response = []
time = []
signal = []    

# extraction of the data
data1 = np.genfromtxt(f'scope_0.csv',comments = '#',skip_header = 3,delimiter = ',')
                                                             
time1 = data1[:,0] 
signal1 = data1[:,2]

time.append(time1)
signal.append(signal1)

R = 40e6
    
time = np.array(time)        
current = -np.array(signal)/R
    
time = time[~np.isnan(current)]
current = current[~np.isnan(current)]
    

current = fft_filter(current,50,time[1]-time[0])
currentf = savgol_filter(current,201,1)

# to center the data
a = 0.40
k = np.argwhere((time>a) & (time< a+0.20)).flatten()
    
timen = time[k]-a
currentn = currentf[k]
currentn2 = current[k]
  
# To find the 90% and 10% of the difference between on and off signal      
maxv = np.max(-currentn)
minv = np.min(-currentn)
diff = maxv-minv
    
 
val10 = minv + 0.1*diff
val90 = minv + 0.9*diff
print(val90,val10)
for i in range(0,len(currentn)):
    if -currentn[i] < val90:
        c = i
        break
        
for i in range(0,len(currentn)):
    if -currentn[i] < val10:
        d = i
        break    
    
plt.plot(timen*1000,-currentn2,'o',markersize=1)    
plt.plot(timen[c]*1000,-currentn[c],'bx',label='90% of difference')    
plt.plot(timen[d]*1000,-currentn[d],'rx',label='10% of difference')

   
plt.xlabel('Time $t$ (ms)')
plt.ylabel('Output current $I$ (A)')    
responsen = timen[d]-timen[c]
finaltext = "Response time down = {:.2f} milliseconds".format(responsen*1000) 
print(np.abs(responsen*1000),"ms") 
plt.legend(fontsize=5,loc='upper right')
plt.tight_layout()

plt.savefig('plot_batch1_ps_response_time_up.png')