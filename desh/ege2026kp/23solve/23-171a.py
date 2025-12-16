# Автор: А. Бычков

from functools import *

@lru_cache(None)
def F(curr, end, num_11, command_1):
    if curr == 11: num_11 = True
    if curr > end or curr == 23: return 0
    if curr == end and num_11: return 1
    if command_1 == 1:
        return F(curr + 2, end, num_11, 2) + F(curr * 2, end, num_11, 3)
    else:
        return F(curr + 1, end, num_11, 1) + F(curr + 2, end, num_11, 2) + F(curr * 2, end, num_11, 3)

print(F(3, 79, 0, 0))

# Ответ: 812266767
