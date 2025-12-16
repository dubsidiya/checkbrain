"""
Ответ:
Кластеры:
551
1046
367
3036
Центр: (0.9934667540258988, 5.997879553744169) Радиус: 0.9719698343352691
Центр: (4.9944026787857885, 5.001393902971468) Радиус: 1.3468364128518666
Центр: (6.00137786705748, 1.0014717347488027) Радиус: 0.7805565508298311
Центр: (0.9917894375536506, 0.9998422363154772) Радиус: 2.301648001081451
Время: 2.245 с
13502
"""
def clusterNo( x, y ):
  return 0 if x < 3 and y > 4 else \
         1 if x > 3 and y > 3 else \
         2 if x > 4 else \
         3

K = 4 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-74b.txt'):
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
scale, shiftX, shiftY = 50, 100, 150
for i, cluster in enumerate(clusters):
  for x, y in cluster:
    goto( x*scale-shiftX, y*scale-shiftY )
    dot( 3, colors[i] )
done()
