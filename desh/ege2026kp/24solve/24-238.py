s = open('24-238.txt').readline()

maxLen = 0
def rec( i ):
  if i > L-2: return 0
  curLen = 0
  if s[i:i+3] == 'DAD':
    curLen = 3 + rec(i+3)
  elif s[i:i+2] == 'DA':
    curLen = 2
  elif s[i:i+1] == 'D':
    curLen = 1 + rec(i+1)
  elif s[i:i+2] == 'AD':
    curLen = 2 + rec(i+2)
  return curLen

maxLen, L = 0, len(s)
for i in range(len(s)):
  curLen = rec(i)
  if curLen > maxLen:
    maxLen = curLen
    print( s[i:i+curLen] )

print( maxLen )


# Автор: Е. Джобс

s = open('24-238.txt').readline()
m_len = 0
for st in range(3):
    c_len = 0
    for i in range(st, len(s), 3):
        if s[i:i+3] == 'DAD':
            c_len += 1
            m_len = max(m_len, c_len)
        else:
            c_len = 0

m_ss = 'DAD'
while m_ss in s:
    m_ss += 'DAD'
m_ss = m_ss[3:]

add = 0
for st in ('', 'D', 'AD'):
    for fn in ('', 'D', 'DA'):
        if st + m_ss + fn in s:
            add = max(add, len(st+fn))
print(len(m_ss) + add)


