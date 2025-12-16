##
uses school; 
 var m:=400000; var ch:=0; var v:=0;
 for var i:=485617  to 529678 do 
   begin
     var n:= i.Divisors; var p:=lst(1);var k:=0;
      for var j:=1 to i.DivisorsCount-2 do
       if (n[j].IsPrime) then p.Add(n[j]); 
      var flag:=true;
      if (p.Count=4) then
        begin
      for var j:=1 to 3 do
       if (p[1] mod 10<>p[2] mod 10) or (p[1] mod 10<>p[3] mod 10) 
       or (p[3] mod 10<>p[2] mod 10) then flag:=false;
       if  (p.Product=i) and flag  then
         begin
         ch+=1; 
         if (p[3]-p[1]<m) then begin m:=p[3]-p[1]; v:=i; end;
                 end; end;end;
            print(ch, v);


{Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
 которые представляют собой произведение трёх различных простых делителей, 
 оканчивающихся на одну и ту же цифру. В ответе запишите количество таких чисел
 и такое из них, для которого разность наибольшего и наименьшего простых делителей
 минимальна.}