data = [ int(x) for x in open('17-426.txt').read().split() ]

r1 = max( abs(x) for x in data ) % 10
r2 = max(data) % 10

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if any( 1000 <= abs(x) < 10000 for x in triple ) and \
     sum( abs(x) % 10 == r1 for x in triple ) <= 1 and \
     sum( abs(x) % 10 == r2 for x in triple ) >= 1:
     results.append( sum(triple) )

print( len(results), sum(results)/len(results) )

