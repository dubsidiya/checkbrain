// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=300000001;
while (ch<5) do
Begin   
   if (n.divisors.count>=8) then
  begin 
  var d1:=n.Divisors[^7:]; 
  println(d1[0],n.divisors.count-2);  ch+=1;
  end;    
  n+=1;
end