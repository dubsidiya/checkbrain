s = open('24-314.txt').readline()

def evalSpec( s ):
  parts = []
  while '+' in s or '*' in s:
    k = min( k1 if (k1 := s.find('+')) >= 0 else float('inf'),
             k2 if (k2 := s.find('*')) >= 0 else float('inf') )
    parts.append( str(int(s[:k], 16)) )
    parts.append( s[k] )
    s = s[k+1:]
  parts.append( str(int(s, 16)) )
  s = ''.join(parts)
  return eval(s)

maxLen, maxVal = 0, 0
chunk = ''
for c in s:
    chunk += c
    if chunk in '*+0': chunk  = ''
    if len(chunk) > 1 and chunk[-2:] in '++**+':
      chunk  = ''
    if len(chunk) > 1 and chunk[-2] == '0' and c in '0123456789ABCDEF' and \
       (len(chunk) == 2 or chunk[-3] in '+*'):
      chunk = c
    curLen = len(chunk)
    if curLen > 0 and chunk[-1] not in '+*':
       if curLen >= maxLen:
          val = evalSpec(chunk)
          print( curLen, chunk, val )
          if curLen > maxLen:
            maxVal = val
          else:
            maxVal = max( maxVal, val )
       maxLen = max(maxLen, curLen)

print( maxLen,  maxVal % 1000000 )