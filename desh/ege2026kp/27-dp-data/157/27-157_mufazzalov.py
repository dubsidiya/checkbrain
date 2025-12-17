# Автор: Д.  Муфаззалов

with open('27-157b.txt') as f:
    n, k = map(int, f.readline().split())
    ans = -200000
    a, b = [], [ans] * 2
    for i in f:
        x, y = map(int, i.split())
        while len(a) and x - a[0][0] >= k:
            b[a[0][1] % 2] = max(b[a[0][1] % 2], a[0][1])
            a.pop(0)
        a.append((x, y))
        ans = max(ans, b[y % 2] + y)
print(ans)