def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 8)
  if s[0] == '5':
    s = s.replace('1','*')
    s = s.replace('2','1')
    s = '11' + s.replace('*','2')
  else:
    s += '10'
    s = '2' + s[1:-1] + '0'
  return int(s,8)

results = []
for n in range(100):
  r = alg(n)
  if r < 1354:
    results.append( (r, n) )

print( max(results) )

