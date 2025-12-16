def f( start, end, mulCount = 0 ):
  if start == end: return 1
  if start > end: return 0
  count = f( start+2, end, mulCount )
  if mulCount < 3:
    count += f( start*3, end, mulCount+1 ) + f( start*5, end, mulCount+1 )
  return count

print( f(2, 200) )

