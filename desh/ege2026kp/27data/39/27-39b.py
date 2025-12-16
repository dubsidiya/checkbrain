
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if (1 < x < 10 and y < 2.6) or (7 < x < 10 and 2 < y < 4) else \
         1 if (4 < x < 12 and 2.6 < y < 6) or (5 < x < 12 and 4 < y < 7.2)  else \
         2 if 1 < x < 10 and 4 < y < 12  else \
        -1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-39b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

import math
def dist( p1, p2 ):
  #return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

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

print( "Центроиды:\n", centers )

sumX, sumY = 0, 0
for k in range(K):
  sumX += centers[k][0]
  sumY += centers[k][1]

print( int(sumX/K*100_000), int(sumY/K*100_000) )

