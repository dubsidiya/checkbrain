# Автор: Д. Статный

from fnmatch import *

k = 0
for x in range(0, 10**10, 4546):
    if fnmatch(str(x), '8*80*06'):
        k += 1
        if (k-1)%60==0:
            print(x, x//4546)
