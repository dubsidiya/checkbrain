def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 3)
  sumDig = sum( int(c) for c in s )
  if sumDig % 3 == 0:
    s = s.replace('0','*')
    s = s.replace('1','0')
    s = '10' + s.replace('*','1')
  else:
    s += '101'
    s = '22' + s[2:]
  return int(s,3)

results = []
for n in range(100):
  r = alg(n)
  if r > 314:
    results.append( (r, n) )

print( min(results) )

