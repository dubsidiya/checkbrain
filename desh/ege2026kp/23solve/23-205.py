def f( start, end, count = None ):
  if not count: count = [0, 0, 0]
  if start > end or count[0] > 4 or count[2] > 5: return 0
  if start == end:
    return 1 if count[1] >= 2 and count[2] == 5 else 0
  return f( start*5,  end, [count[0]+1, count[1], count[2]] ) + \
         f( start*3,  end, [count[0], count[1]+1, count[2]] ) + \
         f( start+45, end, [count[0], count[1], count[2]+1] )

N = 2970
print( f( 1, N ) )

