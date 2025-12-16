s = open('24-256.txt').readline().strip()

N = len(s)
dp = [1]*N
dp[1] = 2

for i in range(2,N):
  if s[i-2] in 'NOT' and s[i] in 'NOT':
    dp[i] = 2
  else:
    dp[i] = dp[i-1] + 1

print( max(dp) )