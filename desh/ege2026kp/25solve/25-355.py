from fnmatch import fnmatch

mask = "?05*22*3"

results = []
for n in range(0, 10**9, 8587):
  if fnmatch( str(n), mask ):
    results.append( (n, sum( int(x) for x in str(n) )) )

for r in sorted(results, key=lambda x: x[1]):
  print( *r )