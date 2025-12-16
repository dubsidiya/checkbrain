s0 = open('24-181.txt').readline()

s = s0
for c in 'AEIOUY':
  s = s.replace(c, ' ')

parts = s.split(' ')
parts.sort( key = len )

parts = [p for p in parts
           if p.count('.') >= 6 ]

print( len(parts[-1]) )

print( '-----------------------------------')

s = s0
Glas = 'AEIOUY'
parts = s.split('.')
maxLen = 0
nParts = len(parts)
for i in range(1,nParts-5):
  if all( not any(c in Glas for c in p)
          for p in parts[i:i+5] ):
    chunk = '.'.join( [''] + parts[i:i+5] + [''] )
    for c in parts[i-1][::-1]:
      if c in Glas: break
      chunk = c + chunk
    for c in parts[i+5]:
      if c in Glas: break
      chunk += c
    curLen = len(chunk)
    if curLen > maxLen:
      maxLen = curLen
      sMax = chunk

print( maxLen, sMax )

print( '-----------------------------------')

s = s0

Glas = 'AEIOUY'
N = len(s)
maxLen = L = countGlas = countPoint = 0
for R in range(N):
  countGlas += (s[R] in Glas)
  countPoint += (s[R] == '.')
  while countGlas > 0:
    countGlas -= (s[L] in Glas)
    countPoint -= (s[L] == '.')
    L += 1
  curLen = R - L + 1
  if countPoint >= 6 and curLen > maxLen:
    maxLen = curLen
    sMax = s[L:R+1]

print( maxLen, sMax )

