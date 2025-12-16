
K = 2  # количество кластеров

def findClusterNo( x, y ):
  return 0 if y > 10 else \
         1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-98a.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

from math import dist

centers = []
for k in range(K):
  minSumDist = float('inf')
  for pCenter in clusters[k]:
    sumDist = sum( dist(pCenter,p)
                   for p in clusters[k] )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  centers.append( center )

print( "Центры:\n", centers )

Px = sum( c[0] for c in centers )
Py = sum( c[1] for c in centers )
print( int(abs(Px)*10_000), int(abs(Py)*10_000) )

