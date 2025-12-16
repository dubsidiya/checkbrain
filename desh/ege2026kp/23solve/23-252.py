def f( start, end, lastCmd = 0 ):
  if start == end: return 1
  if start > end: return 0
  count = 0
  if lastCmd != 1:
    count += f( start+1, end, 1 ) + f( start+3, end, 1 )
  if lastCmd != 2:
    count += f( start*2, end, 2 ) + f( start*3, end, 2 )
  return count

print( f(1, 9999) )