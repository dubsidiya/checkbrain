with open('27-171b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

D = 111

tails = [0]*D
tails[0] = 1

totalSum = prevSumK = 0
count = 0
for i in range(N):
  totalSum += data[i]
  r = totalSum % D
  if i >= K-1:
    count += tails[r]
    prevSumK += data[i-K+1]
    tails[prevSumK % D] += 1

print( count )
