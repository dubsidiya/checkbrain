from re import findall

s0 = open('24-347.txt').readline()

s = s0

num8 = r'([1-7][0-7]*)'
pattern = fr'(?={num8})'

parts = findall( pattern, s )

full = parts[:]
for p in parts:
  for i in range(1,len(p)):
    full.append( p[:-i] )

parts = [ p for p in full if int(p,8) % 13 == 0 ]

sMax = max( parts, key=lambda x: (len(x), -int(x,8))  )

print( s.find(sMax), len(sMax), sMax)

