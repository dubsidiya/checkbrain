with open('27-162b.txt') as F:
  N, K = map(int, F.readline().split() )
  N = N*1000//53915
  K = N // 4
  with open('27-162bb.txt','w') as Fout:
    print( N, K, file=Fout )
    for i in range(N):
      Fout.write( F.readline() )

