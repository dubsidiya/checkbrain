// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=75000001;
while (ch<5) do
Begin   
  if (n.divisors.count(l -> l.IsEven).IsOdd) then 
    begin 
    println(n-75000000, n.divisors.count(l -> l.IsEven)); 
    ch+=1;  
    end;
  n+=1;
end