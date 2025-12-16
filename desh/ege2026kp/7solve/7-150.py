from math import ceil, log2
K = 1280 * 720
M = 256
i = ceil(log2(M))
P = 140
v = 120*1024*8
tMax = 12*60

I = K*i*P
t = I / v
print( round((1 - tMax / t)*100)  )

