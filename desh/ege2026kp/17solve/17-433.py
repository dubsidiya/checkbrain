data = [ int(s) for s in open('17-433.txt') ]

m = min( x for x in data
           if abs(x) % 100 == 15 and 100 <= abs(x) <= 999 )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  nPlus = len( [x for x in triple if x > 0] )
  if nPlus % 3 == 0 and min(triple)*max(triple) > m**2:
    results.append( min(triple)*max(triple) )

print( len(results), min(results) )