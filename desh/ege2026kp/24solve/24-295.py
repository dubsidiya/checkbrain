s = open('24-295.txt').readline()

MAX = 240

maxLen = 0
L = 0
countDE = 0
for R in range(len(s)):
  if s[R] == 'E' and R > 0 and s[R-1] == 'D':
    countDE += 1
  while countDE > MAX:
    if s[L] == 'D' and s[L+1] == 'E':
      countDE -= 1
    L += 1
  maxLen = max( maxLen, R-L+1 )

print( maxLen )

#------------------------------------------

s = open('24-295.txt').readline()

s = s.replace('DE', 'D E').split()

maxLen = 0
for i in range(len(s)):
  chunk = ''.join(s[i:i + MAX + 1])
  maxLen = max( maxLen, len(chunk) )

print( maxLen )