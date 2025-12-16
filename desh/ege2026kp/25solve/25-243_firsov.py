def factorization(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
          return [div] + factorization(n // div)
    return [n]

def progression(n):
    n = sorted(list(set(factorization(n))))
    if len(n) <= 3:
        return (False, 0)
    d = n[1]- n[0]
    if d == 0: return (False, 0)
    return (all(n[i] - n[i - 1] == d for i in range(1, len(n))), d * len(n))

for i in range(100_000, 500_000+1):
    b, pr = progression(i)
    if b: print(*[i, pr])

