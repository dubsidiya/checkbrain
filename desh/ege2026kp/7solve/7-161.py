from math import ceil, log2

K = 3614*2409
i = 16
V = 8*1024*1024*1024
N = 3100

I = ceil(K*i/8)
n1 = V // I

nLast = N % n1

print( nLast )
