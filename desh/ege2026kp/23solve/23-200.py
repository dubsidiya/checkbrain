def f( start, end, diff = 0, prog = None ):
  if not prog: prog = []
  if start == end:
    #if diff > 0: print( prog )
    return 1 if diff > 0 else 0
  if start > end: return 0
  count = f( start+3, end, diff-1, prog+[1] ) + \
          f( start*2, end, diff+1, prog+[2] ) + f( start*7, end, diff+1, prog+[3] )
  return count

print( f(2, 472) )

"""
maxCount = 0
for x in range(1,500):
  count = f(2, x)
  if count > maxCount:
    print( x, count )
    maxCount = count
"""

