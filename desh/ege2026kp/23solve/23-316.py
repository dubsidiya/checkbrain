# Автор: М. Шагитов

from functools import *

@cache
def f(start, end, last=None):
    if start >= end:
        return start == end
    ways = 0
    if last != 'C':
        ways += f(start + 2, end, 'A')
    ways += f(start + 3, end, 'B')
    ways += f(start * 4, end, 'C')
    return ways


print(f(1, 50))
