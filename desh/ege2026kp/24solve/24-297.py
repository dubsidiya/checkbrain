s = open('24-296.txt').readline()

TARGET = 201

s = s.replace('AF', '*').split('*')
s = s[1:-1]

minLen = float('inf')
for i in range(len(s)-TARGET+2):
  chunk = ''.join(s[i:i+TARGET-1])
  minLen = min( minLen, len(chunk) )

print( minLen + len('AF')*TARGET )

#-------------------------------------

s = open('24-296.txt').readline()

N = len(s)

R = 1
countAF = 0
minLen = float('inf')
for L in range(1,N):
  if s[L-1] == 'A' and s[L] == 'F':
    countAF -= 1
  while R < N and countAF < TARGET:
    R += 1
    if s[R-2] == 'A' and s[R-1] == 'F':
      countAF += 1
  if R >= N:
    break
  minLen = min( minLen, R-L )

print( minLen )


