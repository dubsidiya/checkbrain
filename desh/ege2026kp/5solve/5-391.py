def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 4)
  if n % 2 == 0:
    s = '12' + s + tobase(int(s[-1])*3, 4)
  else:
    s = '13' + s + '21'
  return int(s, 4)

results = []
for n in range(100):
  r = alg(n)
  if r > 50:
    results.append(r)

print( min(results) )

