s = open('24-360.txt').readline()

for c in "2468":  s = s.replace(c, "0")
for c in "13579": s = s.replace(c, "1")

def valid( sub ):
  return sub[0] == "0" and sub[-1] == sub[0] and \
         sub[1] not in "0123456789" and \
         all( c == sub[1] for c in sub[2:-1] )

def cantBeValid( sub ):
  return sub[0] != "0" or sub[1] in "01" or \
         any( c != sub[1] for c in sub[2:] )

N = len(s)
maxLen = 3
for L in range(N):
  for R in range(L+maxLen+1,N):
    sub = s[L:R]
    if valid( sub ):
      maxLen = R - L
      sMax = sub
      print( maxLen )
    elif cantBeValid( sub ):
      break

print( maxLen )