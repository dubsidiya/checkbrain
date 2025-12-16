// Автор: И.В.Свистун
##
uses school; 
var k:=1; 
  for var i:=3532000 to 3532160 do   
    if i.IsPrime then begin Println(k,i); k+=1; end;

