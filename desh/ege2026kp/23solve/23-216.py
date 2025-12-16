# Автор: М. Байрамгулов

def f( start, end, p = 0):
    if start > end: return 0
    if start == end: return 1
    return f( start + 1, end, start ) + \
           f( start*3, end, start ) + \
           f( start + p, end, start ) * (p != 0)

print( f(2, 27) )

