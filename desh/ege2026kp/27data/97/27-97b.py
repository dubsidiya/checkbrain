
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return -1 if x < 0 or x > 30 else \
          0 if x < 14 else \
          1 if x > 19 else \
          2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-97b.txt"):
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

dists = [ dist(c1, c2)
          for c1 in centers
          for c2 in centers if c1 != c2 ]

Q1 = min(dists)
Q2 = max(dists)

print( int(abs(Q1)*10_000), int(abs(Q2)*10_000) )

