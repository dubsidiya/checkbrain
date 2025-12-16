def f(x, t1, t2):
  t = t1 <= x <= t2
  a = 645 <= x <= 1632
  b = 0 <= x <= 700
  return (a or b or ((x+800)*(x-1500)>=0)) <= ((not(t) and x < 1568))

allPoints = [ x+delta for x in [0, 645, 700, 1500, 1568, 1632]
                      for delta in [-0.1, 0, 0.1] ]

results = []
for a1 in allPoints:
  for a2 in allPoints:
    if all( not f(x, a1, a2) for x in allPoints if x >= 0):
      results.append( round(a2) - round(a1) )

print( min(results) )
