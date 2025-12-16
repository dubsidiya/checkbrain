# Автор: Д. Статный

def isPrime( x ):
  q = int(x**0.5)
  return x == 2 or \
         all( x % d != 0 for d in range(2,q+1) )

from math import ceil
count = 0
i = 35_000_000
while True:
  x = i
  while x % 2 == 0: x //= 2
  qX = round(x**0.25)
  if isPrime(qX) and qX**4 == x:
    print( i, x )
    count += 1
    if count == 5: break
  i += 1
