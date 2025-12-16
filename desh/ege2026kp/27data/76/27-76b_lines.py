"""
Ответ:
Кластеры:
406
1329
2033
1232
Центр: (4.0001602490356625, 1.1688948002425161) Радиус: 1.1410562181829338
Центр: (7.520350209503722, 4.710917754314405) Радиус: 2.0762357677626393
Центр: (4.014915179649231, 9.679423697976402) Радиус: 2.5761014813481626
Центр: (0.46873802802845166, 4.716905838607473) Радиус: 1.9974313061504405
Время: 1.582 с
19477
"""
def clusterNo( x, y ):
  return 0 if y < x+1 and y < -x+8 else \
         1 if y < x+1 and y > -x+8  else \
         2 if y > -x+9 else \
         3

K = 4 # количество кластеров
clusters = [ [] for i in range(K) ]

for s in open('27-76b.txt'):
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
