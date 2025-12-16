# Автор: М. Ишимов

from fnmatch import *

def divisors(n):
    count = mx = 0
    for d in range(2, int(n**0.5)):
        if n % d == 0:
            if count == 0: mx = n // d
            count += 2
            if count > 6: return (0,0)
    return (count, mx)

def mask(x): return fnmatch(str(x), '15*3*09')

for n in range(9,10**9, 100):
    if int(n ** .5) == n ** .5:
       if mask(n):
        delit = divisors(n)
        if delit[0] == 6:
            print(n, delit[1])
