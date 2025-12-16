data = [ int(x) for x in open('17-418.txt').read().split() ]

r5 = min( [ x for x in data if 6**3 <= x < 6**4] ) % 5
r13 = min( [ x for x in data if 9**2 <= x < 9**3] ) % 13

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if sum( (x % 11 == r5) for x in triple ) == 1 and \
     sum( (x % 7 == r13) for x in triple ) == 1:
     results.append( sum(triple) )

print( len(results), min(results) )

