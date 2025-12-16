// Автор: И.В.Свистун
##
uses school; var d:=0;
 for var i:=2 to 29999 do 
   for var j:=i+1 to 30000 do 
     if (i.Divisors.sum-i = j) and (i = j.Divisors.sum-j)then 
       begin Println(i,j); break; end;
      
      