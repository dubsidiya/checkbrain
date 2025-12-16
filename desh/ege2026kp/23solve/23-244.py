# Автор: М. Шагитов

from functools import cache

@cache
def f(start, end, energy=500):
    if start != end:
       energy -= sum(map(int, str(start)))
    if start > end or energy < 0:
        return 0
    if start == end:
       return energy >= 0
    return f(start + 3, end, energy) + \
           f(start * 4, end, energy) + \
           f(start * 5, end, energy)

print( f(1, 2000) )