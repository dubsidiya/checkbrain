s = open('24-215.txt').readline()

B = ['A', 'B', 'C']
D = ['1', '2', '3']

maxLen = L = 0
for ch in s:
  if ch in D and L % 2 == 0 or \
     ch in B and L % 2 == 1:
    L += 1
    maxLen = max( L, maxLen )
  else:
    L = 0 if ch in B else 1

print( maxLen // 2 )

