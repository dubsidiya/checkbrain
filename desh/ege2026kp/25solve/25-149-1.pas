// Автор: И.В.Свистун
##
uses school;  
  for var i:=55000000 to 60000000 do 
   if (i.Divisors.Where(t -> t.IsOdd).Count=5) then 
         Println(i,i.Divisors.Where(t -> t.IsOdd).max);
    
 
