"""
Ответ:

"""
def clusterNo( x, y ):
  return 0 if x > 6 and y < 4 else \
         1 if y < 2 else \
         2 if y > -x+10 else \
         3

K = 4 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-75b.txt'):
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
scale, shiftX, shiftY = 40, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
