
def f( start, end, stop='.', prog = '' ):
   if stop in prog or start > end: return 0
   return 1 if start == end else \
          f( start+3, end, stop, prog+'A') + \
          f( start*4, end, stop, prog+'B') + \
          f( start*5, end, stop, prog+'C')

print( f(1, 362, 'B')*f(362, 725) )