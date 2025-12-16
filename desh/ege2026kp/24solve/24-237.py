s = open('24-237.txt').readline()

def isChunk3( s ):
  return s[0] == s[1] == s[2]

maxLen = 0
for i in range(3):
  curLen = 0
  nChunks3 = len(s)//3
  for k in range(nChunks3):
    chunk = s[k*3:k*3+3]
    if isChunk3(chunk):
      curLen += 3
      maxLen = max(maxLen, curLen)
    else:
      curLen = 0
  s = s[1:]

print( maxLen )

