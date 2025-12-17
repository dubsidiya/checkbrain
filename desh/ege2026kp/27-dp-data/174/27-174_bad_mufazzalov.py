# Автор Д.Ф. Муфаззалов

with open('27.txt') as f:
    k, k = map(int, f.readline().split())
    c = sorted([list(map(int, i.split())) for i in f])
    a, ans= [], []
    [a.extend([i] * j) for i, j in c]
from heapq import nsmallest
m = (max(a) - min(a)) * len(a)
for i, p in enumerate(a):
    b = a[:i] + a[i + 1:]
    dist = sum([abs(p - j) for j in nsmallest(k, b, key=lambda x: abs(x - p))])
    if dist < m:
        m, d = dist, set()
    if dist == m: d.add(a[i])
print(max(d) - (0 if len(d) == 1 else min(d)))
