from math import ceil, log2
K = 800 * 600
M = 65536
i = ceil(log2(M))
P = 150
v = 100*1024*8
tMax = 10*60

I = K*i*P
t = I / v
print( round((1 - tMax / t)*100)  )

