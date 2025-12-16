# Автор: Д. Статный

from math import *

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

def p(m):
    u = div(m)
    if len(div(m))>=3:
        return gcd(u[0], u[1])==1 and gcd(u[0], u[2])==1 and gcd(u[1], u[2])==1
    else:
        return False

count = 0
for i in range(100_000_000, 110_000_000):
    if p(i):
        print(i, max(div(i)))
        # print(div(i)[:4])
        count += 1
    if count==7:
        break
