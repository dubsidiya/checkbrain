from math import ceil, log2

K = 3840*2160
i = ceil( log2(65536) )
i *= 2
V = 8*1024*1024*1024
C = 3
Nlast = 45

I = ceil( (K*i)/8 )
N1 = int( V / I )

N = N1*(C-1) + Nlast

print( N )

print( ceil(N/10) )
