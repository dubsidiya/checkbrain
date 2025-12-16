def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 6)
  if s[-1] == '3':
    s = s.replace('0','*')
    s = s.replace('2','0')
    s = '10' + s.replace('*','2')
  else:
    s += '12'
    s = '5' + s[1:-1] + '3'
  return int(s,6)

results = []
for n in range(100):
  r = alg(n)
  if r < 1299:
    results.append( (r, n) )

print( max(results, key=lambda x: (x[0], -x[1])) )

