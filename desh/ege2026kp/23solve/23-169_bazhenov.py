# Автор: И. Баженов

def f( start, end, step ):
  if step > 9:
    return 0
  elif start == end and 1 <= step <= 9:
    return 1
  else:
    return f(start+3, end, step+1) + f(start-1, end, step+1)

print( f( 5, 5, 0 ) )
