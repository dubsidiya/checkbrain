// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=400000001;
while (ch<5) do
Begin   
  var f:=n.divisors.Where(l -> l>=299).Where(v -> v.Digits.sum=20).ToArray;
  if (f.count>=6)then begin var f1:=f[^6:]; println(f1[0],f.count); ch+=1;  end;    
  n+=1;
end