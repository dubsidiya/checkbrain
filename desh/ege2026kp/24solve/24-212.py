s = open('24-212.txt').readline()

G = ['A', 'O']
S = ['B', 'C', 'D']

maxLen = L = 0
for ch in s:
  if ch in S and L % 2 == 0 or \
     ch in G and L % 2 == 1:
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0 if ch in G else 1

print( maxLen // 2 )

