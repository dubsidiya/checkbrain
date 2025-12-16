def dist( p1, p2 ):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

data = []
with open('50/27-50b.txt') as F:
  F.readline()
  for s in F:
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    data.append( (x, y) )

minDistBetweenClusters = 1
def getNeighbours( p0 ):
  cluster = []
  for i, p in enumerate(data):
    if dist(p0, p) < minDistBetweenClusters:
      cluster.append(p)
      del data[i]
  for i in range(1,len(cluster)):
    cluster = cluster + getNeighbours(cluster[i])
  return cluster

clusters = []
while data:
  p0 = data.pop()
  cluster = [p0] + getNeighbours( p0 )
  if len(cluster) > 10:
    clusters.append( cluster)

K = len(clusters)
centers = []
for k in range(K):
  minSumDist = float('inf')
  for pCenter in clusters[k]:
    sumDist = sum( dist(pCenter,p)
                   for p in clusters[k] )
    if sumDist < minSumDist:
      minSumDist = sumDist
      center = pCenter
  centers.append( center )

print( "Центроиды:\n", centers )

sumX, sumY = 0, 0
for k in range(K):
  sumX += centers[k][0]
  sumY += centers[k][1]

print( int(sumX/K*100_000), int(sumY/K*100_000) )

