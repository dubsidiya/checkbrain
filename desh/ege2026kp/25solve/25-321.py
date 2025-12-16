from itertools import product

odd = '13579'
even = '02468'

for A in even:
  n = int( f"1{A}21574" )
  if n % 133 == 0:
    print( n, n // 133 )

for A in even:
 for B in odd:
   n = int( f"1{A}2157{B}4" )
   if n % 133 == 0:
     print( n, n // 133 )

for A in even:
 for B in product(odd, repeat=2):
   B = ''.join(B)
   n = int( f"1{A}2157{B}4" )
   if n % 133 == 0:
     print( n, n // 133 )

for A in even:
 for B in product(odd, repeat=3):
   B = ''.join(B)
   n = int( f"1{A}2157{B}4" )
   if n % 133 == 0:
     print( n, n // 133 )