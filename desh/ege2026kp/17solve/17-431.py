data = [ int(x) for x in open('17-428.txt').read().split() ]

def sumDigits( n ):
  return sum( map(int, str(n)) )

div13 = [x for x in data if x % 13 == 0][12]
s1 = sumDigits( div13 )

div25 = [x for x in data if x % 25 == 0][24]
s2 = sumDigits( div25 )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if any( 100 <= x < 1000 for x in triple ) and \
     sum( sumDigits(x) == s1 for x in triple ) <= 1 and \
     sum( sumDigits(x) == s2 for x in triple ) >= 2:
     results.append( sum(triple) )

print( len(results), sum(results)/len(results) )

