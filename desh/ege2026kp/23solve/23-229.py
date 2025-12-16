def f( start, end, prog = '' ):
  if any( x in prog for x in ['AA', 'BB', 'CC'] ):
    return 0
  if start == end:
    return 1 if prog[1] == 'A' and prog[-3:-1] == 'CB' else \
           0
  if start < end: return 0
  return f( start-1, end, prog+'A' ) + \
         f( start-2, end, prog+'B' ) + \
         f( start//2, end, prog+'C' )

print( f( 34, 2 ) )


# Автор: И. Карпачёв

from fnmatch import fnmatch

def f(a, b, s):
    if a < b: return 0
    if a == b and fnmatch(s, '?A*CB?') and 'AA' not in s and 'BB' not in s and 'CC' not in s: return 1
    return f(a - 1, b, s + "A") + f(a - 2, b, s + "B") + f(a // 2, b, s + "C")

print(f(34, 2, ''))

