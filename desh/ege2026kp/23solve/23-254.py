# Вариант 1

def f( start, end, count1 ):
  if start > end or start in [11, 35]:
    return 0
  if start == end:
    return 1 if count1 == 0 else 0
  return f( start+1, end, count1-1 ) + \
         f( start*2, end, count1 ) + f( start+3, end, count1 )

count = 0
LIMIT = 5
for c11 in range(0,LIMIT+1):
  for c12 in range(0,LIMIT-c11+1):
    count += f(2, 18, c11)*f(18, 40, c12)
print( count )

# Вариант 2

def f( start, end, count1 = 0, has18 = False ):
  if start == 18: has18 = True
  if start > end or start in [11, 35]:
    return 0
  if start == end:
    return 1 if count1 <= 5 and has18 else \
           0
  return f( start+1, end, count1+1, has18 ) + \
         f( start*2, end, count1, has18 ) + f( start+3, end, count1, has18 )

print(  f(2, 40) )

