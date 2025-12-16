from math import ceil, log2
K = 1080*920*0.8
b = int(3*8*1024*1024 / K)
print( b )
iColor = ceil(log2(1_000_000))
print( iColor )
print( b - iColor )
print( 2**(b - iColor) )