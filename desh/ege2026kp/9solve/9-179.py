data = []
for s in open('9-178.csv'):
   a, b, c = map( int, s.split(';') )
   data.append( (a, b, c ) )

def isTupoi( c, a, b ):
  return c < a+b and c > a-b and c*c > a*a+b*b

count = 0
for d in data:
  count += isTupoi( *sorted(d, reverse=True) )
print( count )