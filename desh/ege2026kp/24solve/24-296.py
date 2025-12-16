s = open('24-296.txt').readline()

TARGET = 160

maxLen = 0
L = 0
countCD = 0
for R in range(len(s)):
  if s[R] == 'D' and R > 0 and s[R-1] == 'C':
    countCD += 1
  while countCD > TARGET:
    if s[L] == 'C' and s[L+1] == 'D':
      countCD -= 1
    L += 1
  if countCD == TARGET:
    maxLen = max( maxLen, R-L+1 )

print( maxLen )

#------------------------------------------

s = open('24-296.txt').readline()

s = s.replace('CD', 'C D').split()

maxLen = 0
for i in range(len(s)):
  chunk = ''.join(s[i:i + TARGET + 1])
  maxLen = max( maxLen, len(chunk) )

print( maxLen )