// Автор: И.В.Свистун
##
uses school;  
  for var i:=174457 to 174505 do 
  begin
    var n:=i.Divisors;
      if n.Count=4 then Println(n[1],n[2]);             
  end;
