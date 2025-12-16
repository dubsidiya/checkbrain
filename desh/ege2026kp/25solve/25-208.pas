// Автор: И.В.Свистун
##
for var n:=1245 to 1000000 do
begin
  if (n mod 51=0)then
  if (n.ToString[:3]='12')and (n.ToString.Contains('45')) then  println(n, n div 51); 
end
