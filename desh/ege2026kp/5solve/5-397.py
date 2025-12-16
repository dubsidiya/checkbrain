def alg( n ):
  s = f"{n:b}"
  if s.count("1") % 2 == 0:
    s = s + '0'
    s = '10' + s[2:]
  else:
    s = s + '1'
    s = '11' + s[2:]
  return int(s, 2)

for n in range(1,1000):
  R = alg(n)
  if R > 480:
    print( n )
    break