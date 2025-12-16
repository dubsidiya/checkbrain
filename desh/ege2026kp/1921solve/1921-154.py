from math import ceil
def gameOver( x ):
  return x < 6

def moves( x ):
  if x >= 5:
    return x-3, x-5, ceil(x/2)
  if x >= 3:
    return x-3, ceil(x/2)
  return (ceil(x/2), )

def win0( x ): # выигрыш в результате хода соперника
  return gameOver(x) and x % 2 == 0

def lose0( x ): # проигрыш в результате хода соперника
  return gameOver(x) and x % 2 != 0

def lose10( x ): # проигрыш в 1 ход без хода соперника
  return not gameOver(x) and \
         all( win0(y) for y in moves(x) )

def win1( x ): # выигрыш, сделав не более 1 хода
  return not gameOver(x) and \
         any( lose0(y) or lose10(y) for y in moves(x) )

def lose1( x ): # проигрыш, сделав не более 1 хода
  return all( win1(y) or win0(y) for y in moves(x) )

def win2( x ):
  return not win1(x) and not lose1(x) and \
         any( lose1(y) for y in moves(x) )

def lose2( x ):
  return not win1(x) and not lose1(x) and \
         all( win1(y) or win2(y) for y in moves(x) ) and \
         any( win2(y) for y in moves(x) )

#print( 'w0:', [s for s in range(0,100) if win0(s)] )
#print( 'l0:', [s for s in range(0,100) if lose0(s)] )
#print( 'l10:', [s for s in range(0,100) if lose10(s)] )
#print( 'w1:', [s for s in range(3,100) if win1(s)] )
#print( 'l1:', [s for s in range(3,100) if lose1(s)] )

print( '19)', [s for s in range(6,100) if win2(s)] )
print( '20)', [s for s in range(6,100) if lose2(s)] )
print( '21)', [s for s in range(6,100)
                 if  (win1(s) or win2(s)) and
                     any( win1(y) for y in moves(s) )])

