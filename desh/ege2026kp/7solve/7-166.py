from math import ceil, log2

K = 3840*2160
i = ceil( log2(2**24) )
V = 8*1024*1024*1024
C = 128
Nlast = 25

I = ceil( (K*i)/8 )
N1 = int( V / I )

N = N1*(C-1) + Nlast

print( N )
