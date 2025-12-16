// Автор: И.В.Свистун
##
uses school; 
var k:=0; var m:=0;
 for var i:=217437 downto 173225 do  
       if (i.DivisorsCount=4) and i.Divisors[1].IsPrime and i.Divisors[2].IsPrime
           then if(i.Divisors[2]mod 10=i.Divisors[1]mod 10) then begin m:=i;k+=1;end;
            print(k,m);

{Среди целых чисел, принадлежащих числовому отрезку [173225; 217437], 
найдите числа, которые представляют собой произведение двух различных 
простых делителей, заканчивающихся на одну и ту же цифру. 
Запишите в ответе количество таких чисел и минимальное их них.}