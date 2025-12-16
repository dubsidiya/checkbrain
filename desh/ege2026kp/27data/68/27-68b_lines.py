"""
=== Четыре кластера треугольной формы + аномалии ===

Метод: ручное выделение кластеров с помощью условий.

Ответ: 29252 50442
"""
def clusterNo( x, y ):
  return 0 if y > -0.02*x+6.05 and x > 3.8 and y < -x+13 else \
         1 if y > 1.5*x-5 and y < 3.8*x-8.5 and y < -x+13 else \
         2 if y > 3.8*x-8.5 and y > -x and y < 0.25*x+4.9 else \
         3 if x < 4 and y > 0.25*x+4.9 and y < 0.7*x+6.5 else \
        -1

K = 4 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-68b.txt'):
  x, y = s.replace(',','.').split()
  x, y = float(x), float(y)
  k = clusterNo( x, y )
  if k >= 0:
    clusters[k].append( (x, y) )

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

print( "Кластеры:" )
for cluster in clusters:
  print( len(cluster) )

from timeit import default_timer
t0 = default_timer()
centers = [ getCenter(cluster) for cluster in clusters ]

print( "Центры:\n", centers )
print( f"Время: {default_timer()-t0:0.3f} с" )

Px = sum( centers[k][0] for k in range(K) ) / K
Py = sum( centers[k][1] for k in range(K) ) / K

print( int(Px*10000), int(Py*10000) )

from turtle import *
tracer(0)
up()
hideturtle()
colors = ['red', 'green', 'blue', 'magenta', 'brown', 'cyan']
scale, shiftX, shiftY = 50, 150, 200
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
