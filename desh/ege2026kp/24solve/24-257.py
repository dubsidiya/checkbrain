# Автор: А. Кабанов

s = open('24-257.txt').readline().strip()

#s = 'CORAFCAFROCKCFAAC'

count = maxLen = 0
for i in range(len(s)):
  if 'A' in s[i:i+3] and 'F' in s[i:i+3] and 'C' in s[i:i+3]:
    count = -2
  else:
    count += 1
    maxLen = max( count, maxLen )

print( maxLen )