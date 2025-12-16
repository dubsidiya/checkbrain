def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 5)
  sumDig = sum( int(c) for c in s )
  if sumDig % 5 == 0:
    s = s.replace('0','*')
    s = s.replace('1','0')
    s = s.replace('*','1') + '14'
  else:
    s += '33'
    s = '44' + s[2:]
  return int(s,5)

results = []
for n in range(100):
  r = alg(n)
  if r > 370:
    results.append( (r, n) )

print( min(results) )

