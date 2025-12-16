// Автор: И.В.Свистун
##
uses school; 
 var m:=400000; var ch:=0;
 for var i:=345293  downto 158928 do 
   begin
     var n:= i.Divisors; var p:=1;var k:=0;
      for var j:=1 to i.DivisorsCount-2 do
       if (n[j].IsPrime) then begin p:=p*n[j]; k+=1; end; 
       if (k=3) and (p=i) then begin m:=i; ch+=1;end;
   end;
 print(ch, m);


{Рассматриваются целые числа, принадлежащих числовому отрезку [158928; 345293],
 которые представляют собой произведение трёх различных простых делителей. 
 В ответе запишите количество таких чисел и минимальное из них.}