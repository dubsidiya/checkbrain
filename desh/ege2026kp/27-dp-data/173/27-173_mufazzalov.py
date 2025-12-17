# Автор Муфаззалов Д.Ф.

with open('27-173b.txt') as f:
   n, K = map(int, f.readline().split())
   nums, ans, a = [int(i) for i in f], 0, [0] * K
   for i in nums:
       z = max(a[:2])
       a.append(a.pop(0) + i)
       a[0] = z
   print(max(a))