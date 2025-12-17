# Автор Муфаззалов Д.Ф.
import collections
with open('27-176b.txt') as f:
   n, k = map(int, f.readline().split())
   p, x, ans = collections.Counter([int(i) for i in f]), [0] * k, 0
for i in range(max(p) + 1):
   x.append(max(x[-1], x.pop(0) + p[i] * i))
print(x[-1])



