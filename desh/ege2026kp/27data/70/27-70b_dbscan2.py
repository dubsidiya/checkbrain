"""
=== Три кластера сложной формы ===

Метод: кластеризация слиянием (DBSCAN-2).

Ответ: 34461 47809
"""
data = []
for s in open('27-70b.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

def getCenter( cluster ):
  minSumDist = float('inf')
  for pCenter in cluster:
    sumDist = sum( math.dist(pCenter,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  return center

eps = 0.3

from timeit import default_timer
t0 = default_timer()
print( "Кластеры:" )
clusters = []
for p in data:
  clusters.append( [p] )
  for cluster in clusters[:-1]:
    if any( math.dist(x,p) < eps for x in cluster ):
      clusters[-1] += cluster
      clusters.remove( cluster )

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )
print( f"Разбиение на кластеры: {default_timer()-t0:0.3f} с" )

K = len(clusters)

t0 = default_timer()
centers = [ getCenter(cluster) for cluster in clusters ]
print( "Центры:\n", centers )
print( f"Поиск центров: {default_timer()-t0:0.3f} с" )

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 50, 200, 250
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
