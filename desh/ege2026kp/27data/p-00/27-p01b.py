# Задача Р-01 (И. Воропаев)
# Условие полностью совпадает с условием задачи Р-00 (из демо-варианта 2025 года),
# но «расстояние» между точками вычисляется как квадрат обычного евклидового расстояния.
# В этом случае можно организовать перебор так, чтобы он имел линейную сложность,
# а не квадратичную. Это может быть важно, если точек очень много (скажем, 1 000 000)
# и алгоритм с квадратичной сложностью не закончится за разумное время.

K = 3  # количество кластеров

def findClusterNo( x, y ):
  return 0 if y < 3 else \
         1 if x < 5 else \
         2

#------------------------------------------------
# Решение квадратичной сложности
#------------------------------------------------

clusters = [ [] for i in range(K) ]

for s in open('27-p00b.txt'):
  x, y = s.replace(',','.').split()
  x, y = float(x), float(y)
  clusterNo = findClusterNo( x, y )
  clusters[clusterNo].append( (x, y) )

def distKv( p1, p2 ):
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

centers = []
for k in range(K):
  minSumDist = float('inf')
  for pCenter in clusters[k]:
    sumDist = sum( distKv(pCenter,p)
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

#------------------------------------------------
# Решение линейной сложности (К. Поляков)
#------------------------------------------------

centers = []
for k in range(K):
  Sx = sum( x for (x, y) in clusters[k] )
  Sy = sum( y for (x, y) in clusters[k] )
  Q =  sum( x*x + y*y for (x, y) in clusters[k] )
  N = len( clusters[k] )
  minSumDist = float('inf')
  for pCenter in clusters[k]:
    xc, yc = pCenter
    Ac = N*(xc*xc + yc*yc)
    sumDist = Ac - 2*(xc*Sx + yc*Sy)
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

#------------------------------------------------
# Решение линейной сложности (И. Воропаев)
#------------------------------------------------

def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]

    n = len(cluster)
    sum_x = sum([x for x, y in cluster])
    sum_y = sum([y for x, y in cluster])
    sum_kv_x_y = sum([x**2 + y**2 for x, y in cluster])
    for x, y in cluster:
        cur_sum = ((x**2+y**2) * n) + sum_kv_x_y - 2*x*sum_x - 2*y*sum_y
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x, y]
    return centre


# По графику видим, что есть два кластера.
cluster_A = []
cluster_B = []
cluster_C = []
with open('27-p00b.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if y < 3:  # Разделяем точки на три кластера
            cluster_A.append([x, y])
        elif x < 5:
            cluster_B.append([x, y])
        else:
            cluster_C.append([x, y])

centre_A = find_centre(cluster_A)  # Находим центр первого кластера
centre_B = find_centre(cluster_B)  # Находим центр второго кластера
centre_C = find_centre(cluster_C)  # Находим центр второго кластера

# Вычисляем ответ
Px = (centre_A[0] + centre_B[0] + centre_C[0]) / 3
Py = (centre_A[1] + centre_B[1] + centre_C[1]) / 3

print(int(Px*10_000), int(Py*10_000))