s = open("24-241.txt").readline()

#s = 'AOFJJHGASJHOFLKJLKJOMNBMBNMOFLKJLO'

chunks = s.split('O')[1:-1]

N = len(chunks)
maxLen = 0
for i in range(N):
  s = 'O'
  for j in range(i, N):
    if chunks[j].count('F') > 2: break
    s += chunks[j] + 'O'
    maxLen = max( len(s), maxLen )

print( maxLen )

#-------------------------------------------

s = open("24-241.txt").readline()

chunks = s.split('O')[1:-1]
data = zip( chunks, [ chunk.count('F') for chunk in chunks ] )

s = 'O'
for chunk, nF in data:
  if nF > 2:
    s = ''
    continue
  s += chunk + 'O'
  maxLen = max( len(s), maxLen )

print( maxLen )


