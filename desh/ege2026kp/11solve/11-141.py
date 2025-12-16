from math import ceil, log2

M = 10 + 52 + 458
i = ceil( log2(M) )

bNumber = int( 276*2**10 / 862 )

print( bNumber*8 // i )