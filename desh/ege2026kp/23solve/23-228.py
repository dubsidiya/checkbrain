def f( start, end, prog = '' ):
  if start == end:
    return 1 if prog[1] == 'B' and prog[-3] == 'C' else \
           0
  if start < end: return 0
  return f( start-2, end, prog+'A' ) + \
         f( start-3, end, prog+'B' ) + \
         f( start//2, end, prog+'C' )


print( f( 29, 2 ) )


# Автор: И. Карпачёв

from fnmatch import fnmatch

def f(a, b, s):
    if a < b: return 0
    if a == b and fnmatch(s, '?B*C??'):
      return 1
    return f(a - 2, b, s + 'A') + + f(a - 3, b, s + 'B') + f(a // 2, b, s + 'C')

print(f(29, 2, ''))
