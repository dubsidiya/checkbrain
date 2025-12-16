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

N4 = N // 4
n = N4 - 1
while data[n][:3] == data[N4-1][:3]:
  n += 1
print( data[n][3] )

print( sum( 1 for x in data if x[:3] == data[1000][:3]) )

