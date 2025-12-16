data = []
for s in open('9-180.csv'):
   a, b, c, d = map( int, s.split(';') )
   data.append( (a, b, c, d ) )

def sumSum( a, b, c, d ):
  return ( a + b + c +
           a + b + d +
           a + c + d +
           b + c + d )

ma = 0
for d in data:
  if len(d) != len(set(d)):
    ma = max( ma, sumSum( *d ) )
print( ma )