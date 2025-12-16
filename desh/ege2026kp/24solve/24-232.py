s = open('24-232.txt').readline()

maxLen, maxSum = 0, 0
curLen, curSum = 0, 0
for c in s:
  if c == '0':
    if curLen > maxLen and curSum % 5 == 0:
      maxLen, maxSum = curLen, curSum
    curLen, curSum = 0, 0
  else:
    curLen += 1
    curSum += int(c)

print( maxLen, maxSum )

s = [ (len(x), summa) for x in s.split('0')
          if (summa := sum(map(int,x))) % 5 == 0 ]
best = max( s, key = lambda x: x[0] )

print( best )