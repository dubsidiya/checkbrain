from math import ceil, log2

M = 10 + 26 + 8164
i = ceil( log2(M) )

N = 835
V = 156*2**10

bNumber = ceil( V / N )
L = ceil( bNumber*8 / i )

print( L )

bNumber = ceil( L*i/8 )
print( (bNumber * N) / 2**10 )

L -= 1
bNumber = ceil( L*i/8 )
print( (bNumber * N) / 2**10 )

