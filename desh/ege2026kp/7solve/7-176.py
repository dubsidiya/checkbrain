t = 5*60
k = 1
Iimage = 1920*1080 * 30 * 16 * t
Isound = 36000*16*t*k
IMb = (Iimage+Isound) / 1024**2 / 8
print( int(IMb) )