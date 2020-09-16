import matplotlib.pyplot as plt
import numpy as np
import math 
import dft_01 
import idft_01 

if __name__ == "__main__":
    
    Omega = math.pi/4
    N = 20
    n = np.linspace (0, N, num = N+1)
    x = np.cos (Omega * n)
    X = dft_01.dft (x)
    f = idft_01.idft (X)

    plt.figure (1)
    plt.stem (x)
    plt.grid (True)
    plt.title ("Muestra de x(t)")
    plt.ylabel ('Amplitud')
    plt.xlabel ('Muestras')

    plt.figure (2)
    plt.stem (np.absolute (X))
    plt.grid (True)
    plt.title ("Modulo de la DFT de x")
    plt.ylabel ('Amplitud')
    plt.xlabel ('Muestras')
    
    plt.figure (3)
    plt.stem (f)
    plt.grid (True)
    plt.title ("IFFT")
    plt.ylabel ('Amplitud')
    plt.xlabel ('Muestras')
    
    plt.show()
