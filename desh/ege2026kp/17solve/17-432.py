data = [ int(s) for s in open('17-432.txt') ]

s = sum( x for x in data if x < 0 )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if min(triple)*max(triple) > s:
    results.append( sum(triple) )

print( len(results), abs(max(results)) )