s = open('24-215.txt').readline()

B = ['A', 'B', 'C']
D = ['1', '2', '3']
maxLen = L = 0
for m in range(2):
  for i in range(m,len(s)-1, 2):
    if s[i] in B and s[i+1] in D:
      L += 1
      maxLen = max( L, maxLen )
    else:
      L = 0

print( maxLen )

# Автор А. Чеботарев

s = s.replace('B','A')
s = s.replace('C','A')
s = s.replace('2','1')
s = s.replace('3','1')
d = 'A1'
while d in s:
  d += 'A1'

print( (len(d)-2)//2 )
