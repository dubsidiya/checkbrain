from fnmatch import fnmatch

mask = "1*1298*6"

K = 4329
for n in range(112986//K*K, 10**10, K):
   if fnmatch(str(n), mask):
      print( n, n // K )



