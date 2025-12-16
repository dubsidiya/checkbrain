with open('26-173.txt') as F:
  K = int(F.readline())
  N = int(F.readline())
  data = []
  for i in range(N):
    tStart, tEnd  = map(int, F.readline().split())
    data.append( (tStart, tEnd) )

data.sort()

tFree = [0]*K

count = 0
for tStart, tEnd in data:
  for k in range(K):
    if tStart >= tFree[k]:
      tFree[k] = tEnd + 1
      count += 1
      lastWindow = k + 1
      break

print( count, lastWindow )

