# Автор Д.Ф. Муфаззалов

with open('27.txt') as f:
    k, k = map(int, f.readline().split())
    c = sorted([list(map(int, i.split())) for i in f])
    a = []
    [a.extend([i] * j) for i, j in c]
n, d = len(a), set()
m = R = (max(a) - min(a)) * len(a)
for i in range(n):
    dist = R
    for j in range(k, -1, -1):
        if 0 <= i - j < n - k:
            dist = min(dist, a[i] * j - sum(a[i - j:i]) + \
                       sum(a[i + 1:i + k - j + 1]) - a[i] * (k - j))
    if dist < m:
        m, d = dist, set()
    if dist == m: d.add(a[i])
print(max(d) - (0 if len(d) == 1 else min(d)))
