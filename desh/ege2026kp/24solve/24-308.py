s = open('24-307.txt').read()

endLetters = 'CB'
waitDigit = 1
waitDigitOrSign = 2

maxLen = 0

i = 1
while i < len(s):
  if s[i-1:i+1] == endLetters:
    chunk = endLetters
    state = waitDigit
    j = i-1
    while j > 0:
      j -= 1
      if state == waitDigit:
        if s[j].isdigit():
          chunk = s[j] + chunk
          state = waitDigitOrSign
        else:
          break
      else:
        if s[j].isdigit():
          chunk = s[j] + chunk
          state = waitDigitOrSign
        elif s[j] in "+*" and s[j+1] != '0':
          chunk = s[j] + chunk
          state = waitDigit
        else:
          break
      if len(chunk) > maxLen and chunk[0] not in '+*0':
        maxLen = len(chunk)
        print( maxLen, chunk )

  i += 1

print( maxLen )


