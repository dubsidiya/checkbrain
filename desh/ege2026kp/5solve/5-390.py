def tobase( n, base ):
  s = ''
  while n:
    s = str(n%base) + s
    n //= base
  return s

def alg( N ):
  s = tobase( N, 3 )
  if N % 3 == 0:
    s += s[-2:]
  else:
    s += tobase(sum(map(int, s)), 3)
  return int( s, 3 )

results = []
for n in range(1,1000):
  R = alg(n)
  if R > 220:
    results.append(R)

print( min(results) )