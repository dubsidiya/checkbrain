data = [ int(x) for x in open('17-418.txt').read().split() ]

r3, r11 = min(data) % 3, max(data) % 11

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if sum( (x % 3 == r11) for x in triple ) == 1 and \
     sum( (x % 11 == r3) for x in triple ) == 1:
     results.append( sum(triple) )

print( len(results), min(results) )

