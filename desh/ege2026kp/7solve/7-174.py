t = 1.5*60
k = 2
Npixels = 3840*2160*60*t
Isound = 48000*16*t*k
I = 54691875*1024*8
Iimage = I - Isound
i = int(Iimage / Npixels)
print( 2**i )