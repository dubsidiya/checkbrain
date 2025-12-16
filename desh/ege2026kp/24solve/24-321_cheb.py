# Автор: А. Чеботарев

s=open('24-320.txt').readline().strip()
s=s.replace('==','z').replace('z=','z').split('z')
M=-11111111111
for i in s:
       q=i.split('=')
       z='='.join(q)
       if '8' in q and len(z)>M:
              M=len(z)
       else:
              l=i.find('8=')
              r=i.rfind('=8')
              srl=i[l:]
              srr=i[:r+1]
              M=max(len(srl),len(srr),M)
print(M)
