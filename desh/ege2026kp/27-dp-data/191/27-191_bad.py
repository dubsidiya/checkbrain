with open('27.txt') as F:
  N = int(F.readline())
  data = [int(F.readline()) for _ in range(N)]

minS = float('inf')
maxLen = 0
for L in range(N):
  s = data[L]
  for R in range(L+1,N):
    s += data[R]
    if s % 2 == 1:
      if s < minS or (s == minS and R+1-L > maxLen):
        minS = s
        maxLen = R + 1 - L

print( minS, maxLen )
