def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

def valid( n ):
  s = toBase(n, 9)
  prev = None
  for c in s:
    if prev and c > prev:
       return False
    prev = c
  return True

from itertools import product
digits = '0123456789'
pairs = ["".join(x) for x in product(digits, repeat=2)]
triples = ["".join(x) for x in product(digits, repeat=3)]
for a in digits:
  for b in [] + list(digits) + pairs + triples:
    s = f'3{a}458{b}3'
    n = int(s)
    s9 = toBase(n, 9)
    if valid(n):
      print( n, sum(map(int, s9)) )
