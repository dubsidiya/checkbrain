s = open('24-j4.txt').read().strip()

s = ' ' + s + ' '
count = 0
for i in range(1,len(s)-4):
  if s[i:i+4] == 'BOSS' and s[i-1] != 'J' and s[i+4] != 'J':
    count += 1

print( count )
