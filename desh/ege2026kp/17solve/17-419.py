data = [ int(x) for x in open('17-418.txt').read().split() ]

r3, r11 = min(data) % 3, max(data) % 11

N = len(data)
results = []
for i in range(N-1):
  pair = data[i:i+2]
  if any( (x % 3 == r11) for x in pair ) and \
     any( (x % 11 == r3) for x in pair ):
     results.append( sum(pair) )

print( len(results), max(results) )

