# Автор: В. Петров

s = open('24-250.txt').readline().strip()

mn = len(s) + 1
s = s.split('.')
for i in range(len(s)-6):
  cur = '.' + '.'.join(s[i:i+6]) + '.'
  mn = min( mn, len(cur) )
print( mn )