data = [ int(x) for x in open('17-418.txt').read().split() ]

r5, r7 = min(data) % 5, max(data) % 7

N = len(data)
results = []
for i in range(N-1):
  pair = data[i:i+2]
  if any( (x % 5 == r5) for x in pair ) and \
     any( (x % 7 == r7) for x in pair ):
     results.append( sum(pair) )

print( len(results), max(results) )

