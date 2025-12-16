# Автор: К. Багдасарян

from math import prod
def divsMultiplicity(n):
    factors = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d,0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n,0) + 1
    return factors


count = 0
n = 5_200_001
while count < 5:
    result = divsMultiplicity(n)
    total_div = prod(x+1 for x in result.values())
    if sum(result.values()) == 9 and total_div % 90 == 0:
        print(n, max(result))
        count += 1
    n += 1
