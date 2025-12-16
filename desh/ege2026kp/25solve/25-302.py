from fnmatch import fnmatch
from math import ceil

D = 50068
start = ceil(909798/D) * D
end = int(9997999998/D) * D
for n in range(start, end+1, D):
  s = str(n)
  if fnmatch( s, "9?979*8" ) and '0' in s:
    print( n, n // D )