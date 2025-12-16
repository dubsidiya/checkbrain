# Автор: М. Ишимов

from fnmatch import *

def mask(x): return fnmatch(str(x), '1*2*7*04')

def divisors(n):
    count = mx = 0
    for d in range(2, int(n**0.5)):
        if n % d == 0:
            if count == 0: mx = n // d
            count += 2
            if count > 42: return (0,0)
    return (count, mx)

k = 0
n = 10**9 + 4
while k != 5:
    if int(n **.5) == n ** .5:
       if mask(n):
        delit = divisors(n)
        if delit[0] == 42:
            print(n, delit[1])
            k += 1
    n += 100
