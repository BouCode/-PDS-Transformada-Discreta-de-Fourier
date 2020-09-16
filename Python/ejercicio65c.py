import dft_01
import numpy as np
import matplotlib.pyplot as plt 
import math
from scipy import signal 

if __name__ == "__main__":
    N = 400
    M = 350
    Fs = 8000
    f1 = 200
    f2 = 250
    ti = np.linspace (0, M, num = M )/ Fs
    t = np.transpose (ti)
    x = np.cos (2 * math.pi * f1 * t) + 0.2 *np.cos (2*math.pi * f2 * t)
    x = np.append (x, np.zeros (N - M))
    x = x * np.hamming (N)
    arr = dft_01.dft(x)
    s = np.absolute (arr)
    s = s / np.max (s)
    fp = Fs * np.linspace (0, N, num = N) / N

    plt.figure (1)
    plt.title ('x[n]')
    plt.plot (x, 'o-', markersize = 4)
    
    new_range = len (s)/2
    plt.figure (2)
    plt.plot (fp[:int (new_range)],s[:int (new_range)], 'o-', markersize = 4, linewidth = 0.5)
    plt.xlabel ('Frecuencia en Hz')
    plt.title ('Magnitud al cuadrado de FFT')
    plt.grid (True)

    plt.figure (3)
    plt.plot (fp[:], s[:], 'o-', markersize = 4, linewidth = 0.5)
    plt.xlabel ('Frecuencia en Hz')
    plt.axis ([0, 1000, 0, 1])
    plt.title ('Vista detallada')
    plt.grid (True)
    plt.show ()