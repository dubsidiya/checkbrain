// Автор: И.В.Свистун
##
uses school;
var ch:=0; var n:=60000;
while (ch<5) do
Begin    
   var dn:=n.Divisors[^2];
   var qn1:=n.Factorize.Sum.ToString;
   var qn:=qn1.Inverse.ToInteger;
    if (n+dn+qn>202122) then
  begin
    println(n, dn+qn);  ch+=1;
  end; 
  n+=1;
end