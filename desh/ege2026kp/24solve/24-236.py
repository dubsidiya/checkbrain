s = open('24-235.txt').readline()

maxLen = maxFreqChar = 0
chunk = prev = ''
for c in s:
  if c == prev:
    chunk = c
  else:
    chunk += c
    if len(chunk) >= maxLen:
      maxLen = len(chunk)
      maxFreqChar = max( chunk.count(c) for c in set(chunk) )
  prev = c

print( maxLen, maxFreqChar )

# Автор: Д. Статный

import string

s = open('24-235.txt').readline().strip()
for x in string.ascii_uppercase:
  s = s.replace(f'{x}{x}', f'{x} {x}')

M = max(s.split(), key=len)
m = 0
for x in string.ascii_uppercase:
  m = max(M.count(x), m)
print(m)
