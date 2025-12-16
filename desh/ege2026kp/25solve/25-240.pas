// Автор: И.В.Свистун
###
uses school;
var n:=9999999;  var ch:=0;
while (ch<5) do 
  begin 
     if (n mod 10 =7)and (n.ToString.Contains('55')) and(n.ToString?[1:2]='9')
     then
              begin ch+=1; 
              println(ch, n, n.Divisors.Sum mod 21);end;
        n-=1; 
  end
  //в ответ пары выписываются снизу вверх