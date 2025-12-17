# Автор Д.Ф. Муфаззалов

with open('27-174b.txt') as f:
    k, k = map(int, f.readline().split())
    c, a = sorted([list(map(int, i.split())) for i in f]), []
    [a.extend([i] * j) for i, j in c]
left, right, dist, n = 0, k, sum(a[1:k + 1]) - k * a[0], len(a)
d, m = {a[0]}, dist
for i in range(n - 1):
    dist += (a[i] - a[i + 1]) * ((right - i) - (i - left + 1))
    while right < n - 1:
        delta = (a[right + 1] - a[i + 1]) - (a[i + 1] - a[left])
        if delta < 0:
            left += 1
            right += 1
            dist += delta
        else:
            break
    if dist < m:
        m, d = dist, set()
    if dist == m:
        d.add(a[i + 1])
print(max(d) - (0 if len(d) == 1 else min(d)))
