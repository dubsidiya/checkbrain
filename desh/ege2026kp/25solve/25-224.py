def oddEvenDivs( n ):
  count2 = 0
  while n % 2 == 0:
    count2, n = count2+1, n // 2
  if count2 % 2 == 0: return False, 0

  d, p = 3, 1
  while n > 1 and d*d <= n:
    count = 0
    while n % d == 0:
      count, n = count+1, n // d
    if count % 2 == 1: return False, 0
    p *= count + 1
    d += 2

  return n == 1, p*count2

k = 1
count = 0
while count < 5:
  x = 750000000 + k
  valid, evenDivs = oddEvenDivs(x)
  if valid:
    count += 1
    print(k, evenDivs)
  k += 1
