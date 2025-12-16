F = open( "24-200.txt" )

def match( s, mask ):
  s = s.strip()
  for c1, c2 in zip(s, mask):
    if c2 != '?' and c1 != c2:
      return False
  return len(s) == len(mask)

def valid( s ):
  return match( s, "195.2.?.14" ) or \
         match( s, "195.2?.?.14" ) or \
         match( s, "195.2??.?.14" ) or \
         match( s, "195.2.??.14" ) or \
         match( s, "195.2?.??.14" ) or \
         match( s, "195.2??.??.14" ) or \
         match( s, "195.2.???.14" ) or \
         match( s, "195.2?.???.14" ) or \
         match( s, "195.2??.???.14" )

ips = set()
for s in F.readlines():
  if valid(s):
    ips.add( s )

print( len(ips) )

F.close()