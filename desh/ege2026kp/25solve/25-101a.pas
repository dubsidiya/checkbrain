// Автор: И.В.Свистун
##
uses school; 
var k:=0; var m:=0;
 for var i:=125697  to 190234 do 
   begin
     var d:= divisors(i); d.Remove(1); d.Remove(i); 
       if (d.Count=2) and (d[0].IsPrime) and (d[1].IsPrime) and (d.product=i)
            then begin m:=i ; k+=1; end; end;
            print(k,m);

{Среди целых чисел, принадлежащих числовому отрезку [125697;190234],
найдите числа, которые представляют собой произведение 
двух различных простых делителей. 
Запишите в ответе количество таких чисел и максимальное их них.}