s = open('24-299.txt').readline()

s = '01*0'
s = '1+2*0'

#---------------------------------------------------------
# Решение однократным проходом по строке O(N)
#---------------------------------------------------------

def check( expr ):
  global maxLen, sMax
  sZero = []
  for t in expr.split('+'):
    if '*0' in t or t.startswith('0'):
      sZero.append( t )
    elif '0*' in t:
      k = t.find( '0*' )
      sZero = [ t[k:] ]
    elif t.endswith('0'):
      sZero = [ t[-1]  ]
    else:
      sZero = []
    curLen = len( '+'.join(sZero) )
    if curLen > maxLen:
      sMax = '+'.join(sZero)
      # print( curLen-1, sZero )
      maxLen = max( curLen, maxLen )

digits = '0123456789'

if '0' in s:
  sMax, maxLen = '0', 0
else:
  sMax, maxLen = '', 0

state = 0 # start number
sub = ''
for i, c in enumerate(s):
  if state == 0:
    if c in digits:
      sub += c
      check( sub )
      if c == '0':
        state = 2 # wait operation
      else:
        state = 1 # wait number or operation
    else:
      sub = ''
  elif state == 1:
    if c in digits:
      sub += c
      check( sub )
    else:
      sub += c
      state = 0
  else:
    if c in '+*':
      sub += c
      state = 0
    else:
      sub = c
      check( sub )

print( maxLen, sMax )
print( eval(sMax) )


