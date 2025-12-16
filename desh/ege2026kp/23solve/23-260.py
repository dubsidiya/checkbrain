from math import gcd
def f( start, end ):
  if start > end: return 0
  if start == end: return 1
  count = 0
  if gcd(start+1, start) == 1:
    count += f( start+1, end )
  if gcd(start+3, start) == 1:
    count += f( start+3, end )
  if gcd(start+7, start) == 1:
    count += f( start+7, end )
  return count

print( f(13, 31) )