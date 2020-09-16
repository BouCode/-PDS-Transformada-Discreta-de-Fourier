import math
import numpy as np 

def idft (x):
    XSize = len (x)
    arr = np.zeros ((XSize, XSize), dtype=complex)
    new_arr = np.zeros (XSize, dtype=complex)
    for n in range (0, XSize):
        for m in range (0, XSize):
            sum = x[m] * complex (math.cos (2 * math.pi * m * n/ XSize), math.sin (2 * math.pi * m * n / XSize))
            arr[n][m] = sum
    for n in range (0, XSize):
        summ = 0
        for m in range (0, XSize):
            summ = summ + arr[n][m]
        new_arr[n] = summ / XSize 
    return new_arr

