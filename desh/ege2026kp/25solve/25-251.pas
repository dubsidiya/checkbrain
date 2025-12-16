// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=800001;
while (ch<6) do
Begin    
   if (n.divisors.count>10) then
    if (n.divisors.count(t ->t.IsEven)=0) and (n.divisors.sum.IsOdd) then
  begin
    println(n, n.divisors.count);  ch+=1;
  end; 
  n+=1;
end