s = open("24-241.txt").readline()

G = "AEO"
S = "BCDF"

chunk = ""
count = maxCount = 0
for c in s:
  L = len(chunk)
  if L in [0,1]:
    if c in S: chunk += c
    else:
      chunk = ""
      count = 0
  else:
    if c in G:
      count += 1
      maxCount = max( maxCount, count )
      chunk = ""
    else:
      chunk = chunk[1] + c
      count = 0

print( maxCount )
