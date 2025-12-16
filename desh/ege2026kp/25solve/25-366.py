def valid( n ):
  d = 2
  while n > 1:
    count = 0
    while n % d == 0:
      n //= d
      count += 1
    if count == 5:
      return d
    d += 1
  return 0

count = 0
n = 5_000_000 + 12

while count < 5:
  d = valid( n )
  if d:
    print( n, d )
    count += 1
  n += 100
