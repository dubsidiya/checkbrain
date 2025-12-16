"""
Кластеры:
932
1125
1945
998
Центр: (7.673332324197239, 1.178918748798592) Радиус: 1.8832418499235348
Центр: (11.211220224898213, 4.692113100587068) Радиус: 2.068133066014385
Центр: (7.655576526646591, 9.671436055775043) Радиус: 2.7438105029616127
Центр: (4.13368182827352, 4.739503699166459) Радиус: 1.9794280542047518
Время: 1.492 с
21686
"""
def clusterNo( x, y ):
  return 0 if y < x-3 and y < -x+12 else \
         1 if y < x-3 and y > -x+12  else \
         2 if y > -x+12 else \
         3

K = 4 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-78b.txt'):
  x, y = s.replace(',','.').split()
  x, y = float(x), float(y)
  k = clusterNo( x, y )
  if k >= 0:
    clusters[k].append( (x, y) )

import math

def getRadius( cluster ):
  minSumDist = float('inf')
  for pCenter in cluster:
    sumDist = sum( math.dist(pCenter,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
      radius = max( math.dist(pCenter,p) for p in cluster)
  return center, radius

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )

from timeit import default_timer
t0 = default_timer()
centerRad = [ getRadius(cluster) for cluster in clusters ]

for c in centerRad:
  print( f"Центр: {c[0]} Радиус: {c[1]}" )

print( f"Время: {default_timer()-t0:0.3f} с" )

avR = sum( centerRad[k][1] for k in range(K) ) / K

print( int(avR*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 40, 250, 250
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
