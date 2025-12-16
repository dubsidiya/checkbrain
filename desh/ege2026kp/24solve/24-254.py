from string import ascii_uppercase, digits

s = open('24-252.txt').readline().strip()

#s = "ABCDABECD"

maxLen = 0
for c in digits + ascii_uppercase:
  chunks = s.split(c)
  if len(chunks) > 2:
    curMaxLen = max( len(p) for p in chunks[1:-1] )
    if curMaxLen >= maxLen:
      maxLen = curMaxLen
      print( f"{c}{maxLen+2}" )

