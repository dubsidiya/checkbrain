from re import findall

s0 = open('24-347.txt').readline()

s = s0

num14 = r'([1-9A-D][0-9A-D]*)'
pattern = fr'(?={num14})'

parts = findall( pattern, s )

full = parts[:]
for p in parts:
  for i in range(1,len(p)):
    full.append( p[:-i] )

parts = [ p for p in full if int(p,14) % 5 == 0 ]

sMax = max( parts, key=lambda x: int(x,14)  )
print( s.find(sMax), len(sMax), sMax)

