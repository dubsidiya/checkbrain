from math import dist

K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if dist( (x, y), (2, 3) ) < 3.1 else \
         1 if dist( (x, y), (10, 3) ) < 3.1 else \
         2 if dist( (x, y), (6, 10) ) < 3.1 else \
        -1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-94b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )

centers = []
for cluster in clusters:
  N = len(cluster)
  cx = sum( p[0] for p in cluster ) / N
  cy = sum( p[1] for p in cluster ) / N
  pMid = (cx, cy)
  delta = 0.1
  ptsNearCenter = [p for p in cluster
              if dist(pMid,p) < delta ]
  minSumDist = float('inf')
  for pCenter in ptsNearCenter:
    sumDist = sum( dist(pCenter,p)
                   for p in cluster )
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

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 30, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
