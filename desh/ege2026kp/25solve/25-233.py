# Автор: Д. Муфаззалов

import time
n=5022_2022
start_time = time.time()
a = [0, 0, 1] + [i % 2 for i in range(3, n + 1)]
i = 3
while i ** 2 <= n:
    if a[i]:
        for j in range(i ** 2, n + 1, i * 2):
            a[j] = 0
    i += 2
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
