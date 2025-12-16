# Автор: М. Ишимов

from fnmatch import *

n = 0
while n*n <= 10**10:
  n += 1
  square = n*n
  if fnmatch(str(square), '4*1?009'):
    print(n, n*n)
