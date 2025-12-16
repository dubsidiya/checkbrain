s = open('24-314.txt').readline()

maxLen, maxVal = 0, 0
chunk = ''
for i, c in enumerate(s):
    chunk += c
    if chunk in '*+0': chunk  = ''
    if len(chunk) > 1 and chunk[-2:] in '++**+':
      chunk  = ''
    if len(chunk) > 1 and chunk[-2] == '0' and c in '0123456789ABCDEF' and \
       (len(chunk) == 2 or chunk[-3] in '+*'):
      chunk = c
    if c in 'ABCDEF':
      chunk = ''
    curLen = len(chunk)
    if i > curLen and curLen > 0 and s[i-curLen] == 'C' and chunk[-1] not in '+*':
       if curLen >= maxLen:
          val = eval(chunk)
          print( curLen, chunk, val )
          if curLen > maxLen:
            maxVal = val
          else:
            maxVal = max( maxVal, val )
       maxLen = max(maxLen, curLen)

print( maxLen, maxVal )