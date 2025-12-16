def oddDivs(n):
  q = round(n**0.5)
  divs = [] if n % q != 0 else \
         [q] if q == n // q else \
         [q, n//q];
  for d in range(1,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(d for d in divs if d % 2 == 1)

D = 7*13*17*23*29

n = 1000000000
while n % D != 0:
  n += 1

count = 0
d = {}
while n <= 2000000000:
  oDivs = oddDivs(n)
  if len(oDivs) > 100 and 3 not in oDivs and 5 not in oDivs:
    count += 1
    d[n%10] = d.get(n%10,0) + 1
    if n % 10 == 8:
      print( n, max(oDivs) )
  n += D

print(count)
print(d)
