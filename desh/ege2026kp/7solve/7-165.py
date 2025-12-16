from math import ceil, log2

K = 1280*1024
i = ceil( log2(256) )
V = 4*1024*1024*1024
C = 35
Nlast = 307

I = ceil( (K*i)/8 )
N1 = int( V / I )

N = N1*(C-1) + Nlast

print( N )
