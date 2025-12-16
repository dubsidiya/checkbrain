with open('22-122.csv') as F:
  readyToStart = []
  procList = []
  for s in F:
    s = list( map(int, s.replace('"',"").split(";") ) )
    ID, t, *dependsOn = s
    if dependsOn == [0]:
      readyToStart.append( (ID, t) )
    else:
      procList.append( [ID, t, dependsOn] )

LIMIT = 3

from copy import deepcopy
from itertools import combinations

minTotalTime  = float('inf')

def simulate( allProc, readyProc, active = [], started = [], t0 = 0 ):

  def procFinished( pid ):
    for proc in allProc[:]:
      if pid in proc[2]:
        proc[2].remove(pid)
        if not proc[2]:
          readyProc.append( list(proc[:2]) )
          allProc.remove( proc )
    #print( f"t = {t}  finished: {pid}" )
    readyProc.sort()

  global minTotalTime
  while True:
    if not( active or allProc or readyProc ):
      if t0-1 < minTotalTime:
        minTotalTime = t0-1
        print( minTotalTime, *started )
      return t0-1
    for i in range(len(active)-1,-1,-1):
      active[i][1] -= 1
      if active[i][1] == 0:
        procFinished( active[i][0] )
        del active[i]
    if len(active) < LIMIT and readyProc:
      break
    t0 += 1

  nReady = len(readyProc)
  slots = min( nReady, LIMIT - len(active) )

  variantsStart = combinations( range(nReady), slots )

  tMin = float('inf')
  for var in variantsStart:
    _allProc = deepcopy(allProc)
    _readyProc = deepcopy(readyProc)
    _active = deepcopy(active)
    _started = deepcopy(started)
    for i in var:
      _active.append( list(readyProc[i]) )
      _readyProc.remove( readyProc[i] )
      _started.append( (readyProc[i][0], t0) )
    t = simulate( _allProc, _readyProc, _active, _started, t0+1 )
    tMin = min( t, tMin )

  return tMin

t = simulate( procList, readyToStart )

print( t )

