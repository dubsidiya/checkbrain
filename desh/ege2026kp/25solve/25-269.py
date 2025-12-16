# Автор: Д. Статный

def allDivs(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d |= {i, x//i}
    return sorted(d)

result = []
count = 0
for i in range(int(500_000_000 ** 0.5), 0, -1):
    x = i ** 2
    divs = allDivs( x )
    if len(divs) == 7:
       result.append( (x, divs[-1]) )
       count += 1
       if count == 5: break

for res in result[::-1]:
  print( *res )
