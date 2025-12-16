P = {3,6,9,12,15,18,21,24,27,30}
Q = {2,4,6,8,10,12,14,16,18,20}
R = {0,30,31,32,33,34,35,36,37,38,39,40}

def f(x, A):
  a = x in A
  p = x in P
  q = x in Q
  r = x in R
  return (not(a)) <= (((q <= p) <= r) or (x > 500))

A = set()
for a in set(range(510)):
  if any( not f(x, A) for x in range(0,510) ):
    A.add( a )

print( A )

p = 1
for a in A:
  p *= a
print( p )