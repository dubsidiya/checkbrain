from random import randint, shuffle

with open('27-164b.txt') as F:
  N, K = map(int, F.readline().split() )
  N = N*1000//88622
  K = N // 4
  data = [ s for s in F if s.strip() ]
  ind = list( range(0, len(data)) )
  shuffle( ind )
  ind = sorted(ind[:N])
  print('Writing')
  with open('27-164bb.txt','w') as Fout:
    print( N, K, file=Fout )
    for i in range(N):
      Fout.write( data[ind[i]] )

