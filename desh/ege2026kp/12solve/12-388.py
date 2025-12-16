from string import digits, ascii_uppercase

alpha = digits + ascii_uppercase

def alg( s ):
  while any( p in s for p in ['AAA', 'JJJ', 'JA'] ):
    s = s.replace('JA', 'AJ', 1)
    s = s.replace('AAA', 'J', 1)
    s = s.replace('JJJ', 'AA', 1)
  return s

M = nMax = 0
for n in range(4, 10000):
  s = alg( 'F' + n*'A' )
  sumDigits = sum( alpha.index(c) for c in s )
  if sumDigits > M:
    M, nMax = sumDigits, 1
  elif sumDigits == M:
    nMax += 1

print( M, nMax )


