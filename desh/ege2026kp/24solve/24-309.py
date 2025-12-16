s = open('24-309.txt').read()

TEMPLATE = 'FSRQ'
N = 80

n = len(s)
L = count = maxLen = 0
for R in range(4, n+1):
   count += s[R-4:R] == TEMPLATE
   while count > N:
      count -= s[L:L+4] == TEMPLATE
      L += 1
   if count == N:
     maxLen = max( maxLen, R-L )
     sMax = s[L:R]

print( maxLen, sMax )
print( sMax.count(TEMPLATE) )
