"""
=== Два кластера сложной формы + аномалии ===

Метод: ручное выделение кластеров с помощью условий.

Ответ: 39723 45534
"""
def clusterNo( x, y ):
  return 0 if y > -x+8.5 and not( x > 6 and y > 7) else \
         1 if y < -x+8.5 and not( x < 1 and y < 3)  else \
        -1

K = 2 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-72a.txt'):
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
scale, shiftX, shiftY = 30, 150, 150
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
