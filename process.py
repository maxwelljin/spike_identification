import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], analog=False, btype='band', output='sos')
    return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    sos = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sosfilt(sos, data)
    return y

def read_binary(FILE_PATH):
    myarray = np.fromfile(FILE_PATH, dtype=float)
    return myarray[:3000]

median = np.median(array)
arr = read_binary('d533101.dat')
print(arr)