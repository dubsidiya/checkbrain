# Автор Муфаззалов Д.Ф.
import itertools

with open('27-173a.txt') as f:
    n, K = map(int, f.readline().split())
    a, ans = [int(i) for i in f], 0
    for z in range(n // K + (n % K > 0) + 1):
        for j in itertools.combinations(range(n), z):
            if all([j[p] - j[p - 1] >= K for p in range(1, z)]):
                ans = max(ans, sum([a[p] for p in j]))
    print(ans)