data = [ int(x) for x in open('17-418.txt').read().split() ]

r11 = min( [ x for x in data if 1000 <= x <= 9999] ) % 11
r3 = max( [ x for x in data if 10 <= x <= 99] ) % 3

N = len(data)
results = []
for i in range(N-1):
  pair = data[i:i+2]
  if any( (x % 7 == r11) for x in pair ) and \
     any( (x % 5 == r3) for x in pair ):
     results.append( sum(pair) )

print( len(results), max(results) )
