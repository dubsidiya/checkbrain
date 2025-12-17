from itertools import accumulate, combinations
# автор Муфаззалов Д.Ф.
with open('27a.txt') as f:
   N, D, T = map(int, f.readline().split())
   a = [int(_) % D == 0 for _ in f]
   c = list(accumulate(a))
   b = [c[i] for i in range(N) if a[i] == 0]
   ans = sum([j - i == T for i, j in combinations(b, r=2)])
print(ans)