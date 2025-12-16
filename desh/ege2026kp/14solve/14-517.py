n0 = 49**71 + 7**15

def toBase7( n ):
  if n == 0: return '0';
  s = ''
  while n:
    s = str(n%7) + s
    n //= 7
  return s

for x in range(2030, 0, -1):
  n = n0 - x
  if toBase7(n).count('6') >= 11:
    print( x )
    break
