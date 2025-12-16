data = [ int(x) for x in open('17-428.txt').read().split() ]

mi11 = min(data) % 11
ma7  = max(data) % 7

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if any( 1000 <= x < 10000 for x in triple ) and \
     sum( x % 11 == mi11 for x in triple ) <= 1 and \
     sum( x % 7 == ma7 for x in triple ) >= 2:
     results.append( sum(triple) )

print( len(results), sum(results)/len(results) )

