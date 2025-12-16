s = open("24-241.txt").readline()

chunks = s.split('E')

minLen = 10**10
for chunk in chunks:
  if chunk.count('B') == 2:
    p1 = chunk.find('B')
    p2 = chunk.rfind('B')
    if chunk[p1+1:p2].count('A') > 5:
      if len(chunk) < minLen:
        print(chunk)
      minLen = min( minLen, len(chunk) )

print( minLen + 2 )

