def f( start, end, diff = 0 ):
  if start == end:
    return 1 if diff > 0 else 0
  if start > end: return 0
  count = f( start+1, end, diff-1 ) + \
          f( start*2, end, diff+1 ) + f( start*5, end, diff+1 )
  return count

print( f(3, 260) )

"""
maxCount = 0
for x in range(1,500):
  count = f(3, x)
  if count > maxCount:
    print( x, count )
    maxCount = count
"""

