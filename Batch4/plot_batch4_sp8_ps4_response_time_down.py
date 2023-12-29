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

data1 = np.genfromtxt(f'scope_6.csv',comments = '#',skip_header = 3,delimiter = ',')
                                     
                         
time1 = data1[:,0] 
signal1 = data1[:,2]


time.append(time1)
signal.append(signal1)

R = 20e6
    
time = np.array(time)        
current = np.array(signal)/R
    
time = time[~np.isnan(current)]
current = current[~np.isnan(current)]
    

current = fft_filter(current,50,time[1]-time[0])
currentf = savgol_filter(current,11,1)
a = 0.35
k = np.argwhere((time>a) & (time< a+0.35)).flatten()
    
timen = time[k]-a
currentn = currentf[k]
currentn2 = current[k]
        
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
    
plt.plot(timen*1000,-currentn2,'o')    
plt.plot(timen[c]*1000,-currentn[c],'bx')    
plt.plot(timen[d]*1000,-currentn[d],'rx')

    
plt.xlabel('Time $t$ (ms)')
plt.ylabel('Output current(I)')    
responsen = timen[d]-timen[c]
finaltext = "Response time down = {:.2f} milliseconds".format(responsen*1000) 
print(np.abs(responsen*1000),"ms") 
plt.tight_layout()
plt.show()
plt.savefig('plot_batch4_sp8_ps4_response_time_down.png')