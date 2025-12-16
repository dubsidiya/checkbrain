data = [ int(x) for x in open('17-418.txt').read().split() ]

r11 = min( [ x for x in data if 1000 <= x <= 9999] ) % 11
r3 = min( [ x for x in data if 10 <= x <= 99] ) % 3

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if sum( (x % 7 == r11) for x in triple ) == 1 and \
     sum( (x % 5 == r3) for x in triple ) == 1:
     results.append( sum(triple) )

print( len(results), min(results) )

