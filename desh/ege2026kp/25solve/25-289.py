from fnmatch import fnmatch

mask = "12?345*9"

K = 7181
for n in range(1203459//K*K, 10**10, K):
   if fnmatch(str(n), mask):
      print( n, n // K )



