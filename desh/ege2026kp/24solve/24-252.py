s = open('24-252.txt').readline()

digitsHex = '0123456789ABCDEF'

minLen = float('inf')
for i, c in enumerate(s):
  if c == '0':
    k = 1
    for j in range(i+1, len(s)):
      if s[j] == digitsHex[k]:
        k += 1
        if k == 16:
          minLen = min( minLen, j - i + 1 )
          break

print( minLen )


