from fnmatch import fnmatch

def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s


n = int('12135664',7)
while n % 333 != 0: n += 1

while n < 10**9:
  if fnmatch( toBase(n,7), '?213*5664' ):
    print( n, n // 333 )
  n += 333