
for x in range(1,10):
  b1 = 88000 + x*100 + 88
  b2 = 100
  n = 1*b1 + 3 + 1*b2**2 + 4*b2 + x
  if n % 99 == 0:
    print( f"{n // 99} при {x=}" )
