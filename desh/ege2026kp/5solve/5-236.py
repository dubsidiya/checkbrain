def alg( x ):
  s = bin(x)[2:]
  for _ in range(2):
    s += '1' if s[-1] == '0' else '0'
  return int(s, 2)

results = []
for N in range(1, 1000):
  R = alg(N)
  if R < 171:
    results.append( N )

print( max(results) )
