// Автор: И.В.Свистун
##
uses school;  
  for var i:=77777777 to 88888888 do     
   if (i.Divisors.Where(t -> t.IsOdd).Count=5) then          
    Println(i,i.Divisors.Where(t -> t.IsOdd).Slice(1,5));

 
