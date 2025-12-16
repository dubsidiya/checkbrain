s = open('24-298.txt').readline()

digits = '0123456789'
nonzeroDigits = '123456789'

maxLen = 0
state = 0 # start number
expr = ''
for i, c in enumerate(s):
  if state == 0:
    if c in nonzeroDigits:
      state = 1 # continue number or operation
      expr += c
    else:
      expr = ''
  elif state == 1:
    if c in digits:
      expr += c
      #if len(expr) > maxLen: print( expr )
      maxLen = max( maxLen, len(expr) )
    elif c in '-*':
      expr += c
      state = 0

print( maxLen )

print( '---------------------------' )

s = open('24-298.txt').readline()

s = s.replace('-', '*').split('*')

maxLen = 0
sub = ""
for chunk in s:
  if chunk and chunk[0] != '0':
    sub += chunk + '*'
  else:
    while chunk and chunk[0] == '0':
      chunk = chunk[1:]
    if chunk:
      sub = chunk + '*'
    else:
      sub = ""
  maxLen = max( len(sub)-1, maxLen )

print( maxLen )

print( '---------------------------' )

from re import findall

s = open('24-298.txt').readline()
number = r'(?:[1-9]\d*)'
pattern = fr'{number}(?:[-*]{number})*'
#print( findall( pattern, s ) )
print( max( len(part)
            for part in findall(pattern, s) ) )
