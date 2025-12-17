# Автор: А. Минак

import itertools

with open('27-188a.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f]
a.sort()
b = []
for i in range(1, n):
    b.append(a[i]-a[i-1])
k = 0
m = float('inf')
for x in itertools.product('01', repeat=n-1):
    r = ''.join(x)
    if r[0]=='1' and r[-1]=='1':
        if '00' not in r:
            s = 0
            for i in range(n-1):
                if r[i] == '1':
                    s += b[i]
            m = min(m, s)
print(m)

