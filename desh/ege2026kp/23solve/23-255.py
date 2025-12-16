# Вариант 1

def f( start, end, count1 ):
  if start > end or start in [10, 38]:
    return 0
  if start == end:
    return 1 if count1 == 0 else 0
  return f( start+1, end, count1-1 ) + \
         f( start+2, end, count1 ) + f( start*3, end, count1 )

count = 0
LIMIT = 3
for c11 in range(0,LIMIT+1):
  for c12 in range(0,LIMIT-c11+1):
    count += f(1, 25, c11)*f(25, 43, c12)
print( count )

# Вариант 2

from functools import cache

@cache
def f( start, end, count1 = 0, has25 = False ):
  if start == 25: has25 = True
  if start > end or start in [10, 38]:
    return 0
  if start == end:
    return 1 if count1 <= 3 and has25 else \
           0
  return f( start+1, end, count1+1, has25 ) + \
         f( start+2, end, count1, has25 ) + f( start*3, end, count1, has25 )

print(  f(1, 43) )

