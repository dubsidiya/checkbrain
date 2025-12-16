s = open('24-261.txt').read().strip()

N = len(s)
dp = [0]*N
for i in range(2,N):
  if s[i-1:i+1] == 'EA':
    dp[i] = dp[i-2] + 2
  if i > 2 and s[i-2:i+1] == 'NPC':
    dp[i] += dp[i-3] + 3

print( max(dp) )
