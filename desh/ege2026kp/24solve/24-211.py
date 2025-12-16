s = open('24-211.txt').readline()
s = "EDFABECAFBDACFDA"

pairs = ['ABEC', 'BDAC', 'CAFB', 'CFBA']

N = len(s)
maxCount = count = 0
i = 0
while i < N-3:
  if s[i:i+4] in pairs:
    count += 1
    if count > maxCount:
      print( s[i-(count-1)*3:i+4] )
      maxCount = count
    i += 2
  else:
    count = 0
  i += 1

print( maxCount )
