# Автор: М. Шагитов

from functools import *

@cache
def f(start, end, last=None):
    if start >= end:
        return start == end
    ways = 0
    if last != 'A':
        ways += f(start * 5, end, 'B')
    ways += f(start + 3, end, 'A')
    ways += f(start * 7, end, 'C')
    return ways


print(f(1, 1000))
