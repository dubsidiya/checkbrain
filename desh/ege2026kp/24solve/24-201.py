F = open( "24-200.txt" )

def match( s, mask ):
  s = s.strip()
  for c1, c2 in zip(s, mask):
    if c2 != '?' and c1 != c2:
      return False
  return len(s) == len(mask)

def valid( s ):
  return match( s, "195.?2.15.14" ) or \
         match( s, "195.?2.1?5.14" )

ips = set()
for s in F.readlines():
  if valid(s):
    ips.add( s )

print( len(ips) )

F.close()

# Вариант 2. Регулярные выражения

import re
s = open( "24-200.txt" ).read()
m = set( re.findall( r"195\.\d2\.1\d{0,1}5\.14",  s ) )
print( len(m) )

s = open( "24-200.txt" ).read()
m = set( re.findall( r"195\.\d2\.1\d{0,1}5\.14",  s ) )
print( len(m) )

