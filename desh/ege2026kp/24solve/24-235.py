s = open('24-235.txt').readline()

letters = 'XYZWOP'
counts = {}
for c in letters:
  counts[c] = s.count( f'X{c}P' )

print( max(counts.values()) )
