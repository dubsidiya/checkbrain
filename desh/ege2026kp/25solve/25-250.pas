// Автор: И.В.Свистун
##
uses school;
var n:=73000;  var ch:=0;
while (ch<5) do 
  begin 
     if (n mod 73=0) and (n mod 100=76) and (IntToStr(n).IsMatch('12345'))
         then              
            if (n.ToString?[:6]='12345')then 
              begin ch+=1; println(ch, n, n div 73) end;
              
        n+=1; 
  end
  