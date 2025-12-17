with open('27-191b.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

tail = [ [None, None], [None, None] ] # пары (сумма, длина)

minSum = float('inf')
maxLen = 0
total = prevTotal = 0
for i in range(N):
  total += data[i]
  r = total % 2
  rPair = 1 - r
  if tail[rPair][0] is not None:
    curSum = total - tail[rPair][0]
    curLen = i - tail[rPair][1]
    if curSum < minSum or (curSum == minSum and curLen > maxLen):
      minSum = curSum
      maxLen = curLen
  rPrev = prevTotal % 2
  if tail[rPrev][0] is None or prevTotal > tail[rPrev][0]:
    tail[rPrev][0] = prevTotal
    tail[rPrev][1] = i - 1
  prevTotal = total

print( minSum, maxLen )
