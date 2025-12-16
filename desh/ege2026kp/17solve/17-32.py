

start, end = 1000, 9999

def valid( x ):
  s = ''
  while x:
    s = str(x%6) + s
    x //= 6
  return len(s) <= 5 and (s.endswith('13') or s.endswith('14'))

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )