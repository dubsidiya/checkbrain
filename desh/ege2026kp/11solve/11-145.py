from math import ceil, log2
M = 2030 + 10
i = ceil(log2(M))
I = 67*1024
ib = ceil((67*1024+1) / 318)
print( ib )
L = ceil( ((ib-1)*8+1) / i )
print( L )

