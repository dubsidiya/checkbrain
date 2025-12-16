##
uses school;
var n:=700001;  var ch:=0;
while (ch<5) do 
  begin 
     if (n mod 13=0) and (n mod 10000 div 1000<>4) 
     and (n mod 10<>2) and (not IntToStr(n).IsMatch('0??3')) 
     and (not IntToStr(n).IsMatch('1'))then
        begin ch+=1; println(ch, n, n.Digits.Sum) end;
        n+=1; 
  end
  {Найдите 5 минимальных чисел, больших 700000, которые кратны 13 и не 
подходят ни под одну из трех масок: *0??3*, *4??2 и *1*. Найденные числа 
запишите  в  порядке  возрастания,  справа  от  каждого  найденного  числа 
укажите сумму значений разрядов. } 