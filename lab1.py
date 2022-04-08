import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

t=np.arange(0,7,0.02)
freqs=[1, 3]
amps=[1, 0.5]
phis=[-np.pi/2, np.pi/6]

signal_total = 0

for (freq, amp, phi) in zip(freqs,amps,phis):
    omega=2*np.pi*freq
    signal=amp*np.cos(omega*t+phi)
    signal_total += signal
    plt.plot(t,signal, label=f'{freq} Hz')
    
peaks, _ = sp.find_peaks(signal_total, height=0,prominence=True)
max_peak = max(signal_total[peaks])
#print(max_peak)
first_peak = 0
second_peak = 0
for i in range(len(peaks)):
    print(signal_total[peaks[i]])
    if abs(signal_total[peaks[i]] - max_peak) < 0.001:
        if first_peak == 0:
            first_peak = peaks[i]
        else:
            second_peak = peaks[i]
            break
period = (second_peak - first_peak)*0.02
print(period)
#print(signal_total[peaks])
new_freq = 1/period
plt.plot(t,signal_total,label=f'{"{0:.2f}".format(new_freq)} Hz')
plt.legend()
plt.show()
