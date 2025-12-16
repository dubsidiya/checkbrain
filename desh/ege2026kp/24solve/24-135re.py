# Автор: А. Фахуртдинова

#1 способ
s=open('24-J4.txt').readline().strip()
s=s.replace('JBOSSJ','JwJ').replace('BOSSJ','WJ').replace('JBOSS','JW')
print(s.count('BOSS'))

#2 способ
s=open('24-J4.txt').readline().strip()
s=s.replace('J','J J') # для решения проблемы слияния строк
s=s.replace('JBOSSJ','*').replace('BOSSJ','*').replace('JBOSS','*')
print(s.count('BOSS'))
