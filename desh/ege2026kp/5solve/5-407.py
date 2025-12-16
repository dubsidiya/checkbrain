def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 7)
  if s[-1] == '2':
    s = s.replace('1','*')
    s = s.replace('3','1')
    s = '21' + s.replace('*','3')
  else:
    s += '31'
    s = '1' + s[1:-1] + '6'
  return int(s,7)

results = []
for n in range(100):
  r = alg(n)
  if r < 744:
    results.append( (r, n) )

print( max(results, key=lambda x: (x[0], -x[1])) )

