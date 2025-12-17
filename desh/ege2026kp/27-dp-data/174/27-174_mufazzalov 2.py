# Автор Д.Ф. Муфаззалов

p, u = dict(), set()
with open('27-174b.txt') as f:
    k, k = map(int, f.readline().split())
    for i in f:
        e, r = map(int, i.split())
        p[e] = r
a = sorted(list(p.keys()))
q, b = (max(a) - min(a)) * len(a), []
[b.extend([i] * p[i]) for i in a]
a, m = [a[0] - q] + a + [q + a[-1]], q
for i in b:
    if i not in u:
        u.add(i)
        j = w = a.index(i)
        t, dist = k - p[i] + 1, 0
        while t > 0:
            if abs(a[j + 1] - i) < abs(a[w - 1] - i):
                j += 1
                z = j
            else:
                w -= 1
                z = w
            r = min(p[a[z]], t)
            t -= r
            dist += abs(i - a[z]) * r
        if dist < m:
            d, m = set(), dist
        if dist == m: d.add(i)
print(max(d) - (0 if len(d) == 1 else min(d)))
