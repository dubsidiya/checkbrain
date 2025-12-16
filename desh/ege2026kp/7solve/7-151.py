from math import ceil, log2
K = 1024 * 768
M = 1024
i = ceil(log2(M))
P = 180
v = 200*1024*8
tMax = 6*60

I = K*i*P
t = I / v
print( round((1 - tMax / t)*100)  )

