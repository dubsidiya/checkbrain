# Автор: В. Лашин

from itertools import *

n = 0
for x in product(sorted("КОТЕНА"), repeat=7):
    n += 1
    if n % 2 == 1 and sorted('КОТЕНОК') == sorted(x):
        print(n)
