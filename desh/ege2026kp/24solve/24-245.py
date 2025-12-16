s = open("24-241.txt").readline()

chunks = s.split('F')

maxLen = 0
for chunk in chunks:
  if chunk.count('E') >= 5:
    parts = chunk.split('E')[1:-1]
    if all( p.count('A') == 1 for p in parts ):
      print(chunk)
      maxLen = max( maxLen, len(chunk) )

print( maxLen + 2 )

