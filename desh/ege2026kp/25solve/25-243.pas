// Автор: И.В.Свистун
##
uses school;

for var i:=100000 to 500000 do
    if (i.Divisors.Where(t -> t.IsPrime).Count>3)then
    begin
     var a:=|0|*10000; var j:=0; 
     var n:=i.Divisors;  
     for var k:=0 to n.count-1 do
     if n[k].IsPrime then begin a[j]:=n[k]; j+=1; end;
var p:=a[1]-a[0]; var flag:=true;  
//for var g:=0 to j-1 do print(a[g]);
for var t:=1 to j-2 do
  if (a[t+1]-a[t]<>p) then flag:=false;
if flag then println(i,j*p) end;

{'101065 48+
107525 24+
124729 24+
177289 48+
236555 24+
278185 72+
365585 24+
494615 24+
505325 48 
537625 24 
623645 30 }

