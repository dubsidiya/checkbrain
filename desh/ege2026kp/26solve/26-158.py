with open('26-156.txt') as F:
  N = int(F.readline())
  values = [int(x) for x in F.readline().split()]
  data = []
  for s in F:
    ID, *answers = [int(x) for x in s.split()]
    s = sum( x*values[i]
             for i, x in enumerate(answers) )
    fines = sum( -x*values[i]
             for i, x in enumerate(answers) if x < 0 )
    zeros = sum( 1 for x in answers if x == 0 )
    data.append( (s, fines, zeros, ID) )

data.sort( key = lambda x: (-x[0], x[1], x[2], x[3]) )

N5 = N // 5
n = N5 - 1
while data[n][:3] == data[N5-1][:3]:
  n += 1
print( data[n][3] )

data = [ x for x in data[n:] if x[0] > 0 ]
Nlast = len(data)
Nauto = Nlast // 10

print( sum( x[0] for x in data[:Nauto] )  )

