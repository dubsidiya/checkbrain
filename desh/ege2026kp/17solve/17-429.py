data = [ int(x) for x in open('17-428.txt').read().split() ]

mi7 = min(data) % 7
ma5 = max(data) % 5

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if any( 100 <= x < 1000 for x in triple ) and \
     sum( x % 5 == mi7 for x in triple ) <= 1 and \
     sum( x % 7 == ma5 for x in triple ) >= 2:
     results.append( sum(triple) )

print( len(results), sum(results)/len(results) )

