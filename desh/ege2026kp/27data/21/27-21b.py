
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if x < 5 and y > 5 else \
         1 if x > 7 and 2 < y < 7 else \
         2 if 1.8 < x < 6 and y < 5 else \
         -1

#------------------------------------------------

clusters = [ [] for i in range(K) ]

print( "Аномалии:" )
for s in open("27-21b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    if clusterNo >= 0:
      clusters[clusterNo].append( (x, y) )
    else:
      print( f"({x:0.3}, {y:0.3})" )

import math
def dist( p1, p2 ):
  #return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
  return math.hypot( p1[0] - p2[0], p1[1] - p2[1] )

def findMinMaxDistance( cl1, cl2 ):
   global dMin, dMax
   N1, N2 = len(cl1), len(cl2)
   for i in range(N1):
     for j in range(N2):
       d = dist( cl1[i], cl2[j] )
       dMin = min(d, dMin)
       dMax = max(d, dMax)

dMin, dMax = float('inf'), 0
for i in range(K):
  for j in range(i+1,K):
    findMinMaxDistance( clusters[i], clusters[j] )

print( f"dMin = {dMin},  dMax = {dMax}" )

print( int(dMin*10000), int(dMax*10000) )

