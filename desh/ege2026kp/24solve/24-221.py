s = open('24-221.txt').readline()

maxLen = L = 0
prev = ''
total = ''
for i, ch in enumerate(s):
  if ch == '0':
    if prev == '0':
      L += 1
      total += ch
    else:
      L = 1
      total = ch
  elif ch == '1':
    if prev in '01':
      L += 1
      total += ch
  else:
    L = 0
    total = ''
  if L > maxLen and '01' in total:
    maxLen = L
  prev = ch

print( maxLen )


