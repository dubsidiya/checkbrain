
def f( start, end, prog = None ):
  if prog is None: prog = []
  return 0 if start > end else \
         1 if start == end else \
         f( start+1, end, prog+[start+1] ) + \
           f( start*2, end, prog+[start*2] )

print( f(3, 20)*f(20, 43) + f(3, 20)*f(20, 47) +
       f(7, 20)*f(20, 43) + f(7, 20)*f(20, 47) )
