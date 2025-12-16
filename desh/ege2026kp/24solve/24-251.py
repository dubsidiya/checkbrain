s = open('24-251.txt').readline()

prev = '.'
maxLen = curLen = 0
for c in s:
  if c in 'AD':
    if prev != c:
      maxLen = max( curLen, maxLen )
    curLen = 0
    prev = c
  else:
    curLen += 1

print( maxLen + 2 )


