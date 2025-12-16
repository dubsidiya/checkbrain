# Автор: Л. Шастин

with open('26-168.txt') as f:
  n, k = map(int, f.readline().split())
  data = sorted(list(map(int, x.split())) for x in f)

dp = {1: 0}
for cur, nxt, prc in data:
  dp[nxt] = min(dp.get(cur, k + 1) + prc, dp.get(nxt, k + 1))

z_max = max(z for z in dp if dp[z] <= k)

print(z_max, k - dp[z_max])
