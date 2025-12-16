# Автор: М. Шагитов

from functools import lru_cache

@lru_cache(None)
def f(s, e, special = 0):
    special += (s in (8, 16, 32))
    if s > e or special > 1: return 0
    if s == e: return (special == 1)
    return f(s + 1, e, special) + \
           f(s + 4, e, special) + \
           f(s * 2, e, special)

print( f(1, 50) )
