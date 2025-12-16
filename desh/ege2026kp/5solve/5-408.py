def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 5)
  if s[-1] == '0':
    s = s.replace('1','*')
    s = s.replace('4','1')
    s = '33' + s.replace('*','4')
  else:
    s += '44'
    s = '3' + s[1:-1] + '2'
  return int(s,5)

results = []
for n in range(100):
  r = alg(n)
  if r < 1922:
    results.append( (r, n) )

print( max(results, key=lambda x: (x[0], -x[1])) )

