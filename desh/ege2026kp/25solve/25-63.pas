// Автор: И.В.Свистун
##
uses school; 
var ch:=0; 
  for var i:=2532000 to 2532160 do 
    begin
      if i.IsPrime then begin ch+=1; Println(ch,i);  end;
      if ch=5 then break;
      end;
 