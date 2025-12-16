// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=10000001;
while (ch<5) do
Begin
  var d:=n.divisors;  
   if (d.count>=5) then
  begin 
  var d1:=n.Divisors[^4:]; d1.Remove(n);
  if (d1.sum.IsPrime) then
  begin
    println(d1.sum);  ch+=1;
  end; 
  end;  
  n+=1;
end