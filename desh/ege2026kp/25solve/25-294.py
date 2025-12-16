from fnmatch import fnmatch

mask = "1?1?1?1*1"

K = 2023
for n in range(10101011//K*K, 2*10**9, K):
   if fnmatch(str(n), mask) and \
      sum( map(int, str(n)) ) == 22:
      print( n, n // K )



