def prime(x):
    return x>1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

from math import ceil

MIN, MAX = 35_000_000, 100_000_000
min4, max4 = ceil(MIN**(1/4)), int(MAX**(1/4))

for x in range(min4, max4+1):
  if prime(x):
    print( x**4, int(x**3) )


