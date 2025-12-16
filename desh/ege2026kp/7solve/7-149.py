from math import ceil, log2
K = 1920 * 1080
M = 2048
i = ceil(log2(M))
P = 80
v = 150*1024*8
tMax = 15*60

I = K*i*P
t = I / v
print( round((1 - tMax / t)*100)  )

