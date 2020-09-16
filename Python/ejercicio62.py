import dft_01 
import numpy as np
import matplotlib.pyplot as plt 
import math 

if __name__ == "__main__":
    f = 0.4
    Ts = 0.125
    fs = 1/Ts
    n = np.linspace (0, 6, num = int (6/Ts))
    x = np.cos (2 * math.pi * f * n)
    N = len (x)
    X = dft_01.dft (x)
    Xabs = np.absolute (X)
    Xmax = np.max (np.absolute (X))

    plt.figure (1) 
    plt.plot (x, 'o-', markersize = 4)
    plt.xlabel (f'{Ts} segundos entre muestra y muestra')
    plt.title ('Muestra de x(t)')

    plt.figure (2)
    plt.plot (np.absolute (X),'o-', markersize = 4, linewidth = 0)
    plt.xlabel (f'La resolucion de frecuencia es de {fs/(len (X)-1)} Hz entre muestras')
    plt.title ('Modulo de la DFT de x')
    plt.show ()
