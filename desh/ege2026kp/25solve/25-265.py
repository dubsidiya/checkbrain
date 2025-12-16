# Автор: Д. Статный

def allDivs(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d |= {x//i, i}
    return sorted(d)

from math import ceil
i = ceil( 100_000_000**(0.5) )
count = 0
while True:
  x = i**2
  divs = allDivs( x )
  if len(divs) == 39 and x % 2 == 0:
     print( x, max(x for x in divs if x % 2 != 0) )
     count += 1
     if count == 5: break
  i += 1

i = int( 1_000_000_000**(0.5) )
count = 0
ans = []
while True:
  x = i**2
  divs = allDivs( x )
  if len(divs) == 39 and x % 2 == 0:
     ans.append( (x, max(x for x in divs if x % 2 != 0)) )
     count += 1
     if count == 5: break
  i -= 1

for x in ans[::-1]:
  print(x[0], x[1])


