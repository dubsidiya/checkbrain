from functools import cache

# Вариант 1

@cache
def f( start, end, count1 ):
  if start > end or start in [20, 58]:
    return 0
  if start == end:
    return 1 if count1 == 0 else 0
  return f( start+1, end, count1-1 ) + \
         f( start+3, end, count1 ) + f( start*3, end, count1 )

count = 0
LIMIT = 6
for c11 in range(0,LIMIT+1):
  for c12 in range(0,LIMIT-c11+1):
    count += f(3, 37, c11)*f(37, 95, c12)
print( count )

# Вариант 2

@cache
def f( start, end, count1 = 0, has37 = False ):
  if start == 37: has37 = True
  if start > end or start in [20, 58]:
    return 0
  if start == end:
    return 1 if count1 <= 6 and has37 else \
           0
  return f( start+1, end, count1+1, has37 ) + \
         f( start+3, end, count1, has37 ) + f( start*3, end, count1, has37 )

print(  f(3, 95) )

