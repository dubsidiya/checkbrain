from math import ceil
V = 190*2**10
N = 5600
L = 25
Ibytes = int(V / N)
i = int(Ibytes*8 / L)
M = 2**i
print( M - 2*26 - 10 )
