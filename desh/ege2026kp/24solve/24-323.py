s0 = open('24-320.txt').readline()

#s0 = "341=140=3=218=812=1"

#s0 = s0[:1000]

NUMLEN = 35

s = s0
s = s.replace('==',' ').replace(" ="," ")

def isValid( s ):
  nums = s.split('=')
  return all( n for n in nums) and \
         any( 10**(NUMLEN-1) <= int(nums[i]) < 10**NUMLEN for i in range(len(nums)) )

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
print( [ num for num in sMax.split('=') if len(num) == NUMLEN ])

print( '---------------------------------' )

#s0 = '47=596==8146577991845=36=9254822318=244768598279==8=55=91=136433455247155735=66647=638=85965691494=996651828=589846281=681636226=3799426872369531613915415923=8998462=93915=853=9=967571167=5=5615=4=4255774383944954=6228767371741718874=94=62541839698=617=59189=346=2=17154435483942792191=5665264371472471=2272281894=769526698784752991179126275=2=55=3932638=62336463=529419574437224=187638=6744=34622313=45=92527926578314151=98549938858487178367983773817354=88913=1389223294458987685=121985=99459855447844=3=655=6265189859144867776762186746812169657=369=623961=3136487173=75167=2628852411=172238771713612227876826=6912145884=885=744838172258699233979546212142473=36152469=2345161949881915684=19115582647484234=3382673199342781175=3=7275468=36993626523145711738754912736=458981242127162137=7=2626228943=8368847194615196533164284327582=8237=69278725837613483143547877939786575'
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
      if any( 10**(NUMLEN-1) <= int(nums0[i]) < 10**NUMLEN for i in range(kNums) ):
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
print( [ num for num in sMax.split('=') if len(num) == NUMLEN ])

