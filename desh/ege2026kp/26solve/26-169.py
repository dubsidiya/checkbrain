with open('26-169.txt') as F:
  N, M, K = map(int, F.readline().split())
  rows = {}
  cols = {}
  housePos = []
  for i in range(N):
    r, c = map(int, F.readline().split())
    if r in rows:
      rows[r].append( c )
    else:
      rows[r] = [0, c, K+1]
    if c in cols:
      cols[c].append( r )
    else:
      cols[c] = [0, r, M+1]
    housePos.append( [r, c, 0] )

for r in rows:
  rows[r].sort()
for c in cols:
  cols[c].sort()

for i, h in enumerate(housePos):
  r, c, count = h
  ind = rows[r].index(c)
  viewed = c - rows[r][ind-1] - 1 + \
           rows[r][ind+1] - c - 1
  ind = cols[c].index(r)
  viewed += r - cols[c][ind-1] - 1 + \
            cols[c][ind+1] - r - 1
  h[2] = viewed

print( max( housePos, key=lambda x: (x[2], -x[1], x[0]) ) )
