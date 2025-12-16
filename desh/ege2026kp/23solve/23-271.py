# Автор: PRO100-ЕГЭ

def f( start, end ):
  if start > end: return 0
  if start == end: return 1
  return f( start+2, end ) + f( start*start, end ) + f( start**3, end )

print( f(10, 1000) )