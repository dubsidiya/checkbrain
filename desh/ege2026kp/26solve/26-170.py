with open('26-170.txt') as F:
  N = int(F.readline())
  data = set()
  for _ in range(N):
    ID, no = map(int, F.readline().split())
    if (ID, no) not in data:
      data.add( (ID, no) )

data = sorted(data)
N = len(data)

maxCount = 0
count = 1
for i in range(1,N):
  if data[i][0] == data[i-1][0] and data[i][1] == data[i-1][1]+2:
    count += 1
    if count > maxCount:
      maxCount = count
      ID = data[i][0]
  else:
    count = 1

print( ID, maxCount )
