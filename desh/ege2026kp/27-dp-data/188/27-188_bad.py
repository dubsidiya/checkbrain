with open('27-188a.txt') as F:
  N = int(F.readline())
  position = [ int(F.readline()) for i in range(N) ]

position.sort()

data = []
for i in range(N-1):
  data.append( position[i+1] - position[i] )

def minLength( data, pos = 0, prev = False ):
  if not data: return 0
  if pos == len(data)-1:
    return data[pos]
  if prev:
    return min( data[pos] + minLength( data, pos+1, True ),
                minLength( data, pos+1, False ))
  else:
    return data[pos] + \
           minLength( data, pos+1, True )

print( data[0] + minLength(data, 1, True) )

print( data )
N = len(data)
sMin = float('inf')
for i in range(2**(N-1)+1, 2**N, 2):
  bits = f'{i:0{N}b}'
  if bits[0] == '1' and bits[-1] == '1' and '00' not in bits:
    f = list( map(int, list(bits)) )
    s = 0
    for i in range(N):
      s += f[i] * data[i]
    if s < sMin:
      sMin = s
      print( s, [ data[i] for i in range(N) if f[i] ] )

print( sMin )


