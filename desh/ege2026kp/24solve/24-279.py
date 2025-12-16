
s = open('24-279.txt').readline()

pos = -1
maxLen = L = 0
for i, c in enumerate(s):
  if c in '0123456789ABCDEF':
    if L > 0 or c != '0':
      L += 1
      if L > maxLen: pos = i
      maxLen = max( L, maxLen )
  else:
    L = 0

print( maxLen, s[pos-maxLen+1:pos+1] )




