// Автор: И.В.Свистун
##
uses school;
var c:='0123456789ABCDEF';
foreach var t2 in c do
  foreach var t6 in c do
begin
  var sl:='1'+t2+'DED'+t6+'CED';
  var n:=dec(sl,16);
  if (n mod 121=0)then  println(n, n div 121); 
  end;
// пары в ответ выписываются снизу вверх  
