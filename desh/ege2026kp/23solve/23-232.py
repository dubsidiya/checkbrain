
def f( start, end, stop='.', prog = '' ):
   if prog.count(stop) > 4 \
      or start > end: return 0
   return 1 if start == end else \
          f( start+3, end, stop, prog+'A') + \
          f( start*4, end, stop, prog+'B') + \
          f( start*5, end, stop, prog+'C')

print( f(1, 16)*f(16, 140, 'A')*f(140, 725) )