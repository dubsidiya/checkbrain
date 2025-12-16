s = open('24-280.txt').readline()

s += ' '

i = 0
maxLen = 0
for i in range(len(s)-1):
  for j in range(i+1,len(s)):
    if s[i:j].find(s[j]) >= 0: break
  maxLen = max( j-i, maxLen )

print( maxLen )

#------------------------------------------

s = open('24-280.txt').readline()

i = 0
inside = ''
maxLen = 0
for j in range(len(s)):
  k = inside.find(s[j])
  if k >= 0:
    inside = inside[k+1:]
  inside += s[j]
  maxLen = max( len(inside), maxLen )

print( maxLen )

#------------------------------------------

# Автор: М. Шагитов

s = open('24-280.txt').readline()

set = set()
left = 0
max_length = 0
for right in range(len(s)):
    while s[right] in set:
        set.remove(s[left])
        left += 1
    set.add(s[right])
    max_length = max(max_length, right - left + 1)
print(max_length)
