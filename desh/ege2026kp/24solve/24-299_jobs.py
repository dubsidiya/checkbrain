# Автор: Е. Джобс

s = ' ' + open('24-299.txt').readline()

#s = '0+1+2+4+5+0*3'
#s = '10*20*3*0123456'
#s = '01*0'
#s = '1+2*0'

s = ' ' + s
for znak in "+* ":
  for c in '0123456789':
    while znak+'0'+c in s:
      s = s.replace( znak+'0'+c, znak+'0 '+c )

s = s.replace('+*', ' ').replace('*+', ' ') \
     .replace('++',' ').replace('**',' ')

while ' +' in s or ' *'	in s:
  s = s.replace(' +', '	' ).replace(' *', '	')

while '+ ' in s or '* '	in s:
  s =	s.replace('+ ', ' ' ).replace('* ', '	')

words = ' '.join( '+'.join(sss if '*0*' in '*'+sss+'*'
                          else ' '+sss[(sss+'*0*').index('0*'):]
                        for sss in ss.split('+'))
        for ss in s.split())

mx = max( words.replace('+ +', ' ' ).replace(' +', ' ').split(), key=len )

print( len(mx), mx )