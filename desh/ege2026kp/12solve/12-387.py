
for n in range(2, 10000):
  s = '1' + '2'*n
  while '12' in s or '322' in s or '222' in s:
    s = s.replace('12', '2', 1)
    s = s.replace('322', '21', 1)
    s = s.replace('222', '3', 1)
  sumDigits = sum( int(x) for x in s )
  if sumDigits == 15: break

print( n, sumDigits )
