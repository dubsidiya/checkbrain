# Автор: К. Багдасарян

s = open('24-303.txt').readline()

dct = {'(': ')','[': ']', '{': '}'}

max_length = 0
stack = []
for i, char in enumerate(s):
    if char in dct:
        stack.append((i,char))
    elif char in dct.values():
        if stack:
            if char == dct[stack[-1][1]]:
              chunk = s[stack[-1][0]:i+1]
              cur_length = i - stack[-1][0] + 1;
              if cur_length > max_length:
                max_length = cur_length
                print( chunk, len(chunk) )
              max_length = max(max_length, i - stack[-1][0] + 1)
              stack.pop()
            else:
              stack = []
print(max_length)
