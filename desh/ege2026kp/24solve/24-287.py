s = open('24-280.txt').readline()

letters = 'XY'
lettersNot = 'A'
targetCount = 1

lettersAll = letters + lettersNot
count = { let: 0 for let in lettersAll }
i = 0
maxLen = 0
for j, c in enumerate(s):
  for let in lettersAll:
    count[let] += c == let
  while any( count[let] > 0 for let in lettersNot ) or \
        any( count[let] > targetCount for let in letters ):
    for let in lettersAll:
      count[let] -= s[i] == let
    i += 1
  if all( count[let] == targetCount for let in letters ):
    maxLen = max( j - i + 1, maxLen )

print( maxLen )