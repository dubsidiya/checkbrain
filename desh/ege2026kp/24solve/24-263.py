# Автор: Е. Джобс

# FATasdfBADsdfhFATbjhvvBAD -> FATasdfBADsdfhFAT  BADsdfhFATbjhvvBAD
#  asdf sdfh bjhvv

# asdfFATFATbnmBAD   ->  asdf '' nbd ''
s = open('24-263.txt').readline()
# заменит строки FAT И BAD на пробела
s = s.replace('FAT', '*').replace('BAD','*')
# разбил строку по FAT и BAD
# убрал первое и последнее, так как это слова
# ДО первого FAT/BAD и после последнего FAT/BAD
lens = [len(x) for x in s.split('*')][1:-1]
print(min(a+b for a, b in zip(lens, lens[1:])) + 9)
