from fnmatch import fnmatch

Q = [117, 119, 121]
def check( n ):
  if fnmatch(str(n), '1?58*129'):
    R = [ n % q for q in Q ]
    if R.count(0) == 1:
       return [(n, n//q) for q, r in zip(Q, R) if r == 0 ]
  return []

result = []
for q in Q:
  for n in range(158129//q*q, 2*10**7, q):
    result += check( n )

for r in sorted(result):
  print( *r )

print()

# Автор: А. Рогов

from fnmatch import fnmatch

for i in range(10**8 + 1):
    ost = (i % 117 == 0, i % 119 == 0, i % 121 == 0)
    if sum(ost) == 1 and fnmatch(str(i), '1?58*129'):
        print(i, end=' ')
        if ost[0] == 1:
            print(i // 117)
        elif ost[1] == 1:
            print(i // 119)
        else:
            print(i // 121)
