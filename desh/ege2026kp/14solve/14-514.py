
for x in range(1,10):
  b1 = 370 + x
  b2 = 100*x + 73
  n = 7*b1 + 5 + 3*b2 + 7
  if n % 99 == 0:
    print( f"{n // 99} при {x=}" )
