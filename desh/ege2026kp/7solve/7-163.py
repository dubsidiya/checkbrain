from math import ceil, log2

K = 3840*2160
i = ceil( log2(2**24) )
V = 8*1024*1024*1024
N = 5922

I = ceil( (K*i)/8 )
N1 = int( V / I )

C = ceil( N/N1 )
print( C )
