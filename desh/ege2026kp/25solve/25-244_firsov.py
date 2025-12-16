# Автор: М. Фирсов

def pro(n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result

def factorization(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0: return [div] + factorization(n // div)
    return [n]

def Q(n):
    factors = factorization(n)
    return int(str(sum(factors))[::-1]) + pro(factors[1:])
cnt = 0; n = 0
while cnt != 5:
    n += 1; q = Q(n)
    if q + n > 202122: print(n, q); cnt += 1
