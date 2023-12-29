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

data1 = np.genfromtxt(f'scope_0.csv',comments = '#',skip_header = 3,delimiter = ',')
data2 = np.genfromtxt(f'scope_1.csv',comments = '#',skip_header = 3,delimiter = ',')                     
data3 = np.genfromtxt(f'scope_2.csv',comments = '#',skip_header = 3,delimiter = ',')  
data4 = np.genfromtxt(f'scope_3.csv',comments = '#',skip_header = 3,delimiter = ',')
                                    
                         
time1 = data1[:,0] 
signal1 = data1[:,2]

time2 = data2[:,0] 
signal2 = data2[:,2]

time3 = data3[:,0] 
signal3 = data3[:,2]

time4 = data4[:,0] 
signal4 = data4[:,2]


time.append(time1+500)
time.append(time2+1000)
time.append(time3+1500)
time.append(time4+2000)


signal.append(signal1)
signal.append(signal2)
signal.append(signal3)
signal.append(signal4)


R = 10e6
    
time = np.array(time)        
current = np.array(signal)/R
    
time = time[~np.isnan(current)]
current = current[~np.isnan(current)]
    

current = fft_filter(current,50,time[1]-time[0])
currentf = savgol_filter(current,101,1)
    
        
maxv = np.max(-currentf)
minv = np.min(-currentf)
diff = maxv-minv
    
 
val10 = minv + 0.1*diff
val90 = minv + 0.9*diff
    
for i in range(0,len(currentf)):
    if -currentf[i] < val90:
        c = i
        break
        
for i in range(0,len(current)):
    if -currentf[i] < val10:
        d = i
        break    
    
plt.plot(time/60,-current,'o',markersize =1)
plt.plot(time[c]/60,-currentf[c],'bx',label='90% of the difference')    
plt.plot(time[d]/60,-currentf[d],'rx',label='10% of the difference')
plt.xlabel('Time $t$ (mins)')
plt.ylabel('Output Current $I$ (A)')
plt.legend(fontsize=5)
responsen = time[d]-time[c]  
finaltext = "Response time down = {} mins".format(responsen/60) 
print(np.abs(responsen)/60,"mins") 
plt.tight_layout()
plt.savefig('plot_batch4_sp4_ps2_response_time_down.png')