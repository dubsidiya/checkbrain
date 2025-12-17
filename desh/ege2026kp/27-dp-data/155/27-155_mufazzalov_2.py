# автор Муфаззалов Д.Ф.
with open('27.txt') as f:
   N, D, T = map(int, f.readline().split())
   d, s, ans = dict(), 0, 0
   for i in f:
       b = int(i) % D == 0
       s += b
       if not b:
           ans += d.get(s - T, 0)
           d[s] = d.get(s, 0) + 1
print(ans)