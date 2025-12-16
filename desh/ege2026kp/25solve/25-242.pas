// Автор: И.В.Свистун
###
uses school;
var n:=1500000;  var ch:=0;
while (ch<7) do 
  begin 
     if (n mod 217 =0) and (IntToStr(n).Cnt('4')>=2)
     and (n.ToString?[1:3]='14')and (n.ToString?[4:5]='4')then 
              begin ch+=1; 
              print(ch, n);
              n.Divisors.Where(t -> t.IsOdd).Sum.Println;end;
        n-=1; 
  end
  //в ответ пары выписываются снизу вверх