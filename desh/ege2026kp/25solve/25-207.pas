// Автор: И.В.Свистун
##
for var n:=1235670 to 123999999 do
begin
  if (n mod 169=0)and (n mod 10000 in [5670..5679])then      
   if (n.ToString[:4]='123')then  println(n, n div 169);
end