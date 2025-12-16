# Автор: Д. Статный

import time

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0 and i%2022==0:
            d.add(i)
        if x%i==0 and (x//i)%2022==0:
            d.add(x//i)
    return sorted(d)

st = time.time()

ans = []
for i in range(49455, 49600):
    x = 2022*i
    if len(div(x))==7:
        ans.append([x, x//2])
for i in range(98700, 98911+2):
    x = 2022*i
    if len(div(x))==7:
        ans.append([x, x//2])
for x in ans[:5]:
    print(x[0], x[1])
for x in ans[-5:]:
    print(x[0], x[1])

print(time.time()-st)
