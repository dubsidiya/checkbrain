// Автор: И.В.Свистун
##
uses school; 
var ch:=0; 
  for var i:=2532000 to 2532160 do 
      if i.IsPrime and (i mod 10=7) then begin ch+=1;Println(ch,i); end
 