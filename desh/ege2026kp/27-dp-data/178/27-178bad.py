with open('27-178a.txt') as F:
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

sMax = float('-inf')
data = data + data
for i in range(N):
  s = 0
  for j in range(i,i+N):
    s += data[j]
    if s > sMax: sMax = s

print( sMax )
