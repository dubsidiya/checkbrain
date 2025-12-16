s = open('24-239.txt').readline() + '...'

#s = 'ZZXZXZZXYYZYZZYYY'

def rec( i ):
  if i > L-2: return 0
  curLen = 0
  if s[i:i+2] in ['XY', 'YZ']:
    curLen = 2 + rec(i+2)
  if s[i:i+3] == 'YZZ':
    curLen = max( curLen, 3 + rec(i+3) )
  return curLen

maxLen, L = 0, len(s)
for i in range(L):
  curLen = rec(i)
  if curLen > maxLen:
    maxLen = curLen
    print( s[i:i+curLen] )

print( maxLen )

