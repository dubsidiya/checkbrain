s = open('24-213.txt').readline()

s = s.replace( 'NPO', '.' )
s = s.replace( 'PNO', '.' )

maxLen = L = 0
for c in s:
  if c == '.':
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0

print( maxLen )

L = 1
while True:
  if s.find('.'*L) < 0:
    L -= 1
    break
  L += 1

print( L )
