from itertools import product

D = 161
def check( s ):
  n = int( s )
  if n % D == 0:
    print( n, n // D )

digits = '0123456789'
for c1 in ['']+list(digits):
  for c0 in digits:
    check( f"12{c1}4{c0}65" )
for c1, c2 in product(digits, repeat=2):
  for c0 in digits:
    check( f"12{c1}{c2}4{c0}65" )

print( 'Вариант 2:' )
for n in range(1234065, 12994965+1):
  s = str(n)
  if s[:2] == '12' and s[-4] == '4' and s[-2:] == '65':
    check( s )
