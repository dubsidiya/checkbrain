from functools import cache

@cache
def f( start, end, k3=0, k5=0 ):
  k3 += start % 3 == 0
  k5 += start % 5 == 0
  if start > end: return 0
  if start == end: return k3 == k5
  return f( start+1, end, k3, k5 ) + \
         f( start+4, end, k3, k5 ) + \
         f( start*3, end, k3, k5 )

count = f( 1, 180 )
print( sum(map(int, str(count))) )


# Автор: М. Шагитов

def f(s, e, k3, k5, stack={}):
    id = (s, k3, k5)
    if id in stack:
        return stack[id]
    k3 += s % 3 == 0
    k5 += s % 5 == 0
    if s > e:
        return 0
    if s == e:
        return k3 == k5
    result = (f(s + 1, e, k3, k5, stack) + \
              f(s + 4, e, k3, k5, stack) + \
              f(s * 3, e, k3, k5, stack))
    stack[id] = result
    return result

r = f(1, 180, 0, 0)
print( r )
print(sum(map(int, str(r))))







