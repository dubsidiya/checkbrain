def valid( n ):
  d = 2
  while n > 1:
    while n % d == 0:
      dMax = d
      n //= d
      if n % d == 0:
        return 0
    d += 1
  return dMax

count = 0
n = 8_000_000 + 10

while count < 5:
  d = valid( n )
  if d:
    print( n, d )
    count += 1
  n += 100
