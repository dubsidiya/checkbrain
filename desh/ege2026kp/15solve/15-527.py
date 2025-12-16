def f( x, a1, a2 ):
  P = 135 <= x <= 218
  Q = 174 <= x <= 308
  R = 246 <= x <= 382
  A = a1 <= x <= a2
  return (not (Q <= (P or R)) ) <= ((not A) <= (not Q))

points = [ x+dx for x in [135,218,174,308,246,382]
                for dx in [-0.1, 0, 0.1] ]

minLen = float('inf')
for a1 in points:
  for a2 in points:
    if all( f(x,a1,a2) for x in points ):
       minLen = min( minLen, round(a2-a1) )

print( minLen )

