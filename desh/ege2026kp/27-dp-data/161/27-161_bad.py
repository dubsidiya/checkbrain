with open('27-161bb.txt') as F:
    N, V = map(int, F.readline().split())
    data = []
    for _ in range(N):
      P = int(F.readline())
      C = P // V if P % V == 0 else P // V + 1
      data.append( C )

def dist( i, j, d ): # из пункта i в пункт j; d = 1/(-1) - по/против часовой
  if d == 1: # по часовой (j > i)
    if j < i: j += N
  else: # против часовой (j < i)
    if j > i: j -= N
  return abs(i - j)

posLab = []
for i in range(N): # перебор опунктов для лаборатории
  # m1 - пункт для первой машины
  # m2 - пункт для второй машины
  m1 = (i + 1 + N) % N

  while m1 != i: # все возможные положения m1
    m2 = (m1 + 1 + N) % N

    cost1, j = 0, m1
    while j != i:
      cost1 += data[j]*dist(j, i, -1)
      j = (j - 1 + N) % N

    cost2, j = 0, m2
    while j != i:
      cost2 += data[j]*dist(j, i, 1)
      j = (j + 1) % N

    if cost1 == cost2: # нашли!
      posLab.append( (i, m1) )
      break

    m1 = (m1 + 1) % N

print( posLab )
print( max( posLab, key=lambda x: x[0]) )
