s = open("24-249.txt").readline()

A = '0123456789ABCDEF'
tailPos = [None]*16

minLen = 10**10
for i, c in enumerate(s):
  if c in A:
    tailPos[A.index(c)] = i
    if None not in tailPos:
      L = i - min(tailPos) + 1
      minLen = min( minLen, L )

print( minLen )

