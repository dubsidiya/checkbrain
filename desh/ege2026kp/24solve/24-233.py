s = open('24-233.txt').readline()

maxNum = 0
curNum = ''
for c in s:
  if c in '0123456789':
    curNum += c
  else:
    if curNum and curNum[0] != '0':
      maxNum = max( maxNum, int(curNum) )
    curNum = ''

print( maxNum )


# Автор: Д. Статный

import string

s = open('24-233.txt').readline()
for x in string.ascii_uppercase:
  s = s.replace(x, ' ')

s = s.split()

print( max(int(c) for c in s) )
