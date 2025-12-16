with open('22-128.csv') as F:
  readyToStart = []
  procList = []
  active = []
  for s in F:
    s = list( map(int, s.replace('"',"").split(";") ) )
    ID, t, *dependsOn = s
    if dependsOn == [0]:
      readyToStart.append( [ID, t] )
    else:
      procList.append( [ID, t, dependsOn] )

def finished( ID ):
  for proc in procList[:]:
    if ID in proc[2]:
      proc[2].remove(ID)
      if not proc[2]:
        readyToStart.append( proc[:2] )
        procList.remove( proc )
  print( f"t = {t}  finished: {ID}" )
  readyToStart.sort()

LIMIT = 4
t = 0
while active or procList or readyToStart:
  for i in range(len(active)-1,-1,-1):
    active[i][1] -= 1
    if active[i][1] == 0:
      finished( active[i][0] )
      del active[i]
  while len(active) < LIMIT and readyToStart:
    active.append( readyToStart[0] )
    print( f"t = {t}  start: {active[-1][0]} ")
    del readyToStart[0]
  #print( active, readyToStart )
  t += 1

print( t-1 )
