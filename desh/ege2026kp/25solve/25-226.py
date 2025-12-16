def valid( n ):
  s = str(n)
  if s[0] != '1' or s[-1] != '9' or '5' not in s:
    return False
  for i in range(1, len(s)):
    if s[i] <= s[i-1]: return False
  return True

valid(1235679)

for n in range(21, 10**9, 21):
  if valid(n):
    print( n, n // 21 )