def tobase( n, b ):
  s = '' if n < b else tobase(n//b, b)
  return s + str(n%b)

def alg( n ):
  s = tobase(n, 5)
  if n % 2 == 0:
    s += tobase(int(s[-1])*3, 5)
  else:
    s = s[-1] + s[1:-1] + s[0] + '1'
  return s

results = []
for n in range(1000):
  r = alg(n)
  if r.count('0') == 4:
    results.append(n)

print( min(results) )

