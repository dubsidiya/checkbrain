// Автор: И.В.Свистун
###
uses school;
var n:=65001;  var ch:=0;
while (ch<7) do 
  begin 
     if (n.ToString[^2]='5')and (n.ToString.Contains('97')) 
     and(n.ToString?[1:2]='6') and (n.Divisors.Where(t -> t.IsEven).count>=4)then
               begin ch+=1;
              println(ch, n, n.Divisors.Where(t -> t.IsEven).Sum);
              end;
        n+=1; 
  end
  //в ответ пары выписываются снизу вверх