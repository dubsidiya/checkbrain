s = open('24-275.txt').readline()

#s = 'XYZXYZXYUSEFULLMESSAGEZXYZXYZXYAVERYUSEFULLMESSAGEZXYZXYZXYZ'
#s = 'XYZXYZUSEFULLMESSAGEXYZXYZXYZXYZAVERYUSEFULLMESSAGEZXYZXYZXYZ'
#s = 'XYZXYZMSXXYZXY'

divider = "XYZ"

def next( i, d = 1 ):
  return (i + d) % 3

state = 0
messages = []
msg = ""
for i in range(len(s)-2):
  if s[i] == divider[state]:
    if msg:
      if s[i+1] == divider[next(state)] and \
         s[i+2] == divider[next(state,2)]:
        messages.append( msg )
        msg = ""
      else:
        msg += s[i]
    if not msg:
      state = next(state)
  else:
    msg += s[i]


# print( messages )

print( max( len(s) for s in messages ) )




