s = open('24-209.txt').readline()
# s = "BDEABCBABBD"

pairs = ['AB', 'CB', 'BC', 'BA']

N = len(s)
maxCount = count = 0
for i in range(N-1):
  if s[i:i+2] in pairs:
    count += 1
    maxCount = max(maxCount, count)
  else:
    count = 0

print( maxCount )
