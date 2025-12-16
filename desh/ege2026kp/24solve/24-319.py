"""
Демо-2025
Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков «–» и «*». Определите
максимальное количество символов в непрерывной последовательности, которая является
корректным арифметическим выражением с целыми неотрицательными числами.
"""
s = open('24-319.txt').readline()

chunk = ''
maxLen = 0
for c in s:
  if c in '0123456789':
    if len(chunk) > 0 and chunk[-1] == '0' and \
      (len(chunk) == 1 or chunk[-2] in '-*'):
          chunk = c
    else: chunk += c
    if len(chunk) > maxLen and len(chunk) > 130:
      print( len(chunk), chunk )
    maxLen = max( len(chunk), maxLen )
  elif c in '-*':
    if len(chunk) > 0 and chunk[-1] in '-*':
          chunk = ''
    else: chunk += c

print(maxLen)

print( '---------------------------' )

s = open('24-319.txt').readline()

s = s.replace('-', '*').split('*')

maxLen = 0
sub = ""
for chunk in s:
  if chunk and (chunk[0] != '0' or chunk == '0'):
    sub += chunk + '*'
    maxLen = max( len(sub)-1, maxLen )
  else:
    if chunk and chunk[0] == '0':
      maxLen = max( len(sub)+1, maxLen )
      if chunk.count('0') == len(chunk):
            sub = '0*'
      else: sub = chunk.lstrip('0') + '*'
    else:
      sub = ''

print( maxLen )

print( '---------------------------' )

s = open('24-319.txt').readline()

s = s.replace('-', '*').split('*')

def isNumber( s ):
  if not s: return False
  if s == '0': return True
  if s[0] != '0': return True
  s = s.lstrip('0')
  return s if s else '0'

maxLen = 0
sub = ""
for chunk in s:
  res = isNumber(chunk)
  if res == True:
    sub += chunk + '*'
  elif res == False:
    sub = ""
  else:
    maxLen = max( len(sub)+1, maxLen )
    sub = res + '*'
  maxLen = max( len(sub)-1, maxLen )

print( maxLen )

print( '---------------------------' )

from re import findall
s = open('24-319.txt').readline()
number = r'(?:[1-9]\d*|0)'
pattern = fr'{number}(?:[-*]{number})*'
parts = findall( pattern, s )
print( max( len(part) for part in parts ) )
