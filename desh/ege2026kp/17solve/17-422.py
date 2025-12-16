data = [ int(x) for x in open('17-418.txt').read().split() ]

r5, r7 = min(data) % 5, max(data) % 7

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if sum( (x % 5 == r5) for x in triple ) == 1 and \
     sum( (x % 7 == r7) for x in triple ) == 1:
     results.append( sum(triple) )

print( len(results), min(results) )

