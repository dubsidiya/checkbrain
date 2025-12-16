from fnmatch import fnmatch

mask = "19*105*9"

K = 9601
for n in range(191059//K*K, 10**10, K):
   if fnmatch(str(n), mask):
      print( n, n // K )



