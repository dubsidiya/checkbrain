data = [ int(x) for x in open('17-428.txt').read().split() ]

"""
n = 15
count = 0
while True:
  N = sum( 1 for x in data if x % n == 0 )
  if 10 < N < 20:
    print( n )
    count += 1
    if count > 100: break
  n += 1
print( n )
"""

s1 = sum( 1 for x in data if x % 531 == 0 )
s2 = sum( 1 for x in data if x % 773 == 0 )

print( s1, s2 )

def sumDigits( n ):
  return sum( map(int, str(n)) )

N = len(data)
results = []
for i in range(N-2):
  triple = data[i:i+3]
  if any( 100 <= x < 1000 for x in triple ) and \
     sum( sumDigits(x) == s1 for x in triple ) <= 1 and \
     sum( sumDigits(x) == s2 for x in triple ) >= 2:
     results.append( sum(triple) )

print( len(results), sum(results)/len(results) )

