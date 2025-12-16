// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=10000001;
while (ch<5) do
Begin
  var d:=n.divisors;  
   if (d.count>=4) then
  begin 
  var d1:=n.Divisors[^3:]; d1.Remove(n);
  if (d1.sum<100000) and (d1.sum mod 1000=112) then
  begin
    println(d1.sum);  ch+=1;
  end; 
  end;  
  n+=1;
end