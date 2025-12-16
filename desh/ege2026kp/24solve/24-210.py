s = open('24-210.txt').readline()
#s = "BDEABCBABCABBD"

pairs = ['ABC', 'BAC', 'CAB', 'CBA']

N = len(s)
maxCount = count = 0
i = 0
while i < N-2:
  if s[i:i+3] in pairs:
    count += 1
    if count > maxCount:
      #print( s[i-(count-1)*2:i+3] )
      maxCount = count
    i += 1
  else:
    count = 0
  i += 1

print( maxCount )
