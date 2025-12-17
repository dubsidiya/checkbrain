# Автор Муфаззалов Д.Ф.
import itertools

with open('27-176a.txt') as f:
   n, k = map(int, f.readline().split())
   a, ans = sorted([int(i) for i in f]), 0
for t in range(2, n + 1):
   for i in itertools.combinations(a, t):
       if all([i[j + 1] - i[j] >= k or i[j + 1] == i[j] for j in range(t - 1)]):
           ans = max(ans, sum(i))
print(ans)