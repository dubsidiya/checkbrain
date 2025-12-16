# Автор: А. Богданов

s = open('24-240.txt').readline().strip()

s='DAKOVAAA'

curLen = maxLen = 0
for i in range(len(s)-4):
  if sum( x == y for x, y in zip("DANOV",s[i:i+5]) ) == 4:
    curLen = 0
  else:
    curLen += 1
    maxLen = max(curLen, maxLen)

print( maxLen+4 )

