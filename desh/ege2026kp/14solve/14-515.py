
for x in range(1,10):
  b1 = 9000 + x*100 + 87
  b2 = 100
  n = 1*b1 + 3 + 1*b2**2 + x*b2 + 9
  if n % 99 == 0:
    print( f"{n // 99} при {x=}" )
