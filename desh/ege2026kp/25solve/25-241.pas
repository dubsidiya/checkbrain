// Автор: И.В.Свистун
###
uses school;
var n:=336;  var ch:=0;
while (ch<7) do 
  begin 
     if (n mod 6 =0) and (n mod 7 =0) and (n mod 8 =0) 
     and(n mod 10=6) and (IntToStr(n).Cnt('6')>=3)
         then              
            if (n.ToString?[2:3]='6')then 
              begin ch+=1; println(ch, n, n.Divisors.Sum) end;              
        n+=1; 
  end
  