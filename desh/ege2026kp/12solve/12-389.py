from string import digits, ascii_uppercase

alpha = digits + ascii_uppercase

def alg( s ):
  while any( p in s for p in ['GGGG', '333', 'G3'] ):
    s = s.replace('GGGG', '3', 1)
    s = s.replace('333', 'G', 1)
    s = s.replace('G3', '3G', 1)
  return s

count = 0
for n in range(4, 10000):
  s = alg( 'D' + n*'G' )
  sumDigits = sum( alpha.index(c) for c in s )
  if sumDigits % 5 == 0:
    count += 1

print( count )


