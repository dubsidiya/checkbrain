# Автор: А. Сражаев

def er(s, f):
    seq = [0, 0] + [1] * (f - 1)
    for i in range(2, int(f**0.5) + 1):
        if seq[i]:
            for j in range(i*i, f + 1, i):
                seq[j] = 0
    return [i for i in range(max(2, s), f + 1) if seq[i]]

def allDivs( n ):
  q = round(n**0.5)
  divs = set()
  for d in range(1, q+1):
    if n % d == 0:
      divs |= {d, n // d}
  return sorted(divs)

a = er(10_000_000,30_000_000)

for n1,n2 in zip(a,a[1:]):
    if n2 - n1 == 150:
        mid = int(str(n2)[1:-1])
        print( n2, sum(allDivs(mid)) )
