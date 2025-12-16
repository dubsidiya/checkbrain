def ДЕЛ(x, A): return x % A == 0

def f( x, A ):
  return (ДЕЛ(x, A) and ДЕЛ(x, 24) and not ДЕЛ(x, 16)) <= (not ДЕЛ(x, A))


A = 1
while not all( f(x, A) for x in range(1,1000) ):
    A += 1
print( A )
