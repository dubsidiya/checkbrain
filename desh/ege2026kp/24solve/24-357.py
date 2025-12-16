from re import findall

s = open('24-357.txt').readline()

M = 130

N = len(s)
minLen = float('inf')
countRSQ = 0
L = 0
for R in range(3,N+1):
  if s[R-3:R] == 'RSQ': countRSQ += 1
  if s[R-1] == 'Q': continue
  while countRSQ > M:
    if s[L:L+3] == 'RSQ': countRSQ -= 1
    L += 1
  if countRSQ == M:
    while not s[L:R].startswith('RSQ'):
      L += 1
    if R - L < minLen:
      print( L, R, R - L )
      print( s[L:R].count('RSQ') )
      print( s[L:R] )
    minLen = min( minLen, R - L )

print( minLen )


# Автор: А. Кабанов

s = open('24-357.txt').readline()

m = 10000
for l in range(len(s)):
  for r in range(l+m,l,-1):
    c = s[l:r+1]
    if c.count('RSQ')<130: break
    if c.count('RSQ')==130 and c[-1]!='Q':
      m = min(m, len(c))

print( m )
