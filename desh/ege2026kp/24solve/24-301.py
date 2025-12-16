# Автор: К. Багдасарян

s = open('24-301.txt').readline()

max_length = 0
stack = []
for i, char in enumerate(s):
    if char == '(':
        stack.append(i)
    elif char == ')':
        if stack:
            chunk = s[stack[-1]:i+1]
            cur_length = i - stack[-1] + 1;
            if cur_length > max_length:
              max_length = cur_length
              print( chunk, len(chunk) )
            stack.pop()
print(max_length)
