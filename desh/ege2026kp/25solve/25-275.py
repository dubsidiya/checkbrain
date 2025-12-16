from fnmatch import fnmatch

def isValid( s ):
  n = len(s) // 2
  return int(s) % 519 == 0 and \
         sum(map(int, s[:n])) == sum(map(int, s[n:]))

from itertools import product

digits = "123456789"
xx = [ '' ] + \
     [ ''.join(s) for s in product(digits, repeat=2) ] + \
     [ ''.join(s) for s in product(digits, repeat=4) ]

for x in xx:
  for y in digits:
    s = f"32{x}54{y}123"
    if isValid(s):
      n = int(s)
      print( n, n//519 )
