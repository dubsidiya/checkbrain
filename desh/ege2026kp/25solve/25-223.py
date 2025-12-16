def allDivs( n ):
  q = round(n**0.5)
  divs = [] if n % q != 0 else \
         [q] if n // q == q else \
         [q, n//q]
  for d in range(1,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(divs)

k = 1
count = 0
while count < 5:
  x = 75000000 + k
  divs = [d for d in allDivs(x) if d % 2 == 0]
  if len(divs) % 2 == 1:
    print( k, len(divs) )
    count += 1
  k += 1
