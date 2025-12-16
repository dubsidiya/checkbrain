from fnmatch import fnmatch

mask = "202*47*6"

K = 9573
for n in range(202476//K*K, 10**10, K):
   if fnmatch(str(n), mask):
      print( n, n // K )



