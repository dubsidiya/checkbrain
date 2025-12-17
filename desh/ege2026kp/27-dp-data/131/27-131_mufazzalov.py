# автор Муфаззалов Д.Ф.
with open('27.txt') as f:
    n, m, k = map(int, f.readline().split())
    a, ans, m, n = [list(map(int, i.split())) for i in f], 0, m + 1, n + 1
b = [[0] * (m+k) for i in range(n+k)]
for i in range(1, n):
    for j in range(1, m):
        b[i][j] = b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1] + a[i - 1][j - 1]
        ans = max(ans, b[i][j] - b[i - k][j] - b[i][j - k] + b[i - k][j - k])
print(ans)
