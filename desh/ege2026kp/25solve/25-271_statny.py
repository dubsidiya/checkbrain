# Автор: Д. Статный

import time

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0 and i%7==0:
            d.add(i)
        if x%i==0 and (x//i)%7==0:
            d.add(x//i)
    return sorted(d)

def mx(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

st = time.time()
count, ans = 0, []
for x in range(14285715, 142857143):
    x = x*7
    if len(div(x))==15:
        ans.append([x, mx(x)[-1]])
        count += 1
    if count == 5:
        count = 0
        break
for x in range(142857142, 14285715, -1):
    x = x*7
    if len(div(x))==15:
        ans.append([x, mx(x)[-1]])
        count += 1
    if count == 5:
        count = 0
        break
for x in sorted(ans):
    print(x[0], x[1])
print(time.time()-st)


