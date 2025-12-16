
for x in range(1,10):
  b1 = 250 + x
  b2 = 100*x + 25
  n = 7*b1 + 7 - 3*b2 - 3
  if n % 99 == 0:
    print( f"{n // 99} при {x=}" )
