def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 3)
  sumDig = sum( int(c) for c in s )
  if sumDig % 3 == 0:
    s = s.replace('1','*')
    s = s.replace('2','1')
    s = '10' + s.replace('*','2')
  else:
    s += '20'
    s = s[0] + '02' + s[3:]
  return int(s,3)

results = []
for n in range(100):
  r = alg(n)
  if r > 302:
    results.append( (r, n) )

print( min(results, key=lambda x: (x[0], -x[1])) )

