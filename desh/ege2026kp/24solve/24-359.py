s = open('24-359.txt').readline()

COUNT_2025 = 90
COUNT_Y = 80

def valid( sub ):
  return sub.count('2025') >= COUNT_2025 and sub.count('Y') == COUNT_Y

def cantBeValid( sub ):
  return sub.count('Y') > COUNT_Y

N = len(s)
maxLen = 0
for L in range(N):
  for R in range(L+maxLen+1,N):
    sub = s[L:R]
    if valid( sub ):
      maxLen = R - L
      sMax = sub
      print( maxLen )
    elif cantBeValid( sub ):
      break

print( maxLen )