
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return -1 if x < 5 or x > 20 else \
          0 if y < 15 else \
          1 if x > 10 and y > 20 else \
          2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-96b.txt"):
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

"""
iMin = min( [i for i in range(K)],
            key = lambda x: len(clusters[x]) )
iMax = max( [i for i in range(K)],
            key = lambda x: len(clusters[x]) )
"""
iMin = iMax = 0
for i in range(1,K):
  if len(clusters[i]) < len(clusters[iMin]):
    iMin = i
  if len(clusters[i]) > len(clusters[iMax]):
    iMax = i

Qx = centers[iMax][0] - centers[iMin][0]
Qy = centers[iMax][1] - centers[iMin][1]

print( int(abs(Qx)*10_000), int(abs(Qy)*10_000) )

