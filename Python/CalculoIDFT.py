import idft_01
import dft_01
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    x = np.array ([7, 4, 3, 9, 0, 1, 5, 2])
    X = dft_01.dft (x)
    XReal = np.real (X)
    XImag = np.imag (X)
    print (f'X: \n{X}')
    x_2 = idft_01.idft (X)
    x_2Real = np.real (x_2)
    x_2Imag = np.imag (x_2)
    print (f'IDFT: \n{x_2}')
    plt.figure (1)
    plt.plot (XReal)
    
    plt.figure (2)
    plt.plot (XImag)

    plt.figure (3)
    plt.plot (x_2Real)
    plt.title ('Valores reales de la IDFT de X')
    print (f" x_2 Reales: {x_2Real}")

    plt.figure (4)
    plt.title ('Valores imaginarios de la IDFT de X')
    plt.plot (x_2Imag)
    print (f"x_2 Imaginarios{x_2Imag}")
    #plt.show()


