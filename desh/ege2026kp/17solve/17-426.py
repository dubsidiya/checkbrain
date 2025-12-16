data = [ int(x) for x in open('17-426.txt').read().split() ]

m43 = max( [ x for x in data
              if 10**4 <= abs(x) < 10**5 and abs(x) % 100 == 43] )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if sum( (10**4 <= abs(x) < 10**5 and abs(x) % 100 == 43) for x in triple ) > 0 and \
     sum( x*x for x in triple ) <= m43**2:
     results.append( sum( x*x for x in triple) )

print( len(results), min(results) )

