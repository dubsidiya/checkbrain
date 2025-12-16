// Автор: И.В.Свистун
##
uses school; 
var ch:=0; 
  for var i:=2 to 20000 do 
      if i.IsPrime then ch+=1;
      Println(ch);
 