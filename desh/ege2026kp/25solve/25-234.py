N0 = 9500000

def valid( n ):
  d = 2
  count = 0
  while n > 1:
    while n % d == 0:
      n //= d
      count += 1
      if count > 2: return False
    d += 1
  return True

def allDivs( n ):
  q = round( n**0.5 )
  divs = [] if n % q != 0 else \
         [q] if q == n // q else \
         [q, n//q]
  for d in range(1,q):
    if n % d == 0:
       divs.extend( [d, n//d] )
  return sorted(divs)

k = 1
count = 0
results = []
while count < 5:
  if valid( N0+k ):
    count += 1
    divs = allDivs( N0+k )
    results.append( (k, divs[-2]) )
  k += 1

for k, d in results[::-1]:
  print( k, d )