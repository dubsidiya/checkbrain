# Автор: А. Кабанов

s = open('24-212.txt').readline()

s = s.replace('C','B').replace('D','B').replace('O','A')
s = s.replace('BA','*').replace('B',' ').replace('A',' ')
print( max(len(c) for c in s.split()) )