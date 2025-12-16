// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=200000001;
while (ch<5) do
Begin
  var d:=n.divisors;  
   if (d.count>=7) then
  begin 
  var d1:=n.Divisors[:6]; d1.Remove(1);
  if (d1.product<n) and (d1.product mod 10=1) then
  begin
    println(d1.product, d1[d1.count-1]);  ch+=1;
  end; 
  end;  
  n+=1;
end