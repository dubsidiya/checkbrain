def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 4)
  sumDig = sum( int(c) for c in s )
  if sumDig % 4 == 0:
    s = s.replace('0','*')
    s = s.replace('3','0')
    s = s.replace('*','3') + '21'
  else:
    s += '22'
    s = '11' + s[2:]
  return int(s,4)

results = []
for n in range(100):
  r = alg(n)
  if r > 200:
    results.append( (r, n) )

print( min(results) )

