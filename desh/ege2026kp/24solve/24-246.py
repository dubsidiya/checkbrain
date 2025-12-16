s = open("24-241.txt").readline()

def findPalindrome( s, L, R = None ):
  if R is None: R = L
  while L > 0 and R < len(s)-1:
    if s[L-1] != s[R+1]: break
    L, R = L-1, R+1
  return s[L:R+1]

maxLen = 0
for i in range(len(s)):
  c1 = findPalindrome( s, i )
  c2 = findPalindrome( s, i, i+1 )
  maxLen = max( maxLen, len(c1), len(c2) )

print( maxLen )