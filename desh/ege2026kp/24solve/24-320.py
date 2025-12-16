s0 = open('24-320.txt').readline()

#s0 = "341=143=3=218=812"

s = s0
s = s.replace('==',' ').replace(" ="," ")

def isValid( s ):
  nums = s.split('=')
  return all( n for n in nums) and \
         any( nums[i]==nums[i+1] for i in range(len(nums)-1) )

def maxValid( s ):
  if isValid(s): return len(s), s
  maxLen, sMax = 0, ''
  n = len(s)
  for i in range(n-2):
    if s[i] == '=': continue
    for j in range(n,i+2,-1):
      if j - i < maxLen: break
      if isValid(s[i:j]):
        maxLen, sMax = j-i, s[i:j]
        break
  return maxLen, sMax

maxLen, sMax = 0, ''
for chunk in s.split():
  if len(chunk) < maxLen:
    continue
  curLen, chunk = maxValid(chunk)
  if curLen > maxLen:
    sMax, maxLen = chunk, curLen
    print( maxLen, sMax )

print( maxLen, sMax[:100]+'...' )

print( '---------------------------------' )

s = s0
s = s.replace('==',' ').replace(" ="," ")

def isValid( nums ):
  if (kNums := len(nums)) <= 1: return None
  lenFirst = len(nums[0])
  lenLast = len(nums[-1])
  s = '='.join(nums)
  k0 = m0 = float('inf')
  for k in range(lenFirst):
    for m in range(lenLast):
      if k+m > k0+m0: continue
      nums0 = s[k:len(s)-m].split('=')
      if any( nums0[i]==nums0[i+1] for i in range(kNums-1) ):
        k0, m0 = k, m
  if k0+m0 < len(s):
    return k0, m0
  return None

def maxValid( s ):
  nums = s.split('=')
  maxLen, sMax = 0, ''
  n = len(nums)
  for i in range(n-1):
    for j in range(n,i+1,-1):
      chunk = '='.join(nums[i:j])
      L = len(chunk)
      if L < maxLen: break
      pos = isValid(nums[i:j])
      if pos:
        k, m = pos
        if L - (m+k) > maxLen:
          maxLen, sMax = L - (m+k), chunk[k:L-m]
        break
  return maxLen, sMax

maxLen, sMax = 0, ''
for chunk in s.split():
  if len(chunk) < maxLen:
    continue
  curLen, chunk = maxValid(chunk)
  if curLen > maxLen:
    sMax, maxLen = chunk, curLen
    print( maxLen, sMax )

print( maxLen, sMax[:100]+'...' )


print( '---------------------------------' )
