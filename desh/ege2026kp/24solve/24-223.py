s = open('24-223.txt').readline()

while 'CACAC' in s:
  s = s.replace( 'CACAC', 'CAC CAC' )

s = s.replace('AB', '.')
s = s.replace('CAC', ',')

maxLen = L = 0
for i, ch in enumerate(s):
  if ch in '.,':
    L += 2 if ch == '.' else 3
    maxLen = max( maxLen, L )
  else:
    L = 0

print( maxLen )

