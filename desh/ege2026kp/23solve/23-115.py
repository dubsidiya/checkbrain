def F( start, end, nCmd ):
  return (nCmd == 0) if start == end else\
         0 if start > end or nCmd < 0 else \
         F( start+1, end, nCmd-1 ) + \
           F( start+5, end, nCmd-1 ) + \
           F( start*3, end, nCmd-1 )

for nCmd in range(1,1000):
  count = F( 1, 111, nCmd )
  if count > 0:
    print( nCmd, count )
    break

print( '--------------------------------' )

result = [float('inf'), 0]
def F( start, end, nCmd = 0 ):
   global result
   if start > end or nCmd > result[0]:
     return
   if start == end:
     if nCmd < result[0]:
       result = [nCmd, 1]
     else:
       result[1] += 1
     return
   F( start*3, end, nCmd+1 )
   F( start+5, end, nCmd+1 )
   F( start+1, end, nCmd+1 )

F( 1, 111 )
print( result )