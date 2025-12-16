def f(x, a1, a2):
   P = 10 <= x <= 40
   Q = 5 <= x <= 15
   R = 35 <= x <= 50
   A = a1 <= x <= a2
   return (P <= Q) or ((not A) <= R)

points = [x+delta for x in [10, 40, 5, 15, 35, 50]
                  for delta in [-0.1, 0, 0.1]  ]

Amin = float('inf')
for a1 in points:
  for a2 in points:
    if all( f(x,a1, a2) for x in points ):
      Amin = min( Amin, round(a2) - round(a1) )

print( Amin )