import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.optimize import curve_fit
from scipy import interpolate
from scipy.signal import savgol_filter
import sys
import matplotlib as mpl

cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=300)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 9,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)

def fft_filter(
    s: np.ndarray, freqs: float, dt: float, df: float = 0.25
) -> np.ndarray:
    """Filters out frequency contributions from a signal

    Args:
        s (np.ndarray): Signal that schould be filtered
        freqs (Union[float, List[float]]): Frequency(ies) that should be filtered out
        dt (float): Time steps of the provided signal
        df (float, optional): Frequency range around each
            frequency that should be cut out. Defaults to 0.25.

    Returns:
        np.ndarray: Filtered signal
    """
    fft = sc.fft.fft(s)
    fftfreq = sc.fft.fftfreq(fft.shape[0], d=dt)

    # filter both f and -f
    try:
        freqs = np.array(list(set(np.abs(freqs))))
    except Exception:
        freqs = np.array([np.abs(freqs)])
    freqs = np.concatenate((-freqs, freqs))

    for f in freqs:
        rng = np.logical_and(fftfreq > f - df, fftfreq < f + df)
        fft[rng] = 0

    sf = np.real(sc.fft.ifft(fft))
    return sf


response = []
time = []
signal = []    

data1 = np.genfromtxt(f'scope_5.csv',comments = '#',skip_header = 3,delimiter = ',')
data2 = np.genfromtxt(f'scope_6.csv',comments = '#',skip_header = 3,delimiter = ',')                     
data3 = np.genfromtxt(f'scope_7.csv',comments = '#',skip_header = 3,delimiter = ',')  
data4 = np.genfromtxt(f'scope_8.csv',comments = '#',skip_header = 3,delimiter = ',')
data5 = np.genfromtxt(f'scope_9.csv',comments = '#',skip_header = 3,delimiter = ',')
data6 = np.genfromtxt(f'scope_10.csv',comments = '#',skip_header = 3,delimiter = ',')     
data7 = np.genfromtxt(f'scope_11.csv',comments = '#',skip_header = 3,delimiter = ',')    
data8 = np.genfromtxt(f'scope_12.csv',comments = '#',skip_header = 3,delimiter = ',')                             
                         
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

time.append(time1+500)
time.append(time2+1000)
time.append(time3+1500)
time.append(time4+2000)
time.append(time5+2500)
time.append(time6+3000)
time.append(time7+3500)
time.append(time8+4000)

signal.append(signal1)
signal.append(signal2)
signal.append(signal3)
signal.append(signal4)
signal.append(signal5)
signal.append(signal6)
signal.append(signal7)
signal.append(signal8)

R = 10e6
    
time = np.array(time)        
current = np.array(signal)/R
    
time = time[~np.isnan(current)]
current = current[~np.isnan(current)]
    

current = fft_filter(current,50,time[1]-time[0])
currentf = savgol_filter(current,301,1)
        
maxv = np.max(-currentf)
minv = np.min(-currentf)
diff = maxv-minv
    
 
val10 = minv + 0.1*diff
val90 = minv + 0.9*diff
    
for i in range(0,len(currentf)):
    if -currentf[i] > val90:
        c = i
        break
        
for i in range(0,len(currentf)):
    if -currentf[i] < val10:
        d = i
        break    
    
plt.plot(time/60,-current,'o',markersize=1)
plt.plot(time[c]/60,-currentf[c],'bx',markersize='6',label='90% of the difference')    
plt.plot(time[d]/60,-currentf[d],'rx',markersize='6',label='10% of the difference')
responsen = time[d]-time[c] 

plt.xlabel('Time $t$ (mins)')
plt.ylabel('Output Current $I$ (A)')    
print(np.abs(responsen)/60,"mins") 
plt.legend(fontsize=5)
plt.tight_layout()
plt.savefig('plot_batch4_sp4_ps2_response_time_up.png')