from itertools import product

D = 73
count = 0
def check( s ):
  global count
  n = int( s )
  if n % D == 0:
    count += 1
    print( n, n // D )

L = 0
while count < 5:
  for middle in product('0123456789',repeat=L):
    check( '12345' + ''.join(middle) + '76' )
    if count == 5: break
  L += 1