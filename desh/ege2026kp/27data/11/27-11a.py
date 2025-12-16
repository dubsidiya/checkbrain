
K = 2  # количество кластеров

def findClusterNo( x, y ):
  return 0 if y < 2*x-1 else 1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-11a.txt"):
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

#------------------------------------------------
# Метод k-средних
#------------------------------------------------

def findNearest( p0, data ):
  return sorted( (dist(p0, p), p) for p in data )[0][1]

from random import random
centers = [ (x+random()*2, y+random()*2) for x, y in centers ]
centers = [ findNearest(centers[k], clusters[k]) for k in range(K) ]
for _ in range(20):
  allData = sum( (x for x in clusters), [] )
  clusters = [ [] for _ in range(K) ]
  for p in allData:
    pCenter = findNearest(p, centers)
    clusters[centers.index(pCenter)].append( p )
  for k in range(K):
    lenK = len(clusters[k])
    centers[k] = sum( x for x, y in clusters[k] ) / lenK, \
                 sum( y for x, y in clusters[k] ) / lenK
    centers[k] = findNearest(centers[k], clusters[k])

sumX, sumY = 0, 0
for k in range(K):
  sumX += centers[k][0]
  sumY += centers[k][1]

print( "\nМетод k-средних дает НЕВЕРНЫЙ ответ" )
print( "Центроиды:\n", centers )

print( int(sumX/K*10000), int(sumY/K*10000) )