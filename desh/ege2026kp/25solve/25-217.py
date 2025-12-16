def toBase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

def valid( n ):
  s = toBase(n, 7)
  return s == s[::-1]

from itertools import product
digits = '0123456789'
pairs = ["".join(x) for x in product(digits, repeat=2)]
triples = ["".join(x) for x in product(digits, repeat=3)]
quads = ["".join(x) for x in product(digits, repeat=4)]
for a in [] + list(digits) + pairs + triples + quads:
  for b in digits:
    s = f'1{a}586{b}6'
    n = int(s)
    s5 = toBase(n, 7)
    if valid(n):
      print( n, sum(map(int, s5)) )
