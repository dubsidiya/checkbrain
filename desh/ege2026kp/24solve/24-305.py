s = open('24-305.txt').read()

startLetter = 'A'
secondLetter = 'F'
waitStart = 0
waitSecond= 1
waitDigit = 2
waitDigitOrSign = 3

state = waitStart
maxLen = 0
chunk = ''
for c in s:
  if state == waitStart:
    if c == startLetter:
       chunk = startLetter
       state = waitSecond
    else:
       chunk = ''
  elif state == waitSecond:
    if c == secondLetter:
       chunk += secondLetter
       state = waitDigit
    else:
       chunk = ''
       state = waitStart
  elif state == waitDigit:
    if c.isdigit() and c != '0':
      chunk += c
      state = waitDigitOrSign
    elif c.isdigit() and c == '0':
      chunk += c
      state = waitStart
    else:
      state = waitStart
      chunk = ''
  elif state == waitDigitOrSign:
    if c.isdigit():
      chunk += c
    elif c in '+*':
      chunk += c
      state = waitDigit
    else:
      chunk = ''
      state = waitStart
  if len(chunk) > maxLen and chunk[-1] not in '+*':
    maxLen = len(chunk)
    print( maxLen, chunk )

print( maxLen )


