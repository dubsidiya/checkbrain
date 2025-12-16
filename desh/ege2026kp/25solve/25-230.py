# Автор: Д. Муфаззалов

import time

start_time = time.time()
z = {}
n = 2
m = 14
t = 1
for i in range(1, n):
    t *= i
for j in range(n, m + 1):
    t *= j
    i = 2
    k = 0
    p = t
    while p > 1:
        if p % i == 0:
            k += 1
            while p % i == 0:
                p //= i
        i += 1
    if k % 2:
        z[j] = k
for i in list(z.keys())[-5:]:
    print(i, z[i])
print(time.time() - start_time)
