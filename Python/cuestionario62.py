import matplotlib.pyplot as plt
import numpy as np
import math 
import dft_01 
import idft_01 

if __name__ == "__main__":
    X = np.array ([3, 2+4j, 1, 5-3j, 0, 0, 0, 5+3j, 1, 2-4j])
    x_2 = idft_01.idft (X)
    x_2Real = np.real (x_2)
    x_2Imag = np.imag (x_2)
    x_2abs = np.absolute (x_2)

    x = x_2
    X = dft_01.dft (x)
    XReal = np.real (X)
    XImag = np.imag (X)
    Xabs = np.absolute (X)
    Xangle = np.angle (X)
    
    plt.figure (1)
    plt.stem (Xabs)
    plt.grid (True)
    plt.title ("DFT")
    plt.ylabel ('Amplitud')
    plt.xlabel ('Muestras')

    plt.figure (2)
    plt.stem (x_2abs)
    plt.grid (True)
    plt.title ("IDFT")
    plt.ylabel ('Amplitud')
    plt.xlabel ('Muestras')

    plt.figure (3)
    plt.stem (Xangle)
    plt.grid (True)
    plt.show ()
