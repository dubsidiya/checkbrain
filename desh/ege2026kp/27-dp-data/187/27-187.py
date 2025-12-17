# Автор: Е. Джобс
# https://www.youtube.com/watch?v=w7du6qYh4TQ&t=11425s

with open('27-187b.txt') as F:
  K = int(F.readline())
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

p = [0]*(N+1)
for i in range(1,N+1):
  p[i] = p[i-1] + data[i-1]

count = 0
for i in range(N):
  mStart = i + 2*K
  for j in range(i+K, N):
    s1 = p[j] - p[i]
    for m in range(mStart, N+1):
      s2 = p[m] - p[j]
      if s2 >= s1:
        if s1 == s2:
          count += 1
        mStart = max( m, j+K+1 )
        break

print( count )




