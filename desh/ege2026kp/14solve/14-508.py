from string import ascii_uppercase, digits

A = digits + ascii_uppercase
def intx( s, base ):
  s = [ A.index(c) for c in s ][::-1]
  num = sum( a*base**i for i, a in enumerate(s) )
  return num

pq = []
for p in range(31,100):
  for q in range(35,100):
    R = intx('SIRIUS', p) + intx('LYCEUM', q)
    if R % 2025 == 0:
      pq.append( (p+q, p, q, R, R // 2025) )

print( min(pq) )