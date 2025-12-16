from string import ascii_uppercase

s = open('24-280.txt').readline()

letters = ascii_uppercase
maxCount = 10

count = { let: 0 for let in letters }
i = 0
maxLen = 0
for j, c in enumerate(s):
  for let in letters:
    count[let] += c == let
  while any( count[let] > maxCount for let in letters):
    for let in letters:
      count[let] -= s[i] == let
    i += 1
  maxLen = max( j - i + 1, maxLen )

print( maxLen )