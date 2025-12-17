with open('27-180a.txt') as F:
  N = int(F.readline())
  data = [ int(s) for s in F ]

count = 0
for i in range(N):
  s = 0
  p = n = 0
  for j in range(i, N):
    p += data[j] > 0
    n += data[j] < 0
    #if p == n: print( data[i:j+1] )
    count += p == n

print( count )