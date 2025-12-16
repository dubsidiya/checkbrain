def gameOver( pos ):
  return pos <= 87
def moves( pos ):
  return pos-2, pos//2

def win1( pos ):
  return not gameOver(pos) and \
         any( gameOver(m) for m in moves(pos) )

def lose1( pos ):
  return all( win1(m) for m in moves(pos) )

def win2( pos ):
  return not win1(pos) and \
         any( lose1(m) for m in moves(pos) )

def lose2( pos ):
  return all( win1(m) or win2(m) for m in moves(pos) ) and \
         any( win2(m) for m in moves(pos) )

print( '19)', [ x for x in range(88, 1000) if lose1(x) ] )
print( '20)', [ x for x in range(88, 1000) if win2(x) ] )
print( '21)', [ x for x in range(88, 1000) if lose2(x) ] )
