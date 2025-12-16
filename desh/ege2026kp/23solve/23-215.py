# Автор: М. Байрамгулов

def f( start, end, step = 0 ):
    if start == end and step <= 7: return 1
    if step >= 7: return 0
    return f( start+1, end, step+1 ) + \
           f( start*2, end, step+1 ) + \
           f( start-3, end, step+1)

print( f(1, 10) )
