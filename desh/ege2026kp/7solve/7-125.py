from math import ceil

a, b = 20000, 7600
px = 0.65
K = a*b/px**2
I = K / 2**20
print( ceil(I) )
