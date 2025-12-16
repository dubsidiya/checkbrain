# Автор: А. Кабанов

s = open('24-263.txt').readline()
s = s.split('Y')

maxLen = 0
for i in range(len(s)-151):
  c = 'Y'.join(s[i:i+151])
  maxLen = max( len(c), maxLen )

print( maxLen )
