// Автор: И.В.Свистун
##
uses school;  
  for var i:=194455 to 194500 do 
  begin
    var n:=i.Divisors;
      if n.Count=4 then Println(n);      
  end;
