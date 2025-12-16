with open('26-171.txt') as F:
  N = int(F.readline())
  data = []
  for _ in range(N):
    t, a, b, startOp = F.readline().split()
    if startOp == 'A':
      data.append( (int(t), [0, int(a)], [1, int(b)]) )
    else:
      data.append( (int(t), [1, int(b)], [0, int(a)]) )

tFree = [ 0, 0 ]
queues = [ [], [] ]
countQueued = [ 0, 0 ]
while data:
  data.sort( reverse=True, key=lambda x: x[0] )
  ti, *ops = data.pop()
  k, opTime = ops[0]
  if tFree[k] <= ti:
    tFree[k] = ti + opTime
  else:
    countQueued[k] += 1
    tFree[k] += opTime
  if len(ops) > 1:
    data.append( (tFree[k], ops[1]) )

print( f"A: {countQueued[0]} {tFree[0]}" )
print( f"B: {countQueued[1]} {tFree[1]}" )


# Автор: А. Кабанов

print( '----------------------------------' )

with open('26-171.txt') as F:
  N = int(F.readline())
  a = []
  for i in range(N):
    st, da, db, t = F.readline().split()
    a.append( [int(st), int(st), int(da), int(db), t, 1] )

a.sort()
qA = []
qB = []
ans1 = ans2 = 0
while a:
  st, post, da,	db,	t, n = a.pop(0)
  qA = [x for x	in qA if x>st]
  qB = [x for x	in qB if x>st]
  if t == 'A':
    if len(qA)==0:
      end = st + da
    else:
      end = max(qA) + da
      ans1 += 1
    qA.append(end)
  else:
    if len(qB) == 0:
      end = st + db
    else:
      end = max(qB) + db
      ans2 += 1
    qB.append(end)
  if n == 1:
     a.append( [end, post, da, db,
                'B' if t == 'A' else 'A', 2] )
     a.sort()

print( f"A: {ans1} {max(qA)}" )
print( f"B: {ans2} {max(qB)}" )

