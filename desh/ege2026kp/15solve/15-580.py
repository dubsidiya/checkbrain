def f(x, A):
  return  ( x % 12 == A ) <= ( x % 8 != 7 or x % 9!= 2 )

for A in range(1000):
  if all( f(x, A) for x in range(1000) ):
    print( A )
    break
