data = []
for s in open('9-178.csv'):
   a, b, c = map( int, s.split(';') )
   data.append( (a, b, c ) )

def isCube( n ):
  q = round(n**(1/3))
  return q*q*q == n

count = 0
for d in data:
  count += len(d) == len(set(d)) and \
           ( isCube(d[0]*d[1]) or
             isCube(d[1]*d[2]) or
             isCube(d[2]*d[0])  )
print( count )