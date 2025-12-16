def f(x):
  a = a1<=x<=a2
  p = 95892<=x<=345678
  q = 123456<=x<=760123
  r = 875643<=x<=985672
  return (q <= ((not p) <= (( (not r) and  (not a)) <= (not q))))

allPoints = [ x+y for x in [95892, 345678, 123456, 760123, 875643, 985672]
                  for y in [-0.1, 0, 0.1] ]

m=[]
for a1 in allPoints:
  for a2 in allPoints:
    if all(f(x)==1 for x in allPoints):
      m.append( round(a2-a1) )
print(min(m))