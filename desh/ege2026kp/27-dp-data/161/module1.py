from random import randint

with open('27-161b.txt') as F:
   N, V = map( int, F.readline().split() )
   data = [int(x) for x in F]

def dist( i, j, d ): # из пункта i в пункт j; d = 1/(-1) - по/против часовой
  if d == 1: # по часовой (j > i)
    if j < i: j += N
  else: # против часовой (j < i)
    if j > i: j -= N
  return abs(i - j)

def sumDist0( i, d ):  # из пункта i в пункт j; d = 1/(-1) - по/против часовой
  cost, j = 0, i
  while j != 0:
    cost += data[j]*dist(j, 0, d)
    if d < 0:
      j = (j - 1 + N) % N
    else:
      j = (j + 1) % N
  return cost

N = N*1000//5252
m1 = N//2 + 1
m2 = m1 + 1
data = [randint(1,10000//V) for i in range(N)]

diff = sumDist0(m1, -1) - sumDist0(m2, 1)
print( diff )
while diff < 0: # добавление в первый промежуток
  shift = randint(1,min(-diff,m1))
  k = randint(1,10)
  if diff + shift*k <= 0 and data[shift] + k < 10000:
    data[shift] += k
    diff += shift*k

while diff > 0: # добавление во второй промежуток
  shift = randint(1,min(diff,N-m2))
  k = randint(1,10)
  if diff - shift*k >= 0 and data[-shift] + k < 10000:
    data[-shift] += k
    diff -= shift*k

print( sumDist0(m1, -1) )
print( sumDist0(m2, 1) )

data = [ x*V-randint(0,V-1) for x in data ]

with open('27-161bb.txt', 'w') as Fout:
  print( N, V, file=Fout )
  shift = randint(N//5, N//3)
  data = data[shift:] + data[:shift]
  for d in data:
    print( d, file=Fout )
