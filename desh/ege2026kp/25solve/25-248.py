from itertools import product

D = 141
def check( s ):
  n = int( s )
  if n % D == 0:
    print( n, n // D )

digits = '0123456789'
for c in ['']+list(digits):
  check( f"1234{c}7" )
for c1, c2 in product(digits, repeat=2):
  check( f"1234{c1}{c2}7" )
for c1, c2, c3 in product(digits, repeat=3):
  check( f"1234{c1}{c2}{c3}7" )
