from fnmatch import fnmatch

mask = "12*135*9"

K = 5321
for n in range(121359//K*K, 10**10, K):
   if fnmatch(str(n), mask):
      print( n, n // K )



