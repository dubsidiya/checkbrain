from string import ascii_uppercase
from itertools import product

target = 'DEFFED'
L = len(target)
found = False
no = sum( 26**i for i in range(L) )
for w in product( ascii_uppercase, repeat=L ):
  w = ''.join(w)
  if w == target:
    print( no )
    break
  no += 1

