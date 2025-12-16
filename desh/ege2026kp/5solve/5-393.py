#19872

def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 7)
  if n % 2 == 0:
    s = '1' + s + '52'
  else:
    s = s[-1] + s[1:-1] + s[0] + '15'
  return tobase(int(s,7), 7)

results = []
for n in range(1000):
  r = alg(n)
  if len(r) == 4:
    results.append(n)

print( max(results) )

