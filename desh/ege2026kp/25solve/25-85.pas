// Автор: И.В.Свистун
##
uses school; 
var ch:=0;
 for var i:=3661 to 33625 do         
      if (i.DivisorsCount=3) then ch+=1;      
      Println(ch);
 