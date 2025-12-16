s0 = open('24-332.txt').readline()

s = s0
s = s.replace('.', '.|').replace('  ', '|').replace('| ', '|')
for s1 in 'ABCabc.':
  for s2 in 'ABC':
    s = s.replace( s1+s2, s1+'|'+s2 )
s = [ chunk for chunk in s.split('|')
            if any( chunk.startswith(c) for c in 'ABC') and
               chunk.endswith('.')]
sMax = max( s, key = len )
print( len(sMax), sMax )

print( '----------------------------------' )

from re import findall

s = s0
wordCap = "[ABC][abc]*"
wordNoCap = "[abc]+"
word = fr"(?:{wordCap}|{wordNoCap})"
pattern = fr"{wordCap}(?:\s{word})*\."
parts = findall( pattern, s )
sMax = max( parts, key = len )

print( len(sMax), sMax )

print( '----------------------------------' )

# Автор: Л. Шастин

s = s0.rstrip()
m = 0
for l in s.replace('A','C').replace('B','C').split('.'):
  l = l.split('  ')[-1].lstrip(' ').split(' ')
  for i in range(len(l)-1, -1, -1):
    if 'C' in l[i]:
      s1 = ' '.join([l[i][l[i].rfind('C'):]] + l[i+1:]) + '.'
      if len(s1) > m:
        m = max( m, len(s1) )
        sMax = s1
    if l[i] == '' or 'C' in l[i][1:]:
      break
print( m, sMax )