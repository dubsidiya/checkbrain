def alg( s ):
  while "31" in s or "211" in s or "1111" in s:
    s = s.replace("31", "1", 1)
    s = s.replace("211", "13", 1)
    s = s.replace("1111", "2", 1)
  return s

for n in range(3, 10001):
  s = alg( "3"+'1'*n )
  if sum(map(int, s)) == 15:
    print( n )
    break
