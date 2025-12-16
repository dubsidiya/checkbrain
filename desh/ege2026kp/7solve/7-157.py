from math import ceil, log2

K = 3840*2160
i = 24
V = 16*1024*1024*1024
N = 3742

I = ceil(K*i/8)
n1 = V // I

nLast = N % n1

print( nLast )
