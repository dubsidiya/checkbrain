V = 3*2**23
W, H = 1600, 1200
iColor = 10 # 2**10 = 1024

i = int(V*1.2 / (W*H))

print( i - iColor )