# Автор: Д. Муфаззалов

import time
m=2022
start_time = time.time()
d = [2]
z = {2: 1}
for i in range(3, m + 1, 2):
    for k in d:
        if k * k > i or i % k == 0:
            break
    if k * k > i: d.append(i)
    z[i] = len(d)
r = list(z.keys())
j = -1
k = 0
for i in range(m, 0, -1):
    if sum(list(map(int, str(i)))) % 22 == 0:
        if z[r[j]] % 2:
            print(i, z[r[j]])
            k += 1
            if k == 5: break
    if i == r[j]:
        j -= 1
print(time.time() - start_time)
