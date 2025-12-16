from math import ceil
def gameOver( x ):
  return sum(x) > 7

def moves( p ):
  x, y = p
  return (x+1,y), (x,y+1), (x+2,y), (x,y+2)

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

ans19 = 0
a = []
for x in range(0,8):
  for y in range(0,8):
    if any( win1((x1,y1)) for x1, y1 in moves((x,y)) ):
      ans19 += 1
      a += [(x,y)]

print( '19)', ans19, sorted(a) )

a = []
for x in range(0,8):
  for y in range(0,8):
    if win3((x,y)):
      a.append( x+y )

print( '20)', min(a), max(a) )

ans21 = 0
a = []
for x in range(0,8):
  for y in range(0,8):
    if lose1((x,y)) or lose2((x,y)):
      ans21 += 1
      a += [(x,y)]
print( '21)', ans21, sorted(a) )
