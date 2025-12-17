import itertools, collections
# автор Муфаззалов Д.Ф.
with open('27.txt') as f:
   N, D, T = map(int, f.readline().split())
   a = [int(int(_) % D == 0) for _ in f]
   c = list(itertools.accumulate(a))
   b = [c[k] for k in range(N) if a[k] == 0]
   d = sorted(collections.Counter(b).items())
   ans = i = 0
   for j in range(len(d)):
       while d[j][0] - d[i][0] > T:
           i += 1
       if d[j][0] - d[i][0] == T:
           ans += d[j][1] * d[i][1]
print(ans)