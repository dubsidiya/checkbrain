s = open('24-225.txt').readline()

digits = '0123456789'
def matchMask( s, startPos, mask ):
  i = startPos
  for k, m in enumerate(mask):
    if i >= len(s): return 0
    if s[i] == m or \
       s[i] in digits and m == '?':
      i +=1
    else:
      return 0
  numLen = len(mask) - 4
  # print( s[startPos:startPos+20] )
  return int( s[startPos+2:startPos+2+numLen] )

nMax = 0
for i in range(len(s)):
  n = matchMask( s, i, 'FF44??78??3FF' )
  if n: print(n)
  nMax = max( nMax, n )

print( nMax, sum( int(d) for d in str(nMax) if int(d) % 2 == 0 ) )


