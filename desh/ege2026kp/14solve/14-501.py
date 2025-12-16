def N( x ):
  return 5*7**22 + 3*7**15 + 2*49**6 + 5*343**3 + 30 - x

def toBase( x, base ):
  s = ''
  while x:
    s = str(x%base) + s
    x //= base
  return s

x = 0
s = toBase( N(x), 7 )
print( s )

for i in range(1,len(s)):
  nZeros = s[:-i].count('0')
  lenTail = len(s[-i:])
  #print( nZeros, lenTail )
  if nZeros < lenTail or (nZeros == lenTail and s[-i-1] == '0'):
    print( s[:-i], s[-i:] )
    x = int( s[-i:], 7 ) + 1
    print( toBase(x,7), x )
    break

s = toBase( N(x), 7 )
print( s )
print( s.count('6'), s.count('0') )
