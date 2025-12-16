from fnmatch import fnmatch

def allDivs( n ):
  divs = set()
  for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0:
      divs.add( d )
      divs.add( n // d )
  return sorted(divs)

n = 12348
while n % 12 != 0: n += 1

while n <= 1300000:
  divs = allDivs(n)
  if len(divs) == 12 and fnmatch(str(n), '12*348'):
    print( n, divs[-2] )
  n += 12

# Автор: Н. Сафронов

from itertools import product

def f(n):
    a = set()
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            a.add(div)
            a.add(n // div)
    return a


for i in range(5):
    for x in product('0123456789', repeat=i):
        x = ''.join(x)
        n = int('12' + x + '348')
        if n % 12 == 0 and n <= 10 ** 7:
            a = f(n)
            if len(a) == 10:
                print(n, max(a))
