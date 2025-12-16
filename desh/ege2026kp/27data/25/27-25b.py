
K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if x > 3 else \
         1 if y < -2 else \
         2

#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open("27-25b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    clusterNo = findClusterNo( x, y )
    clusters[clusterNo].append( (x, y) )

def dist( p1, p2 ):
  return max( abs(p1[0] - p2[0]), abs(p1[1] - p2[1]) )

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

print( int(sumX/K*10000), int(sumY/K*10000) )


#---------------------------------------------
# Авторы: В. Ланская, Р. Ягафаров

f = open('27-25b.txt')
f.readline()
roots = [list(map(float, s.replace(",", ".").split())) for s in f]
clusters = [[], [], []]
for x, y in roots:
    if x < 3 and y < -3:
        clusters[0].append((x, y))
    elif x < 3 and y > -3:
        clusters[1].append((x, y))
    else:
        clusters[2].append((x, y))
best_centroids = [[] for i in range (len(clusters))]
for i in range (len(clusters)):
    min_dist = 10**10
    for x1, y1 in clusters[i]:
        dist = 0
        for x2, y2 in clusters[i]:
            chebyshev_dist = max(abs(x2 - x1), abs(y2 - y1))
            dist += chebyshev_dist
        if dist < min_dist:
            min_dist = dist
            best_centroids[i] = [x1, y1]
P_x = sum([x / len(clusters) for x, y in best_centroids]) * 10_000
P_y = sum([y / len(clusters) for x, y in best_centroids]) * 10_000
print(int(P_x), int(P_y))

