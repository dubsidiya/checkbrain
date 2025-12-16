def f(x, a1, a2):
  a = a1 <= x <= a2
  b = 3 <= x <= 49
  c = 0 <= x <= 5
  d = 43 <= x <= 123
  return not(a) or( not(b) and not(c) and not(d))

allPoints = [ x+delta for x in [0, 3, 5, 43, 49, 123, 993]
                      for delta in [-0.1, 0, 0.1] ]

results = []
for a1 in allPoints:
  for a2 in allPoints:
    if all( f(x, a1, a2) for x in allPoints
                         if 0 <= x <= 993 ):
      results.append( round(a2) - round(a1) )

print( max(results) )
