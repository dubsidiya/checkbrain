from functools import cache

@cache
def f( start, end, lastCmd = 0 ):
  if start > end: return 0
  if start == end: return 1
  lastDigit = start % 10
  firstDigit = start // 10 if start < 100 else start // 100
  return sum( f( start+k, end )
              for k in {1, lastDigit, firstDigit} if k > 0 )

count = f(82, 95)*f(95, 103)*f(103, 124)
print( count )

