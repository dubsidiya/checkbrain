s = open('24-310.txt').readline()

maxLen = 0
chunk = ''
for c in s:
    chunk += c
    if chunk in '*+0': chunk  = ''
    if len(chunk) > 1 and chunk[-2:] in '++**+':
      chunk  = ''
    if len(chunk) > 1 and chunk[-2] == '0' and c in '0123456789ABCDEF' and \
       (len(chunk) == 2 or chunk[-3] in '+*'):
      chunk = c
    if c in '6789ABCDEF':
      chunk = ''
    curLen = len(chunk)
    if curLen > 0 and chunk[-1] not in '+*':
       if curLen > maxLen:
          print( curLen, chunk )
       maxLen = max(maxLen, curLen)

print(maxLen)