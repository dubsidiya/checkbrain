// Автор: И.В.Свистун
##
uses school; 
var d:=0;
 for var i:=2 to 20000 do 
      if (i.Divisors.sum - i > i)then d+=1;
Println(d);