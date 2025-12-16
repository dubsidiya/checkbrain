# Автор: Е. Джобс

def f( start, end ):
  if start == end: return True
  if start < 10: return False
  return f( start//10 + start%10, end) or \
         f( (start//10)*(start%10), end )

count = 0
for x in range(10, 100):
  if f(x, 8):
    count += 1
print( count )
