# Автор: М. Байрамгулов

from functools import lru_cache

@lru_cache(None)
def f( x, y ):
    if x == 17 and y == 27: return 1
    if x > 17 or y > 27: return 0
    return f( x+1, y ) + f( x*2, y ) + f( x,y+3 )

print( f(1,0) )

