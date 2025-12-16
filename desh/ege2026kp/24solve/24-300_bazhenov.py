# Автор: Баженов Иван

f = open('24-300.txt')
stroka = f.readline()
f.close()

stroka = '10*20*3*012'
stroka = '10*2*3*4'
stroka = '0*2*3*4+10*2*3*4+10*2*3*4*0'

max_len = 0
podstroka = ''
num = 0
for i in range(len(stroka)):
    podstroka += stroka[i]
    # Строка не может начинаться со знака
    if podstroka in ['*', '+']:
        podstroka = ''
    # Строка обрывается при повторении знаков
    if len(podstroka) > 1 and podstroka[-2] + podstroka[-1] in ['++', '**', '+*', '*+']:
        podstroka = ''
    # Строка обрывается, если мы встречаем ведущий ноль у числа
    if len(podstroka) > 2 and podstroka[-3] in '+*' and podstroka[-2] == '0' and podstroka[-1] in '123456789':
        podstroka = ''
    # Строка обрывается, если ее значение уже не имеет шансов стать равным нулю
    if len(podstroka) > 1 and podstroka[-1] == '+' and eval(podstroka[:-1]) != 0:
        podstroka = ''
    # У подходящих строк значение равно нулю, а последний символ - цифра
    if len(podstroka) > 0 and podstroka[-1] not in '+*' and eval(podstroka) == 0:
        if len(podstroka) > max_len:
          print( len(podstroka), podstroka )
        max_len = max(max_len, len(podstroka))
print(max_len)


