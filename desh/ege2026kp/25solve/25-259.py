from itertools import product
for d1 in '02468':
  for d2, d3 in product('0123456789', repeat=2):
    for d4 in '13579':
      n = int( f"11{d1}{d2}{d3}{d4}11" )
      if n % 2023 == 0:
        print( n, n // 2023 )