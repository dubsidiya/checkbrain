from math import ceil
V = 150*2**10
N = 5200
L = 30
Ibytes = int(V / N)
i = int(Ibytes*8 / L)
M = 2**i
print( M - 2*26 - 10 )
