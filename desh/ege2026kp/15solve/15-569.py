def F( x, a1, a2 ):
  P = 5 <= x <= 47
  Q = 12 <= x <= 76
  R = 58 <= x <= 98
  A = a1 <= x <= a2
  return Q <= ( (not P) <= ( ((not R) and (not A)) <= (not Q)) )

points = [ x+dx for x in {5, 12, 47, 76, 58, 98}
                for dx in {-0.1, 0, 0.1} ]

minA = float('inf')
for a1 in points:
  for a2 in points:
    if all( F(x, a1, a2) for x in points ):
      minA = min( round(a2-a1), minA )

print( minA )
