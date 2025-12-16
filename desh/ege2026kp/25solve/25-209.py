# Автор: И. Женецкий

from math import ceil, log2

def prime(n):
    for d in range(2, int(n**0.5)+1):
        if n%d==0:
            return False
    return True

for n in range(99999, 1048571+1):
    if prime(n):
        l = log2(n)
        dvoyka_low = 2**int(l)
        dvoyka_high = 2**ceil(l)
        if any(abs(n - s)<=5 for s in (dvoyka_low, dvoyka_high)):
            print( n, end= " " )
            if abs(n-dvoyka_low) < abs(n-dvoyka_high):
               print( dvoyka_low )
            else:
               print( dvoyka_high )
