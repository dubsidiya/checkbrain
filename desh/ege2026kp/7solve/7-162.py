from math import ceil, log2

K = 1920*1080
i = ceil( log2(2**16) )
V = 4*1024*1024*1024
N = 5915000

I = ceil( (K*i)/8 )
N1 = int( V / I )

C = ceil( N/N1 )
print( C )
