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

data1 = np.genfromtxt(f'scope_0.csv',comments = '#',skip_header = 3,delimiter = ',')
data2 = np.genfromtxt(f'scope_1.csv',comments = '#',skip_header = 3,delimiter = ',')                     
data3 = np.genfromtxt(f'scope_2.csv',comments = '#',skip_header = 3,delimiter = ',')  
data4 = np.genfromtxt(f'scope_3.csv',comments = '#',skip_header = 3,delimiter = ',')
data5 = np.genfromtxt(f'scope_4.csv',comments = '#',skip_header = 3,delimiter = ',')
data6 = np.genfromtxt(f'scope_5.csv',comments = '#',skip_header = 3,delimiter = ',')
data7 = np.genfromtxt(f'scope_6.csv',comments = '#',skip_header = 3,delimiter = ',') 
data8 = np.genfromtxt(f'scope_7.csv',comments = '#',skip_header = 3,delimiter = ',')
data9 = np.genfromtxt(f'scope_8.csv',comments = '#',skip_header = 3,delimiter = ',')  
data10 = np.genfromtxt(f'scope_9.csv',comments = '#',skip_header = 3,delimiter = ',')                                    
                         
time1 = data1[:,0] 
signal1 = data1[:,2]

time2 = data2[:,0] 
signal2 = data2[:,2]

time3 = data3[:,0] 
signal3 = data3[:,2]

time4 = data4[:,0] 
signal4 = data4[:,2]

time5 = data5[:,0] 
signal5 = data5[:,2]

time6 = data6[:,0] 
signal6 = data6[:,2]

time7 = data7[:,0] 
signal7 = data7[:,2]

time8 = data8[:,0] 
signal8 = data8[:,2]

time9 = data9[:,0] 
signal9 = data9[:,2]

time10 = data10[:,0] 
signal10 = data10[:,2]

time.append(time1+500)
time.append(time2+1000)
time.append(time3+1500)
time.append(time4+2000)
time.append(time5+2500)
time.append(time6+3000)
time.append(time7+3500)
time.append(time8+4000)
time.append(time9+4500)
time.append(time9+5000)

signal.append(signal1)
signal.append(signal2)
signal.append(signal3)
signal.append(signal4)
signal.append(signal5)
signal.append(signal6)
signal.append(signal7)
signal.append(signal8)
signal.append(signal9)
signal.append(signal10)

R = 10e6
    
time = np.array(time)        
current = np.array(signal)/R
    
time = time[~np.isnan(current)]
current = current[~np.isnan(current)]
    

current = fft_filter(current,50,time[1]-time[0])
currentf = savgol_filter(current,201,1)
        
maxv = np.max(-currentf)
minv = np.min(-currentf)
diff = maxv-minv
    
 
val10 = minv + 0.1*diff
val90 = minv + 0.9*diff
    
for i in range(0,len(currentf)):
    if -currentf[i] < val90:
        c = i
        break
        
for i in range(0,len(currentf)):
    if -currentf[i] < val10:
        d = i
        break    
    
plt.plot(time/60,-current,'o',markersize =1)
plt.plot(time[c]/60,-current[c],'bx',  markersize=6, label='90% of the diff.')    
plt.plot(time[d]/60,-current[d],'rx',  markersize=6, label='10% of the diff.')
plt.xlabel('Time $t$ (mins)')
plt.ylabel('Output Current $I$ (A)')
plt.legend()
responsen = time[d]-time[c]  
finaltext = "Response time down = {} mins".format(responsen/60) 
print(np.abs(responsen)/60,"mins") 
plt.tight_layout()
plt.savefig('plot_batch3_ps_100um_10um_response_time_down_tempered.png')