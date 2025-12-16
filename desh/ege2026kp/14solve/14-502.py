def N( x ):
  return 5*9**22 + 3*9**12 + 2*81**5 + 5*729**2 + 30 - x

def toBase( x, base ):
  s = ''
  while x:
    s = str(x%base) + s
    x //= base
  return s

base = 9
x = 0
s = toBase( N(x), base )
print( s )

for i in range(1,len(s)):
  nZeros = s[:-i].count('0')
  lenTail = len(s[-i:])
  if nZeros < lenTail or (nZeros == lenTail and s[-i-1] == '0'):
    print( s[:-i], s[-i:] )
    x = int( s[-i:], base ) + 1
    print( toBase(x,base), x )
    break

s = toBase( N(x), base )
print( s )
print( s.count('8'), s.count('0') )
