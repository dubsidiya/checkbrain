def f( start, end ):
  if start > end: return 0
  if start == end: return 1
  res = f( start+1,  end ) + f( start*5,  end )
  if (10*start+1) % 3 == 0:
    res += f( 10*start+1, end )
  return res

N = 410
print( f( 1, N ) )

def f( start, end ):
  return 0 if start > end else \
         1 if start == end else \
         f( start+1,  end ) + f( start*5,  end ) + \
           (f( 10*start+1, end ) if (10*start+1) % 3 == 0 else 0)

print( f( 1, N ) )
