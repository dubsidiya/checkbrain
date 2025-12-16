# Автор: Д. Статный

def prime(x):
    return x>1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

def allDivs(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

from math import ceil
i = ceil( 10_000_000**0.5 )
ans = []
while True:
    x = i**2
    if x > 60_000_000: break
    divs = allDivs(x)
    if prime(len(divs)):
       ans.append( (x, len(divs)) )
    i += 1

ans.sort( key = lambda x: (-x[1], x[0]) )

for x in ans[:7]:
    print( *x )