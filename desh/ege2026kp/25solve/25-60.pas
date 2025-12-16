// Автор: И.В.Свистун
##
uses school; var ch:=0; 
  for var i:=3532160 downto 3532000 do 
      if i.IsPrime then begin ch+=1; Println(ch,i); end            
 