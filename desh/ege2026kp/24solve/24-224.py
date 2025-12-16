s = open('24-224.txt').readline()

while 'BACAB' in s:
  s = s.replace( 'BACAB', 'BAC CAB' )
while 'CABAC' in s:
  s = s.replace( 'CABAC', 'CAB BAC' )

s = s.replace('BAC', '.')
s = s.replace('CAB', ',')

maxLen = L = 0
for i, ch in enumerate(s):
  if ch in '.,':
    L += 3
    maxLen = max( maxLen, L )
  else:
    L = 0

print( maxLen )

