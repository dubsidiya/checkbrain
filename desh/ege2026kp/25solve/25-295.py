count = 0
digits = '0123456789'
for x1 in [''] + list(digits):
  for x2 in digits:
    n = int( f'6323{x1}353{x2}' )
    if n % 28 == 0:
      print( n, n//28)

print()

# Автор: Д. Статный

from itertools import product
for nan in '0123456789':
    for k in range(2):
        for p in product('0123456789', repeat=k):
            s = int('6' + '323' + ''.join(p) + '353' + nan)
            if s%28==0:
                print(s, s//28)

