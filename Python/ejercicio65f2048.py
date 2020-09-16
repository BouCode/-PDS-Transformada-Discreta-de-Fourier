import dft_01
import numpy as np
import matplotlib.pyplot as plt 
import math
from time import time

if __name__ == "__main__":
    start_time = time ()
    N = 2048
    M = 350
    Fs = 8000
    f = 250
    ti = np.linspace (0, M, num = M )/ Fs
    t = np.transpose (ti)
    x = np.cos (2 * math.pi * f * t)
    x = np.append (x, np.zeros (N - M))
    x = x * np.kaiser (N, beta = 0)
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
    elapsed_time = time () - start_time
    print (f'Tiempo de ejecucion {elapsed_time}')