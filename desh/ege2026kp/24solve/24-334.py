s0 = open('24-334.txt').readline()

digits = '0123456789AB'
even = '02468A'
s = s0
sub = sMax = ''
for c in s:
   if c in digits[1:] or c == '0' and sub:
      sub += c
      if c in even:
        if len(sub) > len(sMax):
          sMax = sub
   else:
     sub = ''

print( len(sMax), sMax )

#----------------------------------------
s = ' ' + s0 + ' '
for c in set(s)-set('0123456789AB'):
  s = s.replace( c, ' ' )

while ' 0' in s:
  s = s.replace( ' 0', ' ' )

for c in '13579B':
  while c+' ' in s:
    s = s.replace( c+' ', ' ' )

parts = s.split()
sMax = max( parts, key = len )
print( len(sMax), sMax )

#----------------------------------------
from re import findall

s = s0
num12 = r"[1-9AB][0-9AB]*[02468A]"
pattern = fr"(?=({num12}))"

parts = findall( pattern, s )
sMax = max( parts, key = len )

print( len(sMax), sMax )

