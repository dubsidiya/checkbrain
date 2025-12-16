with open('26-150.txt') as F:
  N, M, K = [int(x) for x in F.readline().split()]
  minOccupiedInRow = [float('inf')]*(K+1)
  for i in range(N):
    row, place = [int(x) for x in F.readline().split()]
    minOccupiedInRow[place] = min(minOccupiedInRow[place], row)

results = []
for place in range(1,K):
  freeRow = min(minOccupiedInRow[place:place+2]) - 1
  results.append( (freeRow, place+1) )

results.sort( reverse = True )

print( results[0] )

print( '----------------------------------------' )

with open('26-150.txt') as F:
  N, M, K = [int(x) for x in F.readline().split()]
  minOccupiedInRow = [float('inf')]*(K+1)
  allOccupied = []
  for i in range(N):
    row, place = [int(x) for x in F.readline().split()]
    allOccupied.append( (row, place) )

minOccupiedInRow = [float('inf')]*(K+1)
for place in range(K+1):
  minOccupiedInRow[place] = min( [x[0] for x in allOccupied if x[1] == place],
                                 default = float('inf') )

result = (0, 0)
for place in range(1, K):
  freeRow = min(minOccupiedInRow[place:place+2]) - 1
  if (freeRow, place+1) > result:
    result = (freeRow, place+1)

print( result )

print( '---------------------------------------' )

# Автор: А. Кабанов

f = open('26-150.txt')
N, M, K = [int(x) for x in f.readline().split()]
min_ryad = [M+1]*(K+1)

for i in range(N):
  r, m = [int(x) for x in f.readline().split()]
  min_ryad[m] = min(min_ryad[m], r)

ans1 = 0
for i in range(1,K):
  ans1 = max(ans1, min(min_ryad[i]-1, min_ryad[i+1]-1))

ans2 = []
for i in range(1,K):
  if min(min_ryad[i]-1, min_ryad[i+1]-1) == ans1:
    ans2.append( i+1 )

print( ans1, max(ans2) )

