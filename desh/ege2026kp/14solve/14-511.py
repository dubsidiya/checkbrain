maxCount0 = 0
for x in range(1,3001):
  n = 4**210 + 4**110 - x
  count0 = 0
  while n:
    count0 += ((n % 4) == 0)
    n //= 4
  if count0 > maxCount0:
    maxCount0 = count0
    print( x )

