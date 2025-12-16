for x in range(2300,0,-1):
  n = 7**350 + 7**150 - x
  count0 = 0
  while n:
    count0 += ((n % 7) == 0)
    n //= 7
  if count0 == 200:
    print( x )
    break

