from math import ceil
def gameOver( x ):
  return sum(x) < 2

def moves( p ):
  x, y = p
  nextMoves = []
  if x >= 1: nextMoves.append( (x-1,y) )
  if x >= 2: nextMoves.append( (x-2,y) )
  if y >= 1: nextMoves.append( (x,y-1) )
  if y >= 2: nextMoves.append( (x,y-2) )
  return nextMoves

def win1( x ): # выигрыш, сделав не более 1 хода
  return not gameOver(x) and \
         any( gameOver(y) for y in moves(x) )

def lose1( x ): # проигрыш, сделав не более 1 хода
  return all( win1(y) for y in moves(x) )

def win2( x ):
  return not win1(x) and \
         any( lose1(y) for y in moves(x) )

def lose2( x ):
  return not win1(x) and not lose1(x) and \
         all( win1(y) or win2(y) for y in moves(x) ) and \
         any( win2(y) for y in moves(x) )

def win3( x ):
  return any( lose2(y) for y in moves(x) )

def loseAny( x ):
  if gameOver(x): return True
  return all( winAny(y) for y in moves(x) )

def winAny( x ):
  if gameOver(x): return False
  return any( loseAny(y) for y in moves(x) )

ans19 = 0
pos = []
for x in range(1,9):
  for y in range(1,9):
    if any( win1((x1,y1)) for x1, y1 in moves((x,y)) ):
      ans19 = max( x+y, ans19 )
      pos.append( (x,y) )

print( '19)', ans19, sorted(pos) )

ans20 = []
pos = []
for x in range(1,9):
  for y in range(1,9):
    if win3((x,y)):
      ans20.append( x+y )
      pos.append( (x,y) )

print( '20)', min(ans20), max(ans20), sorted(pos) )

ans21 = 0
pos = []
for x in range(1,9):
  for y in range(1,9):
    if not gameOver((x,y)) and loseAny((x,y)):
      ans21 += 1
      pos.append( (x,y) )

print( '21)', ans21, sorted(pos) )

