# Автор: Е. Джобс

s = open('24-259.txt').readline().strip()

s = s.replace('ATG', 'A**')

s = s.replace('TGA', 'TG GA')\
     .replace('TAG', 'TA AG')\
     .replace('TAA', 'TAA AA')
mx = 0
for ss in s.split():
  if ss[-3:] == 'TAA' and 'A**' in ss:
    mx = max(mx, len(ss) - max(ss.index('A**'),
                               ss.rfind('A**A')))
print(mx)

s = open('24-259.txt').readline().strip()
mx = 0
lft = rht = 0
for i in range(len(s)):
  if s[i:i+3] == 'ATG':
    for j in range(i+3, len(s)):
      if s[j:j+3] in ('TGA', 'TAG'):
        break
      if s[j:j+3] == 'TAA':
        mx = max(mx, j+3-i)
        break
print(mx)
