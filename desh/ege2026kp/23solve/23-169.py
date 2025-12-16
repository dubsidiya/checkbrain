def valid( prog ):
  p = [p for p in range(len(prog)) if prog[p] == prog[0] ]
  if len(p) < 2: return False
  lenCycle = len(prog[:p[1]])
  for i in range(p[1],len(prog)):
    if prog[i] != prog[i-lenCycle]:
       return False
  return True

count = 0
def f( start, prog ):
  global count
  prog = prog + [start]
  if len(prog) == 10:
    if valid(prog):
      print( prog )
      count += 1
    return
  f( start+3, prog )
  f( start-1, prog )

f( 5, [] )
print( count )