# Автор Муфаззалов Д.Ф.
import collections
with open('27-175b.txt') as f:
   n, *data = map(int, f.readlines())
p, a, b = collections.Counter(data), 0, 0
for i in range(max(data) + 1):
   a, b = b, max(a + p[i] * i, b)
print(b)