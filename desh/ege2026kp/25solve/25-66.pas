// Автор: И.В.Свистун
##
uses school; 
var ch:=0; 
  for var i:=194441 to 196500 do 
      if i.IsPrime and (i mod 100=93) then begin ch+=1; Println(ch,i); end;
 