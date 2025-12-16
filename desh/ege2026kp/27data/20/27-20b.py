
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if y > 0.5 and x < 8.5 else \
         1 if y > -x+9.3 else \
         2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-20b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
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

print( int(sumX/K*10000), int(sumY/K*10000) )

