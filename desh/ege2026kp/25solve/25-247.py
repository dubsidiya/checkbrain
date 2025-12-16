def valid( n ):
  s = str(n)
  for i in range(len(s)-3):
    if s[i] == '0' and s[i+3] == '3': return False
  return n % 13 == 0 and \
         not( s[-1] == '2' and s[-4] == '4' ) and \
         not( '1' in s )

count = 0
n = 700000
while count < 5:
  if valid(n):
    print( n, sum(map(int, str(n))) )
    count += 1
  n += 1

print()

import fnmatch, re
re1 = re.compile( fnmatch.translate('*0??3*') )
re2 = re.compile( fnmatch.translate('*4??2') )
re3 = re.compile( fnmatch.translate('*1*') )
def valid( n ):
   s = str(n)
   return n % 13 == 0 and \
          not re.match(re1, s) and \
          not re.match(re2, s) and \
          not re.match(re3, s)

count = 0
n = 700000
while count < 5:
  if valid(n):
    print( n, sum(map(int, str(n))) )
    count += 1
  n += 1