data = [ int(s) for s in open('17-434.txt') ]

m = min( x for x in data
           if x % 10 == 6 and 1000 <= x <= 9999 )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  nSpec = len( [x for x in triple
                  if abs(x) % 10 == 6 and 1000 <= abs(x) <= 9999] )
  if nSpec == 1 and sum(triple) <= m:
    results.append( sum(triple) )

print( len(results), max(results) )