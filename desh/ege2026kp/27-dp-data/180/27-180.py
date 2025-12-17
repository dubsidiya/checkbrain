with open('27-180b.txt') as F:
  N = int(F.readline())
  data = [ int(s) for s in F ]

diff = 0
nDiff = { 0: 1 }
count = 0
for i in range(N):
  diff += (data[i] > 0) - (data[i] < 0)
  count += nDiff.get( diff, 0 )
  nDiff[diff] = nDiff.get( diff, 0 ) + 1

print( count )