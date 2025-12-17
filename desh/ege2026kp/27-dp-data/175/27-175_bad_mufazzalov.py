# Автор Муфаззалов Д.Ф.

import itertools
with open('27.txt') as f:
   n, *a = map(int, f.readlines())

ans = 0
a.sort()
for t in range(2, n + 1):
  for i in itertools.combinations(a, t):
   if all([i[j + 1] - i[j] > 1 or i[j + 1] == i[j] for j in range(t - 1)]):
        if sum(i) > ans:
          print( sum(i), i )
        ans = max(ans, sum(i))
print(ans)