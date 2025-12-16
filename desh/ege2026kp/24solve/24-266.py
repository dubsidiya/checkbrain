# Автор: А. Кабанов

s = open('24-263.txt').readline()
s = s.split('Z')

minLen = 10**10
for i in range(len(s)-121):
  c = 'Z' + 'Z'.join(s[i+1:i+120]) + 'Z'
  minLen = min( len(c), minLen )

print( minLen )
