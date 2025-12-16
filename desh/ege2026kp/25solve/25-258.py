from itertools import product
nc = '13579'
ch = '02468'

for c1, n1 in product(ch,nc):
  for c2, n2 in product(ch,nc):
    for c3, n3 in product(ch,nc):
      n = int( f"1{c1}{n1}{c2}{n2}{c3}{n3}" )
      if n % 4023 == 0:
        print( n, n // 4023x` )