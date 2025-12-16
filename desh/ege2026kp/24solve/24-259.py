s = open('24-259.txt').readline().strip()

start, stop = 'ATG', 'TAA'

maxLen = 0
i = s.find( start )
while i >= 0:
  for j in range(i+3, len(s)):
    if s[j:j+3] == stop:
      curLen = j - i + 3
      if curLen > maxLen:
        maxLen = curLen
        print( i, j, curLen )
    if s[j:j+3] in 'TAA TGA TAG':
      break
  i = s.find( start, i + 3 )

print( maxLen )