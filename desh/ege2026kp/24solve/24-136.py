# Автор: В.Н. Шубинкин

with open('24-j5.txt') as tf:
    s = tf.read().strip()

print(s.count('OCK') - s.count('STOCK'))

count = 0
for i in range(len(s)-2):
  if s[i:i+3] == "OCK" and \
     (i < 2 or s[i-2:i] != "ST"):
    count += 1

print( count )
