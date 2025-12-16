t = 70
k = 4
Iimage = 1920*1080 * 30 * 24 * t
Isound = 48000*24*t*k
I = 1024**4 * 8
print( int(I / (Iimage+Isound) ) )