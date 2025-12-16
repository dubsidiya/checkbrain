# Автор: Л. Шастин

prime = lambda x: all(x%j != 0 for j in range(2, int(x**0.5) + 1))

k = 0
n = (100_000_000) // 2 + 1
while k < 5:
    if prime(n):
        print(2*n, n)
        k += 1
    n += 1