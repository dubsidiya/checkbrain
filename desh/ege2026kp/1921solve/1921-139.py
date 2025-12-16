TARGET = 227
def gameOver( pos ):
  return sum(pos) >= TARGET
def next( pos ):
  x, y = pos
  return (x+1,y), (x*2,y), (x,y+1), (x,y*2)

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

from math import ceil
N1 = 17
print( '19)', ceil((TARGET-N1)/4) )
print( '20)', sorted([ s for s in range(1, TARGET-N1)
                    if win((N1,s), 3) and not win((N1,s), 1) ]) )
print( '21)', sorted([ s for s in range(1, TARGET-N1)
                    if win((N1,s), 4) and not win((N1,s), 2) ]) )

