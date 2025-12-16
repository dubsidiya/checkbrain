sArr = open("24-247.txt").readlines()

def findLongest( s ):
  cMax, maxLen = s[0], 1
  chunk = '.'
  for c in s:
    if c == chunk[-1]:
      chunk += c
      if len(chunk) > maxLen:
        cMax, maxLen = c, len(chunk)
    else:
      chunk = c
  return cMax, maxLen, s.count(cMax)

result = [ findLongest(s) for s in sArr ]
result.sort( key = lambda x: (x[1], x[2]), reverse = True )

print( result[0] )