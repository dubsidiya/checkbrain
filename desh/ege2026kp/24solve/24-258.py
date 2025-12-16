# Автор: А. Богданов

s = open('24-258.txt').readline().strip()

start, stop = 'ATGTTT', 'ACATAA'
i = s.find( start )
while i >= 0:
  for j in range(i+6, len(s), 3):
    if s[j:j+6] == stop:
      print( (j-i)//3+2)
    if s[j:j+3] in 'TAA TGA TAG':
      break
  i = s.find( start, i + 6 )



