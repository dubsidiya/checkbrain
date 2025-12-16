def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 4)
  if s[0] == '3':
    s = s.replace('1','*')
    s = s.replace('3','1')
    s = '21' + s.replace('*','3')
  else:
    s += '11'
    s = '2' + s[1:-1] + '1'
  return int(s,4)

results = []
for n in range(100):
  r = alg(n)
  if r < 598:
    results.append( (r, n) )

print( max(results) )

