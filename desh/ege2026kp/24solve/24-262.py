# Автор: А. Кирпичев

s = open('24-262.txt').readline()

s = s.replace( 'SOLO', 'SOL OLO').split()
m = 0

for j in range(len(s)):
  r = ''.join( s[j:j+5] )
  c = 0
  for i in '0123456789':
    if i in r:
      c += 1
  if c >= 5:
    m = max( m, len(r)- 8 )

print( m )