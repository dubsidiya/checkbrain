def isPrime( n ):
  if n < 2: return False
  if n == 2: return True
  return all( n % d != 0 for d in range(2,round(n**0.5)+1) )

def gameOver( pos ):
  return isPrime(pos)

def moves( pos ):
  return pos+1, pos+3, pos*2

def win1( pos ):
  return not gameOver(pos) and \
         any( gameOver(m) for m in moves(pos) )

def lose1( pos ):
  return not gameOver(pos) and all( win1(m) for m in moves(pos) )

def win2( pos ):
  return not win1(pos) and \
         any( lose1(m) for m in moves(pos) )

def lose2( pos ):
  return all( win1(m) or win2(m) for m in moves(pos) ) and \
         any( win2(m) for m in moves(pos) )

print( '19)', [ S for S in range(1, 100) if lose1(S) ] )
print( '20)', [ S for S in range(1, 100) if win2(S) ] )
print( '21)', [ S for S in range(1, 100) if lose2(S) ] )
