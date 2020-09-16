import math

def dft (x):
    arr = []
    XSize = len (x)
    for m in range (0, XSize):
        sum = 0
        for n in range (0, XSize):
            sum = sum + x [n] * complex (math.cos (2 * math.pi* n * m / XSize), - math.sin (2 * math.pi * n * m/XSize))
        arr.append(sum)
    return arr

