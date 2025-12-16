def f(x, a1, a2):
  a = a1 <= x <= a2
  p = 52 <= x <= 105
  q = 0 <= x <= 53
  return (not(a) and not(p) and not(q)) <= (x*x > 303601)

from math import ceil
x0 = ceil(303601**0.5)
allPoints = [ x+delta for x in [0, 52, 53, 105, x0]
                      for delta in [-0.1, 0, 0.1] ]

results = []
for a1 in allPoints:
  for a2 in allPoints:
    if all( f(x, a1, a2) for x in allPoints if x >= 0 ):
      results.append( round(a2) - round(a1) )

print( min(results) )
