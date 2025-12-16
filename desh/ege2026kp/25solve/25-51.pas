// Автор: И.В.Свистун
##
uses school;  var ch:=0;
  for var i:=3144472 to 3144600 do 
      if i.IsPrime then begin ch+=1; Println(ch,i); end;            
 