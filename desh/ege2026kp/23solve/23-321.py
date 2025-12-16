allNumbers = set()
def f( start, end, path = [], count2 = 0 ):
   if start > end: return
   path = path + [start]
   if start == end:
      if (8 in path and 16 in path) != (32 in path):
        global allNumbers
        allNumbers |= set(path)
        print( path )
      return
   f( start*2, end, path, 0 )
   if count2 < 2:
     f( start+3, end, path, count2+1 )

f( 2, 70 )
print( len( allNumbers ) )

#---------------------------------------------------------------------------
# Автор: П. Тюрин

def _f(x,nd,F8,F16,F32,m,s):#старт, финиш, флаги, список посещенных точек, совершенные ходы
    global tmp
    if x==8:
        F8=True#поднимаем флаг, если прошли через точку
    if x==16:
        F16=True
    if x==32:
        F32=True
    if x>nd:
        return 0
    if x<nd and s[-4:]!='+3+3':
        return _f(x*2,nd,F8,F16,F32,m+[x*2],s+'*2')+_f(x+3,nd,F8,F16,F32,m+[x+3],s+'+3')
    if x<nd and s[-4:]=='+3+3':
        return _f(x*2,nd,F8,F16,F32,m+[x*2],s+'*2')
    if x==nd and ((F8 and F16)!=F32):#добравшись до конца, учитываем поднятые флаги
        print( m )
        tmp=tmp+m#все посещенные точки сохраняем в глобальный список
        return 1#количество считать не обязательно, но пусть будет
    return 0

tmp=[]
_f(2,70,False,False,False,[2],'')
print(len(set(tmp)))
#print(sorted(set(tmp)))
