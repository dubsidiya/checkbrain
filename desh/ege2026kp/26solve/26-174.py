with open('26-174.txt') as F:
  N = int(F.readline())
  data = set()
  for i in range(N):
    no, point  = map(int, F.readline().split())
    data.add( (point, no) )

data = sorted( data )

maxCount = count = 0
prevPoint = prevNo = -1
for point, no in data:
  if point != prevPoint or no != prevNo+1:
    count = 1
  else:
    count += 1
    if count > maxCount:
      maxCount = count
      maxPoint = point
  prevPoint, prevNo = point, no

print( maxCount, maxPoint )

