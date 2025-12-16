from re import findall

s0 = open('24-347.txt').readline()

s = s0

num12 = r'([1-9AB][0-9AB]*)'
pattern = fr'(?={num12})'

parts = findall( pattern, s )

full = parts[:]
for p in parts:
  for i in range(1,len(p)):
    full.append( p[:-i] )

parts = [ p for p in full if int(p,12) % 9 == 0 ]

sMax = max( parts, key=lambda x: (len(x), -int(x,12))  )

print( s.find(sMax)+len(sMax)-1, len(sMax), sMax)

# Автор: К. Багдасарян

s = s0
n = len(s)
c = ''
mxlen = 0
for i in range(n):
    if s[i] in '123456789AB' or (s[i]=='0' and len(c) > 0):
        c = c + s[i]
        if int(c,12) % 9 == 0:
            if len(c) > mxlen or (len(c) == mxlen and int(c,12) < int(mxc,12)):
                mxlen = len(c)
                mxc = c
                ans = i
    else:
        c = ''
print(ans, mxlen, mxc)
