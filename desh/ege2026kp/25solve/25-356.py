from fnmatch import fnmatch

mask = "?13*79*9"
K = 7521

results = []
for n in range(0,10**9,K):
  if fnmatch( str(n), mask ):
    results.append( (n, sum( int(x) for x in str(n) )) )

for r in sorted(results, key=lambda x: (x[1], x[0])):
  print( *r )