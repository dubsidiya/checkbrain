# Автор: Д. Муфаззалов

import time

start_time = time.time()
n = 2022_2022
a = [0, 0] + [1] * (n - 1) + [0]
i = 1
while i <= n:
    while a[i] == 0 and i < n: i += 1
    if a[i]:
        for j in range(2 * i, n + 1, i): a[j] = 0
    i += 1
k = 0
z = sum(a)
for i in range(n, 0, -1):
    if z % 2022 == 0 and sum(list(map(int, str(i)))) % 22 == 0:
        k += 1
        print(i, z)
        if k == 5:
            break
    z -= a[i]
print(time.time() - start_time)
