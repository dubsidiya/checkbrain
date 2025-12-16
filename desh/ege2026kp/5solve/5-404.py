def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 4)
  sumDig = sum( int(c) for c in s )
  if sumDig % 4 == 0:
    s = s.replace('0','*')
    s = s.replace('2','0')
    s = '32' + s.replace('*','2')
  else:
    s += '33'
    s = s[0] + '10' + s[3:]
  return int(s,4)

results = []
for n in range(100):
  r = alg(n)
  if r > 320:
    results.append( (r, n) )

print( min( results, key=lambda x: (x[0], -x[1]) ) )

