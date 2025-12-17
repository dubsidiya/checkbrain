with open('27-190a.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

maxVal = float('-inf')
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if data[i] > data[j] and data[k] > data[j]:
        v = data[i] - data[j] + data[k] - data[j]
        if v > maxVal:
          #print( data[i], data[j], data[k], v )
          maxVal = v

print( maxVal )
