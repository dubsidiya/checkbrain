// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=100000001;
while (ch<5) do
Begin    
    if (n.divisors.count(t ->t.IsEven)=n.divisors.count(t ->t.IsPrime))  then
  begin
    var pn:=n.divisors.where(t ->t.IsEven).sum;
    var en:=n.divisors.where(t ->t.IsPrime).sum;
    println(n, abs(pn-en));  ch+=1;
  end; 
  n+=1;
end