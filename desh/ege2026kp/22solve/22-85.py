with open('22-85.csv') as F:
  data = {}
  sumT = 0
  starting = []
  for s in F.readlines():
    s = s.replace( '"', '' )
    pid, t, *deps = map( int, s.split(';') )
    if deps == [0]: starting.append( pid )
    sumT += t
    data[pid] = [pid, t, [d for d in deps if d]]

TARGET = 4

maxLen = 0
def check():
  global maxLen
  count4 = 0
  for i in range(2*sumT):
    if rasp[i] >= TARGET:
      count4 += 1
      maxLen = max( count4, maxLen )
    else:
      count4 = 0

finish = { d: float('inf') for d in data }
points = [0]
def place( d, pos, direction = 1 ):
  pid, t, deps = d
  for k in deps:
    if direction == 1 and pos < finish[k]: return False
  if direction == 1:
    points.append( pos )
    points.append( pos+t )
    finish[pid] = pos+t
  else:
    points.pop()
    points.pop()
    finish[pid] = float('inf')
  for i in range(pos, pos+t):
    rasp[i] += direction*1
  return True

def tryVar( chain ):
  for i, p in enumerate(points):
    if points.index(p) == i:
      if place( data[chain[0]], p ):
        if len(chain) == 1:
          check()
        else:
          tryVar( chain[1:] )
        place( data[chain[0]], p, -1 )

from copy import deepcopy

def constructChain( s ):
  chain = [s]
  while True:
    allReady = [ d for d, v in data1.items()
                   if (d not in chain) and v[2] and
                       all( x in chain for x in v[2] ) ]
    if not allReady:
      allReady = [ d for d, v in data1.items() if not v[2] ]
      if allReady: allReady = allReady[:1]
    for nxt in allReady:
      chain.append( nxt )
      del data1[nxt]
    if not data1: break
  return chain

for s in starting:
  data1 = deepcopy( data )
  del data1[s]
  chain = constructChain( s )
  rasp = [0]*(2*sumT)
  tryVar ( chain )

print( maxLen )

