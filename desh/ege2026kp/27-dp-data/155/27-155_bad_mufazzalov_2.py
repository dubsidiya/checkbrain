from itertools import combinations
# автор Муфаззалов Д.Ф.
with open('27a.txt') as f:
   N, D, T = map(int, f.readline().split())
   a = [int(_) % D == 0 for _ in f]
   ans = sum([a[i] + a[j] == 0 and sum(a[i + 1:j + 1]) == T \
              for i, j in combinations(range(N), r=2)])
print(ans)