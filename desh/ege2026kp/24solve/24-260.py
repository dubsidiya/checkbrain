s = open('24-260.txt').read().strip()

ch = '02468'
nch = '13579'
L = maxLen = 0
prev = '.'
for c in s:
  if prev in ch and c in nch or \
    prev in nch and c in ch:
    L = 1
  else:
    L += 1
    maxLen = max( L, maxLen )
  prev = c

print( maxLen )
