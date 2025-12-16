"""
=== Три кластера + аномалии ===

Метод: k-средних (k-медоид)

Ответ: 38012 50002
"""
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

data = []
for s in open('27-65b.txt'):
  x, y = s.replace(',','.').split()
  data.append( (float(x), float(y)) )

from timeit import default_timer
t0 = default_timer()

K = 6 # количество кластеров данных + аномалии
centers = [(6.5, 5), (3.5, 9), (1.5, 2),     # полезные данные
           (3.5, 5), (4.5, 2.5), (6.5, 8.5)  # кластеры-аномалии
          ]
oldCenters = []
while centers != oldCenters:
  oldCenters = centers
  clusters = [ [] for i in range(K) ]
  for p in data:
    distToCenters = [ dist(p,center) for center in centers ]
    k = distToCenters.index( min(distToCenters) )
    clusters[k].append( p )
  centers = [ getCenter(cluster) for cluster in clusters ]

# удалить кластеры-аномалии
centers = [ getCenter(cluster) for cluster in clusters
            if len(cluster) > 10 ]

print( "Центры:\n", centers )
print( f"Время: {default_timer()-t0:0.3f} с" )

K = len(centers)  # количество кластеров с полезными данными

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'maroon', 'orange', 'navy']
scale, shiftX, shiftY = 50, 200, 250
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()

