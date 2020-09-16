import dft_01
import numpy as np
import matplotlib.pyplot as plt 
import math

if __name__ == "__main__":
    f1 = 40
    f2 = 140
    fs = 200
    Ts = 1/fs 
    n = np.linspace (0, 0.50, num = 200)
    x = np.cos (2 * math.pi * f1 * n) + 0.5 * np.cos (2 * math.pi * f2 * n)
    N = len (x)
    X = dft_01.dft (x)
    Xabs = np.absolute (X)
    Xmax = np.max (np.absolute (X))

    plt.figure (1)
    plt.stem (x)
    plt.xlabel (f'{Ts} segundos entre muestra y muestra')
    plt.title ('Muestras de x(t)')

    plt.figure (2)
    plt.stem (np.absolute (X))
    plt.xlabel (f'La resolucion de frecuencia es de {fs/(len (X) - 1)} Hz entre muestras')
    plt.title ('Modulo de la DFT de x')
    plt.show ()