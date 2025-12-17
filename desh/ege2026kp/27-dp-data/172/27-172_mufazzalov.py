#автор Муфаззалов Д.Ф.

with open('27-172b.txt') as f:
    ans, *a = map(int, f.readlines())
    d, g = dict(), 23
    for i in a:
        r = i % g
        b = d.copy()
        if b.get(r, 0) == 0:
            b[r] = i, 1
        for j in d:
            if b.get(j, 0):
                x = d[j][0] + i
                t = x % g
                if b.get(t, 0) == 0 or x < b[t][0]:
                    b[t] = x, d[j % g][1] + 1
        d = b.copy()
    z = sum(a) % g
    ans -= d[z][1] if z else 0
print(ans)