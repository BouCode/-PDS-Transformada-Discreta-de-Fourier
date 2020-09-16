import dft_01
import numpy as np
import matplotlib.pyplot as plt 
import math

if __name__ == "__main__":
    
    Array_x = np.array([])
    f = 40
    fs = 1000 
    Ts = 1/fs
   
    n = np.linspace (0, 0.5, num = 1000)
    x = np.cos (2*math.pi*f*n)
   
    arr = dft_01.dft (x)
    Array_x = arr
    Xabs = np.absolute (Array_x)
    Xmax = np.max (Array_x)
   
    plt.figure(1)
    plt.title('Muestra de x(t)')
    plt.plot (x, 'o-', markersize = 4)
    plt.xlabel (f'{Ts} Segundos entre muestra y muestra')
   
    plt.figure(2)
    plt.title ('Modulo de la DFT de x')
    plt.plot (np.absolute (Array_x), 'o-', markersize = 2, linewidth = 0)
    plt.xlabel (f'La resolucion de frecuencia es de {fs/(len(Array_x)-1)}Hz entre muestras')
    plt.show()
