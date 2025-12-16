from math import ceil, log2
V = 30*2**10
L = 25
Iadd = 140
M = 26 + 10
i = ceil(log2(M))
Nparty = 1
while True:
  xBits = log2(Nparty)
  Ibits = L*i + xBits
  Ibytes = ceil(Ibits/8) + Iadd
  Vx = Ibytes*Nparty
  if Vx > V: break
  print( Nparty, xBits, Vx, Vx/2**10 )
  Nparty += 1
