from fnmatch import fnmatch
from math import ceil

D = 1017
start = ceil( 205431 / D ) * D
end = int( 2954329991 / D ) * D
for n in range(start, end, D):
  if fnmatch( str(n), "2?5432*1" ) and str(n).count('9') > 0:
     print( n, n // D )