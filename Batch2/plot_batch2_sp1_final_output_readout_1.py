
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.optimize import curve_fit
from scipy import interpolate
from csaps import csaps
from scipy.signal import savgol_filter
import sys
import matplotlib as mpl

#image settings
savePlot = True
cm = 1/2.54
plt.figure(figsize= (7.3*cm,5*cm),dpi=600)
settings = {"xtick.labelsize": 6,
            "ytick.labelsize": 6,
            "font.size": 7,
            "legend.fontsize": 6,
            "font.family":['Arial']
            }
mpl.rcParams.update(settings)
savePlot = True

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

p0 = [1.64e-9,230,7.63e-10]

response = []

data = np.genfromtxt('scope_0.csv',comments = '#',skip_header = 3,delimiter = ',')
time = data[:,0] 
inpsignal = data[:, 4]
signal1 = data[:, 3]

    
time = time[~np.isnan(signal1)]
inpsignal = inpsignal[~np.isnan(signal1)]
signal1 = signal1[~np.isnan(signal1)]
signal1 = savgol_filter(signal1,11,3)
signal1 = fft_filter(signal1,50,time[1]-time[0])
    

plt.plot(time,inpsignal,'b-', label="Input Signal")
plt.plot(time,signal1,'r-', label="Output Signal")
plt.ylabel('Voltage $V$ (V)')
plt.xlabel('Time $t$ (s)')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Plot_batch2_SP1_final_output_readout1.png')


