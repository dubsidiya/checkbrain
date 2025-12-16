from string import ascii_uppercase, digits

s = open('24-264.txt').readline().strip()

for c in ascii_uppercase:
  s = s.replace(c, '.')
for c in digits:
  s = s.replace(c, '*')

dp = [1]*len(s)
for i in range(1, len(s)):
  if s[i] != s[i-1]:
    dp[i] += dp[i-1]

print( max(dp) )
