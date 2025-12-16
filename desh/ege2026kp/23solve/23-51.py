# Автор: А.Носкин

def f(x,y,s=''):
    if x == y: return s[-2]=='1'
    elif x > y: return 0
    return f(x+1,y,s+'1')+f(x*2,y,s+'2')

print(f(5,32))
