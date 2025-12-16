from functools import cache

@cache
def f( start, end, even=0, odd=0 ):
  even += start % 2 == 0
  odd += start % 2 != 0
  if start > end: return 0
  if start == end: return even > odd
  return f( start+2, end, even, odd ) + \
         f( start+3, end, even, odd ) + \
         f( start*4, end, even, odd )

count = f( 1, 100 )
print( sum(map(int, str(count))) )


# Автор: М. Шагитов

def f(s, e, ch, nch, stack={}):

    id = (s, ch, nch)
    if id in stack:
        return stack[id]
    ch += s % 2 == 0
    nch += s % 2 != 0
    if s > e:
        return 0
    if s == e:
        return ch > nch
    result = ( f(s + 2, e, ch, nch, stack) + \
               f(s + 3, e, ch, nch, stack) + \
               f(s * 4, e, ch, nch, stack) )
    stack[id] = result
    return result

r = f(1, 100, 0, 0)
print( r )
print(sum(map(int, str(r))))







