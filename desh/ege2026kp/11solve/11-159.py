from math import ceil, log2

N = 1016
M = 26*2 + 10 + 50*5
i = ceil( log2(M) )
I = ceil( (N*i)/8 )
print( I )