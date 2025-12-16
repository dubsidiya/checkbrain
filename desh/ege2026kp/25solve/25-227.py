# Автор: Д. Муфаззалов

import time

start_time = time.time()
n, m = 2022, 10
k = 0
for i in range(n - 1 + n % 2, 0, -2):
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0: break
    if i % j == 0 and j > m:
        k += 1
        print(i, j)
        if k == 5:
            break
print(time.time() - start_time, 'sec')
