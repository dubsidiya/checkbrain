// Автор: И.В.Свистун
##
var c:='0123456789';
foreach var t6 in c do
  foreach var t8 in c do
begin
  var n:=('12345'+t6+'6'+t8+'8').ToInteger;
  if (n mod 17=0)then println(n, n div 17); 
  end;
