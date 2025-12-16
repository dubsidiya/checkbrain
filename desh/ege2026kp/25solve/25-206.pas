// Автор: И.В.Свистун
##
var c:='0123456789';
foreach var t2 in c do
  foreach var t8 in c do
begin
  var n:=('1'+t2+'34567'+t8+'9').ToInteger;
  if (n mod 17=0)then println(n, n div 17); 
  end;
