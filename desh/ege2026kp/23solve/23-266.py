def f(start, end):
    if start < end or start in [9, 16]: return 0
    if start == end: return 1
    return f( start-1, end ) + f( start-2, end ) + \
           f( start//3, end )

print( f( 19, 3 ) )
