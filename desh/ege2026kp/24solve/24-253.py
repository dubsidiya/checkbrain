s = open('24-253.txt').readline().strip()

maxCount = 0
for k in range(3):
  for start in range(k, len(s)-2, 3):
    j, count = start, 0
    while j+2 < len(s):
      if not(s[j] in 'CDF' and s[j+2] in 'AO'):
        break
      count += 1
      j += 3
    if count > maxCount:
      print( k, start, count )
    maxCount = max( count, maxCount )

print( maxCount )

# PRO100 ЕГЭ Динамическое программирование
# https://www.youtube.com/watch?v=B_r7kOK3PJo&t=15771s

s = open('24-253.txt').readline().strip()

n = len(s)
d = [0]*(n+1)
ans = 0
for i in range(3, n+1):
   si = i - 1
   if s[si-2] in 'CDF' and s[si] in "OA":
     d[i] = d[i-3] + 1
     ans = max( d[i], ans )
   else:
     d[i] = 0

print( ans )
