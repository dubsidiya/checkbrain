with open('27-187a.txt') as F:
  K = int(F.readline())
  N = int(F.readline())
  data = [ int(F.readline()) for i in range(N) ]

count = 0
for i in range(N-2*K):
  s1 = sum( data[i:i+K-1] )
  for j in range(i+K-1, N-K):
    s1 += data[j]
    s2 = sum( data[j+1:j+K] )
    for m in range(j+K,N):
      s2 += data[m]
      if s2 >= s1:
        if s1 == s2:
          count += 1
          #print( data[i:j+1], data[j+1:m+1])
        break

print( count )




