def f(x, A):
  return (5*x + 15 < 233345) and (A < 2*x + 3325)

for A in range(1,1000):
  if any( not f(x, A) for x in range(1,10**6) ):
    print( A )
    break
