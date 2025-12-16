"""
=== Два кластера треугольной формы + аномалии ===

Метод: DBSCAN. Разбиение на кластеры с мнимыми аномалиями, которые не влияют на результат.

Ответ: 35646 -5461
"""

data = []
for s in open('27-68a.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

import math
def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

eps = 0.3

# Нерекурсивная версия
def getCluster( p0, eps ):
  data.remove( p0 )
  cluster = [ p0 ]
  for p in cluster:
    neighbors = [ n for n in data
                    if math.dist(n, p) < eps ]
    cluster += neighbors
    for n in neighbors:
      data.remove( n )
  return cluster

def getCenter( cluster ):
  minSumDist = float('inf')
  for pCenter in cluster:
    sumDist = sum( math.dist(pCenter,p)
                   for p in cluster )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  return center

from timeit import default_timer
t0 = default_timer()
print( "Кластеры:" )
clusters = []
while data:
  cluster = getCluster( data[0], eps )
  clusters.append( cluster )
  print( len(cluster) )
print( f"Разбиение на кластеры: {default_timer()-t0:0.3f} с" )

clusters = [ cluster for cluster in clusters
                     if len(cluster) > 10 ]

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
colors = ['red', 'green', 'blue', 'orange', 'cyan', 'magenta']
scale, shiftX, shiftY = 50, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
